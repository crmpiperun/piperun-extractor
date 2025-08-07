from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class User:
    id: int | None
    pipeline_id: int | None
    is_active: bool | None
    avatar: str | None
    birth_day: datetime | None
    cellphone: str | None
    cpf: str | None
    email: str | None
    last_login_at: datetime | None
    name: str | None
    name_tag: str | None
    permission: str | None
    telephone: str | None
    created_at: datetime | None
    created_by: int | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.pipeline_id = utils.parse_int(k, 'pipeline_id')  # Pipeline.id
        self.is_active = utils.parse_bool(k, 'active')
        self.avatar = utils.parse_url(k, 'avatar')
        self.birth_day = utils.parse_date(k, 'birth_day')
        self.cellphone = utils.parse_str(k, 'cellphone')
        self.cpf = utils.parse_str(k, 'cpf')
        self.email = utils.parse_mail(k, 'email')
        self.last_login_at = utils.parse_date(k, 'last_login_at')
        self.name = utils.parse_str(k, 'name')
        self.name_tag = utils.parse_str(k, 'name_tag')
        self.permission = utils.parse_str(k, 'permission')
        self.telephone = utils.parse_str(k, 'telephone')
        self.created_at = utils.parse_date(k, 'created_at')
        self.created_by = utils.parse_int(k, 'created_by')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class Team:
    id: int | None
    name: str | None
    description: str | None
    leader_id: int | None
    deal_user_id: int | None
    deal_quantity: int | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description = utils.parse_str(k, 'description')
        self.leader_id = utils.parse_int(k, 'leader_id')  # User.id
        self.deal_user_id = utils.parse_int(k, 'deal_user_id')  # User.id
        self.deal_quantity = utils.parse_int(k, 'deal_quantity')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')


@dataclass
class TeamGroup:
    id: int | None
    name: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
