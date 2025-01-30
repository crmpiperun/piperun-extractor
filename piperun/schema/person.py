from dataclasses import dataclass
from datetime import datetime

from piperun import utils
from piperun.schema.custom_forms import CustomForm


@dataclass
class Person:
    id: int | None
    owner_id: int | None
    manager_id: int | None
    city_id: int | None
    cpf: str | None
    avatar: str | None
    name: str | None
    website: str | None
    job_title: str | None
    gender: str | None
    birth_day: datetime | None
    observation: str | None
    customer_at: datetime | None
    facebook: str | None
    linkedin: str | None
    address_postal_code: str | None
    address: str | None
    address_number: str | None
    address_complement: str | None
    district: str | None
    external_code: str | None
    updated_at: datetime | None
    created_at: datetime | None
    is_lgpd_declaration_accepted: bool | None
    customForms: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.owner_id = utils.parse_int(k, 'owner_id')  # User.id
        self.manager_id = utils.parse_int(k, 'manager_id')  # User.id
        self.city_id = utils.parse_int(k, 'city_id')  # City.id
        self.cpf = utils.parse_str(k, 'cpf')
        self.avatar = utils.parse_url(k, 'avatar')
        self.name = utils.parse_str(k, 'name')
        self.website = utils.parse_url(k, 'website')
        self.job_title = utils.parse_str(k, 'job_title')
        self.gender = utils.parse_str(k, 'gender')
        self.birth_day = utils.parse_date(k, 'birth_day')
        self.observation = utils.parse_str(k, 'observation')
        self.customer_at = utils.parse_date(k, 'customer_at')
        self.facebook = utils.parse_url(k, 'facebook')
        self.linkedin = utils.parse_url(k, 'linkedin')
        self.address_postal_code = utils.parse_str(k, 'address_postal_code')
        self.address = utils.parse_str(k, 'address')
        self.address_number = utils.parse_str(k, 'address_number')
        self.address_complement = utils.parse_str(k, 'address_complement')
        self.district = utils.parse_str(k, 'district')
        self.external_code = utils.parse_str(k, 'external_code')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')
        self.is_lgpd_declaration_accepted = utils.parse_bool(k, 'lgpd_declaration_accepted')
        self.customForms = utils.parse_list(k, 'customForms', CustomForm)
