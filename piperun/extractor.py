import inspect
import logging
import math
import re
import time
from collections.abc import Iterator as CollectionsIterator
from datetime import datetime
from functools import partial
from typing import Iterator, Dict, Any, Type, TypeVar, List, get_origin

import requests
from requests.exceptions import RequestException

import piperun.schema.activities
import piperun.schema.calls
import piperun.schema.cities
import piperun.schema.cnaes
import piperun.schema.companies
import piperun.schema.custom_forms
import piperun.schema.data_lists
import piperun.schema.deals
import piperun.schema.emails
import piperun.schema.items
import piperun.schema.notes
import piperun.schema.origins
import piperun.schema.person
import piperun.schema.pipeline
import piperun.schema.proposals
import piperun.schema.regions
import piperun.schema.tags
import piperun.schema.users
from piperun import utils

T = TypeVar('T')


class PipeRunExtractor:
    VERSION = '1.0.1'

    def __init__(self,
                 token: str,
                 token_throttle: str = '',
                 origin: str = '',
                 log_level: str = 'WARNING',
                 base_url: str = 'https://api.pipe.run/v1',
                 ):
        self.base_url = base_url.strip('/')

        if not re.fullmatch(r"[a-fA-F0-9]{32}", token):
            raise Exception('Invalid token')

        if token_throttle and not re.fullmatch(r"[a-fA-F0-9]{32}", token_throttle):
            raise Exception('Invalid skip throttle token')

        self.headers = {
            'Token': token,
            'X-Token-Skip-Throttle': token_throttle,
            'X-Application-Piperun': 'Lib_Python_ETL',
            'User-Agent': 'PipeRun API Python Client - v' + self.VERSION,
            'Origin': utils.parse_origin(origin),
        }

        self.logger = logging.getLogger('piperun')
        self.logger.setLevel(log_level.upper())
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def _fetch(self, schema_class: Type[T], endpoint: str, params: Dict[str, str | int]) -> Iterator:
        # For performance reasons, do not change this defaults
        params['show'] = max(1, min(200, int(params.get('show', 10))))
        params['sort'] = 'id'
        params['desc'] = 'false'

        cursor = ''
        counter = 0
        while True:
            params['cursor'] = cursor

            data = self._do_request(f'{self.base_url}/{endpoint}', params)

            data_items = data.get('data', [])

            if not isinstance(data_items, list):
                self.logger.error(f'Invalid response: {data}')
                break

            if not data_items:
                break

            counter += len(data_items)
            self.logger.info(f'Requesting {endpoint}: {counter}')

            for item in data_items:
                yield schema_class(**item)

            cursor = data.get('meta', {}).get('cursor', {}).get('next')
            if not cursor:
                break

    def _do_request(self, endpoint: str, params: Dict[str, str | int]) -> Any:
        attempt = 0
        retry_after = 5  # 5,25,125 seconds
        while attempt < 3:
            attempt += 1

            code = 0
            try:
                self.logger.debug(f'Requesting {endpoint} with params {params}')
                response = requests.get(endpoint, params=params, headers=self.headers, timeout=60, verify=True)
                code = response.status_code
                retry_after = max(retry_after, int(response.headers.get('Retry-After', retry_after)))

                if 200 <= code < 300:
                    return response.json()
            except RequestException as e:
                self.logger.error(f'Request failed with exception: {e}')
                pass

            # Abort on redirect
            if 300 <= code < 400:
                self.logger.error('Abort: Redirect not supported')
                raise Exception('Redirect not supported')

            # Abort on invalid token
            if code in (401, 403):
                self.logger.error('Abort: Invalid token')
                raise Exception('Invalid token')

            # Wait and retry in case of errors
            if code == 429:
                self.logger.warning(f'Rate limit exceeded. Retrying in {retry_after} seconds.')
            else:
                self.logger.error(f'Request failed with status code {code}. Retrying in {retry_after} seconds.')
                # if error is unknown, timeout, 5xx or 4xx: reduce the number of items to retrieve
                params['show'] = max(1, min(200, math.ceil(int(params.get('show', 1)) / 2)))  # Cut show in half every error

            time.sleep(retry_after ** attempt)  # Exponential backoff

        self.logger.error(f'Abort: Request failed after {attempt} attempts.')
        raise Exception(f'Request failed after {attempt} attempts.')

    def all(self, after: datetime) -> List:
        methods = []

        for name, member in inspect.getmembers(self, inspect.ismethod):
            # Skip private methods
            if name.startswith('_'):
                continue

            # Check if the return type is an Iterator
            if get_origin(inspect.signature(member).return_annotation) in (Iterator, CollectionsIterator):
                methods.append((name, partial(member, after=after)))

        return methods

    def users(self, after: datetime) -> Iterator[piperun.schema.users.User]:
        return self._fetch(piperun.schema.users.User, 'users', {'show': 200})  # full fetch

    def users_teams(self, after: datetime) -> Iterator[piperun.schema.users.Team]:
        return self._fetch(piperun.schema.users.Team, 'teams', {'show': 200})  # full fetch

    def users_team_groups(self, after: datetime) -> Iterator[piperun.schema.users.TeamGroup]:
        return self._fetch(piperun.schema.users.TeamGroup, 'teamGroup', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def pipelines(self, after: datetime) -> Iterator[piperun.schema.pipeline.Pipeline]:
        return self._fetch(piperun.schema.pipeline.Pipeline, 'pipelines', {'show': 200})  # full fetch

    def pipelines_stages(self, after: datetime) -> Iterator[piperun.schema.pipeline.Stage]:
        return self._fetch(piperun.schema.pipeline.Stage, 'stages', {'show': 200})  # full fetch

    def deals(self, after: datetime) -> Iterator[piperun.schema.deals.Deal]:
        return self._fetch(piperun.schema.deals.Deal, 'deals', {'show': 100, 'with': 'tags', 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def deals_stage_histories(self, after: datetime) -> Iterator[piperun.schema.deals.StageHistory]:
        return self._fetch(piperun.schema.deals.StageHistory, 'stageHistories', {'show': 200, 'in_date_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def deals_lost_reasons(self, after: datetime) -> Iterator[piperun.schema.deals.LostReason]:
        return self._fetch(piperun.schema.deals.LostReason, 'lostReasons', {'show': 200})  # full fetch

    def companies(self, after: datetime) -> Iterator[piperun.schema.companies.Company]:
        return self._fetch(piperun.schema.companies.Company, 'companies', {'show': 100, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def companies_segments(self, after: datetime) -> Iterator[piperun.schema.companies.Segment]:
        return self._fetch(piperun.schema.companies.Segment, 'segments', {'show': 200})  # full fetch

    def persons(self, after: datetime) -> Iterator[piperun.schema.person.Person]:
        return self._fetch(piperun.schema.person.Person, 'persons', {'show': 100, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def activities(self, after: datetime) -> Iterator[piperun.schema.activities.Activity]:
        return self._fetch(piperun.schema.activities.Activity, 'activities', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def activities_types(self, after: datetime) -> Iterator[piperun.schema.activities.ActivityType]:
        return self._fetch(piperun.schema.activities.ActivityType, 'activityTypes', {'show': 200})  # full fetch

    def proposals(self, after: datetime) -> Iterator[piperun.schema.proposals.Proposal]:
        return self._fetch(piperun.schema.proposals.Proposal, 'proposals', {'show': 100, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def proposal_model(self, after: datetime) -> Iterator[piperun.schema.proposals.ProposalModel]:
        return self._fetch(piperun.schema.proposals.ProposalModel, 'proposals/models', {'show': 200})  # full fetch

    def proposal_layout(self, after: datetime) -> Iterator[piperun.schema.proposals.ProposalLayout]:
        return self._fetch(piperun.schema.proposals.ProposalLayout, 'proposals/layouts', {'show': 200})  # full fetch

    def proposals_payment_methods(self, after: datetime) -> Iterator[piperun.schema.proposals.PaymentMethod]:
        return self._fetch(piperun.schema.proposals.PaymentMethod, 'paymentMethods', {'show': 200})  # full fetch

    def proposals_payment_methods_types(self, after: datetime) -> Iterator[piperun.schema.proposals.PaymentMethodsType]:
        return self._fetch(piperun.schema.proposals.PaymentMethodsType, 'paymentMethodTypes', {'show': 200})  # full fetch

    def proposals_parcel_payments(self, after: datetime) -> Iterator[piperun.schema.proposals.ProposalParcel]:
        return self._fetch(piperun.schema.proposals.ProposalParcel, 'proposalParcelPayments', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def cities(self, after: datetime) -> Iterator[piperun.schema.cities.City]:
        return self._fetch(piperun.schema.cities.City, 'cities', {'show': 200})  # full fetch

    def calls(self, after: datetime) -> Iterator[piperun.schema.calls.Call]:
        return self._fetch(piperun.schema.calls.Call, 'calls', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def custom_fields(self, after: datetime) -> Iterator[piperun.schema.custom_forms.CustomFieldResponse]:
        return self._fetch(piperun.schema.custom_forms.CustomFieldResponse, 'customFields', {'show': 200})  # full fetch

    def custom_forms(self, after: datetime) -> Iterator[piperun.schema.custom_forms.CustomForm]:
        return self._fetch(piperun.schema.custom_forms.CustomForm, 'customForms', {'show': 200, 'with': 'fields'})  # full fetch

    def notes(self, after: datetime) -> Iterator[piperun.schema.notes.Note]:
        return self._fetch(piperun.schema.notes.Note, 'notes', {'show': 100, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def items(self, after: datetime) -> Iterator[piperun.schema.items.Item]:
        return self._fetch(piperun.schema.items.Item, 'items', {'show': 200})  # full fetch

    def items_characteristics(self, after: datetime) -> Iterator[piperun.schema.items.Characteristic]:
        return self._fetch(piperun.schema.items.Characteristic, 'items/characteristics', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def items_categories(self, after: datetime) -> Iterator[piperun.schema.items.Category]:
        return self._fetch(piperun.schema.items.Category, 'itemCategories', {'show': 200})  # full fetch

    def items_measurement_units(self, after: datetime) -> Iterator[piperun.schema.items.MeasurementUnit]:
        return self._fetch(piperun.schema.items.MeasurementUnit, 'measurementUnit', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def datalists(self, after: datetime) -> Iterator[piperun.schema.data_lists.DataList]:
        return self._fetch(piperun.schema.data_lists.DataList, 'datalists', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def tags(self, after: datetime) -> Iterator[piperun.schema.tags.Tag]:
        return self._fetch(piperun.schema.tags.Tag, 'tags', {'show': 200})  # full fetch

    def cnaes(self, after: datetime) -> Iterator[piperun.schema.cnaes.Cnae]:
        return self._fetch(piperun.schema.cnaes.Cnae, 'cnaes', {'show': 200})  # full fetch

    def emails(self, after: datetime) -> Iterator[piperun.schema.emails.Email]:
        return self._fetch(piperun.schema.emails.Email, 'emails', {'show': 100, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def emails_templates(self, after: datetime) -> Iterator[piperun.schema.emails.EmailTemplate]:
        return self._fetch(piperun.schema.emails.EmailTemplate, 'email/templates', {'show': 200})

    def origins(self, after: datetime) -> Iterator[piperun.schema.origins.Origin]:
        return self._fetch(piperun.schema.origins.Origin, 'origins', {'show': 200})  # full fetch

    def origins_groups(self, after: datetime) -> Iterator[piperun.schema.origins.OriginGroup]:
        return self._fetch(piperun.schema.origins.OriginGroup, 'originGroups', {'show': 200, 'updated_at_start': after.strftime('%Y-%m-%d %H:%M:%S')})

    def regions(self, after: datetime) -> Iterator[piperun.schema.regions.Region]:
        return self._fetch(piperun.schema.regions.Region, 'regions', {'show': 200})  # full fetch
