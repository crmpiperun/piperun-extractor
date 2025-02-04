from dataclasses import dataclass
from datetime import datetime

from piperun import utils
from piperun.schema.tags import Tag


@dataclass
class Deal:
    id: int | None
    owner_id: int | None
    stage_id: int | None
    started_in_stage_id: int | None
    pipeline_id: int | None
    person_id: int | None
    company_id: int | None
    origin_id: int | None
    lost_reason_id: int | None
    reference_type: int | None
    reference_text: str | None
    temperature: int | None
    temperature_text: str | None
    probability: float | None
    title: str | None
    description_html: str | None
    description_text: str | None
    observation_html: str | None
    observation_text: str | None
    status: int | None
    status_text: str | None
    closed_reason: str | None
    closed_at: datetime | None
    lost_at: datetime | None
    frozen_at: datetime | None
    last_stage_updated_at: datetime | None
    probably_closed_at: datetime | None
    last_contact_at: datetime | None
    stage_changed_at: datetime | None
    lead_time: int | None
    is_deleted: bool | None
    is_freezed: bool | None
    value: float | None
    value_mrr: float | None
    created_at: datetime | None
    updated_at: datetime | None
    tags: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.owner_id = utils.parse_int(k, 'owner_id')  # User.id
        self.stage_id = utils.parse_int(k, 'stage_id')  # Stage.id
        self.started_in_stage_id = utils.parse_int(k, 'started_in_stage_id')  # Stage.id
        self.pipeline_id = utils.parse_int(k, 'pipeline_id')  # Pipeline.id
        self.person_id = utils.parse_int(k, 'person_id')  # Person.id
        self.company_id = utils.parse_int(k, 'company_id')  # Company.id
        self.origin_id = utils.parse_int(k, 'origin_id')  # Origin.id
        self.lost_reason_id = utils.parse_int(k, 'lost_reason_id')  # LostReason.id
        self.reference_type = utils.parse_int(k, 'type_reference')
        self.reference_text = utils.parse_str(k, 'reference')
        self.temperature = utils.parse_int(k, 'temperature')
        self.temperature_text = {1: 'Very Hot', 2: 'Hot', 3: 'LukeWarm', 4: 'Cold', 5: 'Not Informed', None: None}.get(self.temperature)
        self.probability = utils.parse_float(k, 'probability')
        self.title = utils.parse_str(k, 'title')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.observation_html = utils.parse_str(k, 'observation')
        self.observation_text = utils.parse_html2text(k, 'observation')
        self.status = utils.parse_int(k, 'status')
        self.status_text = {0: 'open', 1: 'closed', 3: 'lost', None: None}.get(self.status)
        self.closed_reason = utils.parse_str(k, 'reason_close')
        self.closed_at = utils.parse_date(k, 'closed_at')
        self.lost_at = utils.parse_date(k, 'closed_at') if self.status == 3 else None
        self.frozen_at = utils.parse_date(k, 'frozen_at')
        self.last_stage_updated_at = utils.parse_date(k, 'last_stage_updated_at')
        self.probably_closed_at = utils.parse_date(k, 'probably_closed_at')
        self.last_contact_at = utils.parse_date(k, 'last_contact_at')
        self.stage_changed_at = utils.parse_date(k, 'stage_changed_at')
        self.lead_time = utils.parse_int(k, 'lead_time')
        self.is_deleted = utils.parse_bool(k, 'deleted')
        self.is_freezed = utils.parse_bool(k, 'freezed')
        self.value = utils.parse_float(k, 'value')
        self.value_mrr = utils.parse_float(k, 'value_mrr')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.tags = utils.parse_list(k, 'tags', Tag)


@dataclass
class StageHistory:
    id: int | None
    deal_id: int | None
    in_stage_id: int | None
    out_stage_id: int | None
    in_user_id: int | None
    out_user_id: int | None
    in_date: datetime | None
    out_date: datetime | None
    in_value: int | None
    out_value: int | None
    lead_time: str | None
    lead_time_days_and_second: str | None
    deleted_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.deal_id = utils.parse_int(k, 'deal_id')  # Deal.id
        self.in_stage_id = utils.parse_int(k, 'in_stage_id')  # Stage.id
        self.out_stage_id = utils.parse_int(k, 'out_stage_id')  # Stage.id
        self.in_user_id = utils.parse_int(k, 'in_user_id')  # User.id
        self.out_user_id = utils.parse_int(k, 'out_user_id')  # User.id
        self.in_date = utils.parse_date(k, 'in_date')
        self.out_date = utils.parse_date(k, 'out_date')
        self.in_value = utils.parse_int(k, 'in_value')
        self.out_value = utils.parse_int(k, 'out_value')
        self.lead_time = utils.parse_str(k, 'lead_time')
        self.lead_time_days_and_second = utils.parse_str(k, 'lead_time_days_and_second')
        self.deleted_at = utils.parse_date(k, 'deleted_at')


@dataclass
class LostReason:
    id: int | None
    name: str | None
    is_active: bool | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.is_active = utils.parse_bool(k, 'status')
