from dataclasses import dataclass

from piperun import utils


@dataclass
class City:
    id: int | None
    name: str | None
    uf: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.uf = utils.parse_str(k, 'uf')
