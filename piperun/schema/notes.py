from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Note:
    id: int | None
    user_id: int | None
    deal_id: int | None
    company_id: int | None
    person_id: int | None
    call_id: int | None
    user_name: str | None
    text_html: str | None
    text_text: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.deal_id = utils.parse_int(k, 'deal_id')  # Deal.id
        self.company_id = utils.parse_int(k, 'company_id')  # Company.id
        self.person_id = utils.parse_int(k, 'person_id')  # Person.id
        self.call_id = utils.parse_int(k, 'call_id')  # Call.id
        self.user_name = utils.parse_str(k, 'user_name')
        self.text_html = utils.parse_str(k, 'text')
        self.text_text = utils.parse_html2text(k, 'text')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
