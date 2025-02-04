from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Company:
    id: int | None
    owner_id: int | None
    manager_id: int | None
    manager_field_sales_id: int | None
    cnae_id: int | None
    city_id: int | None
    segment_id: int | None
    name: str | None
    cnpj: str | None
    website: str | None
    email_nf: str | None
    logo: str | None
    observation_text: str | None
    observation_html: str | None
    address_postal_code: str | None
    address: str | None
    address_number: str | None
    address_complement: str | None
    company_name: str | None
    ie: str | None
    district: str | None
    country: str | None
    facebook: str | None
    linkedin: str | None
    cep: str | None
    company_type: str | None
    company_status: str | None
    company_situation: str | None
    status_touch: str | None
    nps_score: str | None
    social_capital: float | None
    legal_nature: str | None
    status: int | None
    external_code: str | None
    size: str | None
    customer_at: datetime | None
    foundation_at: datetime | None
    updated_at: datetime | None
    created_at: datetime | None
    is_brand: bool | None
    is_supplier: bool | None
    is_client: bool | None
    is_carrier: bool | None
    is_franchise: bool | None
    is_channel: bool | None
    is_distributor: bool | None
    is_manufacturer: bool | None
    is_partner: bool | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.owner_id = utils.parse_int(k, 'owner_id')  # User.id
        self.manager_id = utils.parse_int(k, 'manager_id')  # User.id
        self.manager_field_sales_id = utils.parse_int(k, 'manager_field_sales_id')  # User.id
        self.cnae_id = utils.parse_int(k, 'cnae_id')  # Cnae.id
        self.city_id = utils.parse_int(k, 'city_id')  # City.id
        self.segment_id = utils.parse_int(k, 'segment_id')  # Segment.id
        self.name = utils.parse_str(k, 'name')
        self.cnpj = utils.parse_str(k, 'cnpj')
        self.website = utils.parse_url(k, 'website')
        self.email_nf = utils.parse_mail(k, 'email_nf')
        self.logo = utils.parse_url(k, 'logo')
        self.observation_text = utils.parse_html2text(k, 'observation')
        self.observation_html = utils.parse_str(k, 'observation')
        self.address_postal_code = utils.parse_str(k, 'address_postal_code')
        self.address = utils.parse_str(k, 'address')
        self.address_number = utils.parse_str(k, 'address_number')
        self.address_complement = utils.parse_str(k, 'address_complement')
        self.company_name = utils.parse_str(k, 'company_name')
        self.ie = utils.parse_str(k, 'ie')
        self.district = utils.parse_str(k, 'district')
        self.country = utils.parse_str(k, 'country')
        self.facebook = utils.parse_url(k, 'facebook')
        self.linkedin = utils.parse_url(k, 'linkedin')
        self.cep = utils.parse_str(k, 'cep')
        self.company_type = utils.parse_str(k, 'company_type')
        self.company_status = utils.parse_str(k, 'company_status')
        self.company_situation = utils.parse_str(k, 'company_situation')
        self.status_touch = utils.parse_str(k, 'status_touch')
        self.nps_score = utils.parse_str(k, 'nps_score')
        self.social_capital = utils.parse_float(k, 'social_capital')
        self.legal_nature = utils.parse_str(k, 'legal_nature')
        self.status = utils.parse_int(k, 'status')
        self.external_code = utils.parse_str(k, 'external_code')
        self.size = utils.parse_str(k, 'size')
        self.customer_at = utils.parse_date(k, 'customer_at')
        self.foundation_at = utils.parse_date(k, 'foundation_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')
        self.is_brand = utils.parse_bool(k, 'is_brand')
        self.is_supplier = utils.parse_bool(k, 'is_supplier')
        self.is_client = utils.parse_bool(k, 'is_client')
        self.is_carrier = utils.parse_bool(k, 'is_carrier')
        self.is_franchise = utils.parse_bool(k, 'is_franchise')
        self.is_channel = utils.parse_bool(k, 'is_channel')
        self.is_distributor = utils.parse_bool(k, 'is_distributor')
        self.is_manufacturer = utils.parse_bool(k, 'is_manufacturer')
        self.is_partner = utils.parse_bool(k, 'is_partner')


@dataclass
class Segment:
    id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None
    sector: int | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.sector = utils.parse_int(k, 'sector')
