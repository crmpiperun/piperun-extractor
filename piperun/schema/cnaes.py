from dataclasses import dataclass

from piperun import utils


@dataclass
class Cnae:
    id: int | None
    code: str | None
    description: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.code = utils.parse_str(k, 'code')
        self.description = utils.parse_str(k, 'description')
