from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Goal:
    id: int
    visibility: int
    visibility_name: str
    type: int
    goal_for: int
    goal_for_name: str
    type_name: str
    type_of_period_name: str
    item_criteria_name: str
    situation_name: str
    title: str
    observation: str | None
    state: str | None
    type_of_period: int
    item_criteria: int | None
    item_id: int | None
    activity_type_id: int | None
    origin_id: int | None
    region_id: int | None
    city_id: int | None
    segment_id: int | None
    created_by_id: int | None
    situation: int | None
    # value: float | None
    calculate_item_by_unit_value: bool | None
    active: bool | None
    start_at: datetime
    end_at: datetime
    created_at: datetime | None
    updated_at: datetime | None
    item_criterias: list | None
    deal_status: list | None
    deal_value_for: list | None
    proposal_status: list | None
    activity_status: list | None
    call_relevance: list | None
    signature_status: list | None
    item_criterias_in: list | None
    processed: list | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.visibility = utils.parse_int(k, 'visibility')
        self.visibility_name = {1: 'public', 2: 'private', 3: 'by_participant'}.get(self.visibility)
        self.type = utils.parse_int(k, 'type')
        self.type_name = {1: 'deals', 2: 'activities', 3: 'forecast', 4: 'proposals', 5: 'calls', 6: 'signatures'}.get(self.type)
        self.goal_for = utils.parse_int(k, 'goal_for')
        self.goal_for_name = {1: 'quantity', 2: 'value', 3: 'lead_tme', 4: 'lead_time_in_stage', 5: 'duration'}.get(self.goal_for)
        self.title = utils.parse_str(k, 'title')
        self.observation = utils.parse_str(k, 'observation')
        self.state = utils.parse_str(k, 'state')
        self.type_of_period = utils.parse_int(k, 'type_of_period')
        self.type_of_period_name = {0: 'custom_period', 1: 'day', 2: 'week', 3: 'two_week', 4: 'month', 5: 'bimester', 6: 'quarter', 7: 'semester',
                                    8: 'year'}.get(self.type_of_period)
        self.item_criteria = utils.parse_int(k, 'item_criteria')
        self.item_criteria_name = {1: 'category', 2: 'item', 3: 'type'}.get(self.item_criteria)
        self.item_id = utils.parse_int(k, 'item_id')  # Item.id
        self.activity_type_id = utils.parse_int(k, 'activity_type_id')  # ActivityType.id
        self.origin_id = utils.parse_int(k, 'origin_id')  # Origin.id
        self.region_id = utils.parse_int(k, 'region_id')  # Region.id
        self.city_id = utils.parse_int(k, 'city_id')  # City.id
        self.segment_id = utils.parse_int(k, 'segment_id')  # Segment.id
        self.created_by_id = utils.parse_int(k, 'created_by_id')  # User.id
        self.calculate_item_by_unit_value = utils.parse_bool(k, 'calculate_item_by_unit_value')
        self.active = utils.parse_bool(k, 'active')
        self.situation = utils.parse_int(k, 'situation')
        self.situation_name = {1: 'active', 2: 'close', 3: 'uninitialized'}.get(self.situation)
        self.start_at = utils.parse_date(k, 'start_at')
        self.end_at = utils.parse_date(k, 'end_at')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.item_criterias = utils.parse_list(k, 'item_criterias', str)
        self.deal_status = utils.parse_list(k, 'deal_status', str)
        self.deal_value_for = utils.parse_list(k, 'deal_value_for', str)
        self.proposal_status = utils.parse_list(k, 'proposal_status', str)
        self.activity_status = utils.parse_list(k, 'activity_status', str)
        self.call_relevance = utils.parse_list(k, 'call_relevance', str)
        self.signature_status = utils.parse_list(k, 'signature_status', str)
        self.item_criterias_in = utils.parse_list(k, 'item_criterias_in', str)
        self.processed = utils.parse_list(k, 'processed', Processed)
        # self.value = utils.parse_float(k, 'value')  # Valor da meta a ser atingida


@dataclass
class Processed:
    value: float | None
    id: int | None
    goal_id: int | None
    user_id: int | None
    team_id: int | None
    value: float | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.value = utils.parse_float(k, 'value') # value realized
        self.id = utils.parse_int(k, 'byUser.id')
        self.goal_id = utils.parse_int(k, 'byUser.goal_id')  # Goal.id
        self.user_id = utils.parse_int(k, 'byUser.user_id')  # User.id
        self.team_id = utils.parse_int(k, 'byUser.team_id')  # Team.id
        self.value = utils.parse_float(k, 'byUser.value')
        self.created_at = utils.parse_date(k, 'byUser.created_at')
        self.updated_at = utils.parse_date(k, 'byUser.updated_at')