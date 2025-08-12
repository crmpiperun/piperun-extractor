from dataclasses import dataclass
from datetime import datetime

from piperun import utils
from piperun.schema.cities import City


@dataclass
class Region:
    id: int | None
    region_id: int | None
    city_id: int | None
    name: str | None
    cep_to: str | None
    cep_from: str | None
    balance: int | None
    created_at: datetime | None
    cities: list
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.region_id = utils.parse_int(k, 'region_id')  # Region.id if microregion
        self.city_id = utils.parse_int(k, 'city_id')  # City.id if not has cep
        self.name = utils.parse_str(k, 'name')
        self.cep_to = utils.parse_str(k, 'cep_to')
        self.cep_from = utils.parse_str(k, 'cep_from')
        self.balance = utils.parse_int(k, 'balance')
        self.created_at = utils.parse_date(k, 'created_at')
        self.cities = utils.parse_list(k, 'cities', City)
        self.updated_at = utils.parse_date(k, 'updated_at')
