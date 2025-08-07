from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class CustomForm:
    id: int | None
    name: str | None
    type: int | None
    type_name: str | None
    is_active: bool | None
    page_title: str | None
    fields: list
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.type = utils.parse_int(k, 'type')
        self.type_name = {1: 'Deal', 2: 'Person', 3: 'Company', None: None}.get(self.type)
        self.is_active = utils.parse_bool(k, 'status')
        self.page_title = utils.parse_str(k, 'page_title')
        self.fields = utils.parse_list(k, 'fields', CustomFormField)
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class CustomFormField:
    id: int | None
    custom_form_id: int | None
    custom_field_id: int | None
    native_field_name: str | None
    native_field_type: int | None
    native_field_entity: int | None
    name: str | None
    value: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.custom_form_id = utils.parse_int(k, 'custom_form_id')  # CustomForm.id
        self.custom_field_id = utils.parse_int(k, 'custom_field_id')  # CustomField.id
        self.native_field_name = utils.parse_str(k, 'native_field_name')
        self.native_field_type = utils.parse_int(k, 'native_field_type')  # FIXME Criar dict com tipos
        self.native_field_entity = utils.parse_int(k, 'native_field_entity')  # FIXME Criar dict as entidades
        self.name = utils.parse_str(k, 'name')  # Only exists when is a response
        self.value = utils.parse_str(k, 'value')  # Only exists when is a response
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
