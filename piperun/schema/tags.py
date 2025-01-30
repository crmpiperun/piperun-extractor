from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Tag:
    id: int | None
    user_id: int | None
    name: str | None
    color: str | None
    created_at: datetime | None
    belongs: int | None
    is_active: bool | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.name = utils.parse_str(k, 'name')
        self.color = utils.parse_str(k, 'color')
        self.created_at = utils.parse_date(k, 'created_at')
        self.belongs = utils.parse_int(k, 'belongs')
        self.is_active = utils.parse_bool(k, 'active')
