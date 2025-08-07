from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Activity:
    id: int | None
    owner_id: int | None
    activity_type_id: int | None
    requester_id: int | None
    deal_id: int | None
    status: int | None
    status_text: str | None
    time_utilized: int | None
    time_estimated: int | None
    duration: int | None
    priority: int | None
    type: int | None
    title: str | None
    description_html: str | None
    description_text: str | None
    comment: str | None
    start_at: datetime | None
    end_at: datetime | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.owner_id = utils.parse_int(k, 'owner_id')  # User.id
        self.activity_type_id = utils.parse_int(k, 'activity_type_id')  # ActivityType.id
        self.requester_id = utils.parse_int(k, 'requester_id')  # User.id
        self.deal_id = utils.parse_int(k, 'deal_id')  # Deal.id
        self.status = utils.parse_int(k, 'status')
        self.status_text = {0: 'open', 2: 'done', 4: 'no_show', None: None}.get(self.status)
        self.time_utilized = utils.parse_int(k, 'time_utilized')
        self.time_estimated = utils.parse_int(k, 'time_estimated')
        self.duration = utils.parse_int(k, 'duration')
        self.priority = utils.parse_int(k, 'priority')
        self.type = utils.parse_int(k, 'type')
        self.title = utils.parse_str(k, 'title')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.comment = utils.parse_str(k, 'comment')
        self.start_at = utils.parse_date(k, 'start_at')
        self.end_at = utils.parse_date(k, 'end_at')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class ActivityType:
    id: int | None
    activity_type_id: int | None
    name: str | None
    icon: str | None
    description_html: str | None
    description_text: str | None
    is_active: bool | None
    updated_at: datetime | None
    created_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.activity_type_id = utils.parse_int(k, 'activity_type_id')  # ActivityType.id if sub ActivityType
        self.name = utils.parse_str(k, 'name')
        self.icon = utils.parse_str(k, 'icon')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.is_active = utils.parse_bool(k, 'active')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')
