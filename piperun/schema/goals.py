from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Entity:
    id: int | None
    name: str | None
    value: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.value = utils.parse_str(k, 'value')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class EntityAttribute:
    id: int | None
    name: str | None
    type: int | None
    type_text: str | None
    format: str | None
    date_field: str | None
    created_at: datetime | None
    updated_at: datetime | None
    entity: Entity | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.type = utils.parse_int(k, 'type')
        self.type_text = {0: 'count', 1: 'sum', None: None}.get(self.type)
        self.format = utils.parse_str(k, 'format')
        self.date_field = utils.parse_str(k, 'date_field')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.entity = utils.parse_obj(k, 'entity', Entity)


@dataclass
class SubGoal:
    id: int | None
    user_id: int | None
    value: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.value = utils.parse_str(k, 'value')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class Goal:
    id: int | None
    pipeline_id: int | None
    stage_id: int | None
    region_id: int | None
    custom_field_id: int | None
    custom_field_value: str | None
    title: str | None
    observation_text: str | None
    observation_html: str | None
    is_active: bool | None
    start_at: datetime | None
    end_at: datetime | None
    created_at: datetime | None
    updated_at: datetime | None
    sub_goals: list
    entity_attribute: EntityAttribute | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.pipeline_id = utils.parse_int(k, 'pipeline_id')  # Pipeline.id
        self.stage_id = utils.parse_int(k, 'stage_id')  # Stage.id
        self.region_id = utils.parse_int(k, 'region_id')  # Region.id
        self.custom_field_id = utils.parse_int(k, 'custom_field_id')  # CustomField.id
        self.custom_field_value = utils.parse_str(k, 'custom_field_value')
        self.title = utils.parse_str(k, 'title')
        self.observation_text = utils.parse_html2text(k, 'observation')
        self.observation_html = utils.parse_str(k, 'observation')
        self.is_active = utils.parse_bool(k, 'status')
        self.start_at = utils.parse_date(k, 'start_at')
        self.end_at = utils.parse_date(k, 'end_at')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.sub_goals = utils.parse_list(k, 'subGoals', SubGoal)
        self.entity_attribute = utils.parse_obj(k, 'entityAttribute', EntityAttribute)
