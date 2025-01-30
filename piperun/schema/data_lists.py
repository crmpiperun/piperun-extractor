from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class DataListFieldTypeType:
    id: int | None
    name: str | None
    table: str | None
    column: str | None
    column_join: str | None
    column_join_field: str | None
    native_table: str | None
    native_column_join: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.table = utils.parse_str(k, 'table')
        self.column = utils.parse_str(k, 'column')
        self.column_join = utils.parse_str(k, 'column_join')
        self.column_join_field = utils.parse_str(k, 'column_join_field')
        self.native_table = utils.parse_str(k, 'native_table')
        self.native_column_join = utils.parse_str(k, 'native_column_join')


@dataclass
class DataListFieldTypeOption:
    id: int | None
    name: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')


@dataclass
class DataListField:
    id: int | None
    datalist_id: int | None
    datalist_field_type_id: int | None
    name: str | None
    key: str | None
    order: int | None
    type: DataListFieldTypeType | None
    options: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.datalist_id = utils.parse_int(k, 'datalist_id')  # DataList.id
        self.datalist_field_type_id = utils.parse_int(k, 'datalist_field_type_id')  # DataListFieldTypeType.id
        self.name = utils.parse_str(k, 'name')
        self.key = utils.parse_str(k, 'key')
        self.order = utils.parse_int(k, 'order')
        self.type = utils.parse_obj(k, 'type', DataListFieldTypeType)
        self.options = utils.parse_list(k, 'options', DataListFieldTypeOption)


@dataclass
class DataList:
    id: int | None
    name: str | None
    entity: str | None
    created_at: datetime | None
    updated_at: datetime | None
    type: DataListFieldTypeType | None
    fields: list
    options: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.entity = utils.parse_str(k, 'entity')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.type = utils.parse_obj(k, 'type', DataListFieldTypeType)
        self.fields = utils.parse_list(k, 'fields', DataListField)
        self.options = utils.parse_list(k, 'options', DataListFieldTypeOption)
