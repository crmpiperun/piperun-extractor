from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Call:
    id: int | None
    user_id: int | None
    from_user_id: int | None
    deal_id: int | None
    company_id: int | None
    person_id: int | None
    username: str | None
    from_number: str | None
    to_number: str | None
    record_audio: str | None
    from_caller_ref: str | None
    to_caller_ref: str | None
    description_html: str | None
    description_text: str | None
    start_at: datetime | None
    end_at: datetime | None
    record_url: str | None
    external_call_id: str | None
    is_important: bool | None
    duration: str | None
    cost: float | None
    created_at: datetime | None
    updated_at: datetime | None
    is_running_ai: bool | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.from_user_id = utils.parse_int(k, 'from_user_id')  # User.id
        self.deal_id = utils.parse_int(k, 'deal_id')  # Deal.id
        self.company_id = utils.parse_int(k, 'company_id')  # Company.id
        self.person_id = utils.parse_int(k, 'person_id')  # Person.id
        self.username = utils.parse_str(k, 'username')
        self.from_number = utils.parse_str(k, 'from_number')
        self.to_number = utils.parse_str(k, 'to_number')
        self.record_audio = utils.parse_url(k, 'record_audio')
        self.from_caller_ref = utils.parse_str(k, 'from_caller_id')
        self.to_caller_ref = utils.parse_str(k, 'to_caller_id')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.start_at = utils.parse_date(k, 'start_at')
        self.end_at = utils.parse_date(k, 'end_at')
        self.record_url = utils.parse_url(k, 'record_url')
        self.external_call_id = utils.parse_str(k, 'external_call_id')
        self.is_important = utils.parse_bool(k, 'important')
        self.duration = utils.parse_str(k, 'duration')
        self.cost = utils.parse_float(k, 'cost')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.is_running_ai = utils.parse_bool(k, 'running_ai')
