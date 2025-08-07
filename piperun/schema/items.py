from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Item:
    id: int | None
    category_id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None
    minimum_value: float | None
    cost: float | None
    reference: str | None
    type: int | None
    type_name: str | None
    is_active: bool | None
    photo: str | None
    commission: float | None
    brand_id: int | None
    ipi_tax: float | None
    measurement_unit_id: int | None
    code: str | None
    fix_commission_value: float | None
    is_product_belong_deal: bool | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.category_id = utils.parse_int(k, 'category_id')  # Category.id
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.minimum_value = utils.parse_float(k, 'minimum_value')
        self.cost = utils.parse_float(k, 'cost')
        self.reference = utils.parse_str(k, 'reference')
        self.type = utils.parse_int(k, 'type')
        self.type_name = {0: 'Produto', 1: 'MRR', 2: 'Serviço', None: None}.get(self.type)
        self.is_active = not utils.parse_bool(k, 'status')
        self.photo = utils.parse_url(k, 'photo')
        self.commission = utils.parse_float(k, 'commission')
        self.brand_id = utils.parse_int(k, 'brand_id')  # Company.id
        self.ipi_tax = utils.parse_float(k, 'ipi_tax')
        self.measurement_unit_id = utils.parse_int(k, 'measurement_unit_id')  # MeasurementUnit.id
        self.code = utils.parse_str(k, 'code')
        self.fix_commission_value = utils.parse_float(k, 'fix_commission_value')
        self.is_product_belong_deal = utils.parse_bool(k, 'is_product_belong_deal')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')


@dataclass
class MeasurementUnit:
    id: int | None
    name: str | None
    abbreviation: str | None
    decimal_places: int | None
    created_at: datetime | None
    updated_at: datetime | None
    is_active: bool | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.abbreviation = utils.parse_str(k, 'abbreviation')
        self.decimal_places = utils.parse_int(k, 'decimal_places')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.is_active = utils.parse_bool(k, 'active')


@dataclass
class Characteristic:
    id: int | None
    name: str | None
    description: str | None
    created_at: datetime | None
    updated_at: datetime | None
    options: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description = utils.parse_str(k, 'description')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.options = utils.parse_list(k, 'options', CharacteristicOption)


@dataclass
class CharacteristicOption:
    id: int | None
    name: str | None
    description: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description = utils.parse_str(k, 'description')


@dataclass
class Category:
    id: int | None
    category_id: int | None
    name: str | None
    description: str | None
    reference: str | None
    is_deleted: bool | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.category_id = utils.parse_int(k, 'category_id')  # Category.id if subcategory
        self.name = utils.parse_str(k, 'name')
        self.description = utils.parse_str(k, 'description')
        self.reference = utils.parse_str(k, 'reference')
        self.is_deleted = utils.parse_bool(k, 'deleted')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.created_at = utils.parse_date(k, 'created_at')
