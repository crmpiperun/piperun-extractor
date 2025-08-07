from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Origin:
    id: int | None
    origin_group_id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None
    is_active: bool | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.origin_group_id = utils.parse_int(k, 'origin_group_id')  # OriginGroup.id
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.is_active = utils.parse_bool(k, 'active')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')


@dataclass
class OriginGroup:
    id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None
    is_active: bool | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.is_active = utils.parse_bool(k, 'active')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')
