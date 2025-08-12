from dataclasses import dataclass
from datetime import datetime

from piperun import utils

@dataclass
class CustomFieldResponse:
    id: int | None
    name: str | None
    description: str | None
    type: int | None
    type_name: str | None
    belongs: int | None
    belongs_name: str | None
    values: str | None
    numeric_currency_id: int | None
    numeric_decimal_places: int | None
    numeric_thousand_sep: int | None
    equation_formula: str | None
    equation_output_type: str | None
    equation_decimal_places: int | None
    equation_allow_negative: str | None
    equation_currency_id: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description = utils.parse_html2text(k, 'description')
        self.type = utils.parse_int(k, 'type')
        self.type_name = {1: 'text', 2: 'numeric_old', 3: 'select', 4: 'native', 5: 'long_text', 6: 'multi_select', 7: 'skype_chat', 8: 'skype_call', 9: 'link',
                          10: 'data', 11: 'whatsapp', 12: 'city', 13: 'equation', 14: 'numeric', 15: 'file', None: None}.get(self.type)
        self.belongs = utils.parse_int(k, 'belongs')
        self.belongs_name = {1: 'Deal', 2: 'Person', 3: 'Company', None: None}.get(self.belongs)
        self.values = utils.parse_str(k, 'values')  # FIXME não é srt, corrigir
        self.numeric_currency_id = utils.parse_int(k, 'currency_id')
        self.numeric_decimal_places = utils.parse_int(k, 'decimal_places')
        self.numeric_thousand_sep = utils.parse_int(k, 'thousand_sep')
        self.equation_formula = utils.parse_str(k, 'formula')
        self.equation_output_type = utils.parse_str(k, 'output_type')
        self.equation_decimal_places = utils.parse_int(k, 'decimal_places')
        self.equation_allow_negative = utils.parse_str(k, 'allow_negative')
        self.equation_currency_id = utils.parse_str(k, 'currency_id')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')

@dataclass
class EntityHasCustomField:
    id: int | None
    person_id: int | None
    company_id: int | None
    deal_id: int | None
    custom_field_id: int | None
    value: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.person_id = utils.parse_int(k, 'person_id')
        self.company_id = utils.parse_int(k, 'company_id')
        self.deal_id = utils.parse_int(k, 'deal_id')
        self.custom_field_id = utils.parse_int(k, 'custom_field_id')
        self.value = utils.parse_str(k, 'value')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
