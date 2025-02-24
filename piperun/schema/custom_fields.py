from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class EntityHasCustomField:
    person_id: int | None
    company_id: int | None
    deal_id: int | None
    custom_field_id: int | None
    value: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.person_id = utils.parse_int(k, 'person_id')
        self.company_id = utils.parse_int(k, 'company_id')
        self.deal_id = utils.parse_int(k, 'deal_id')
        self.custom_field_id = utils.parse_int(k, 'custom_field_id')
        self.value = utils.parse_str(k, 'value')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')