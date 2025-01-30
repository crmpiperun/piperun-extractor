from dataclasses import dataclass

from piperun import utils


@dataclass
class Pipeline:
    id: int | None
    funnel_type: int | None
    funnel_type_name: str | None
    distribution_type: int | None
    user_id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None
    order: int | None
    is_main: bool | None
    limit_time: int | None
    visibility: int | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.funnel_type = utils.parse_int(k, 'funnel_type')
        self.funnel_type_name = utils.parse_str(k, 'funnel_type_name')
        self.distribution_type = utils.parse_int(k, 'distribution_type')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.order = utils.parse_int(k, 'order')
        self.is_main = utils.parse_bool(k, 'is_main')
        self.limit_time = utils.parse_int(k, 'limit_time')
        self.visibility = utils.parse_int(k, 'visibility')


@dataclass
class Stage:
    id: int | None
    pipeline_id: int | None
    origin_id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None
    order: int | None
    color: str | None
    completion_percentage: float | None
    block_emails: int | None
    days_limit: int | None
    update_limit: int | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.pipeline_id = utils.parse_int(k, 'pipeline_id')  # Pipeline.id
        self.origin_id = utils.parse_int(k, 'origin_id')  # Origin.id
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.order = utils.parse_int(k, 'order')
        self.color = utils.parse_str(k, 'color')
        self.completion_percentage = utils.parse_float(k, 'completion_percentage')
        self.block_emails = utils.parse_int(k, 'block_emails')
        self.days_limit = utils.parse_int(k, 'days_limit')
        self.update_limit = utils.parse_int(k, 'update_limit')
