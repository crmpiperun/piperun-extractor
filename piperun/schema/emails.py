from dataclasses import dataclass
from datetime import datetime

from piperun import utils


@dataclass
class Email:
    id: int | None
    user_id: int | None
    email_id: int | None
    deal_id: int | None
    company_id: int | None
    person_id: int | None
    email_template_id: int | None
    sender: str | None
    sender_name: str | None
    to: str | None
    to_name: str | None
    reply_to: str | None
    cc: str | None
    cco: str | None
    subject: str | None
    sent_at: datetime | None
    status: int | None
    type: int | None
    is_important: bool | None
    is_trash: bool | None
    attachments_count: int | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.email_id = utils.parse_int(k, 'email_id')  # Email.id if a response of another email
        self.deal_id = utils.parse_int(k, 'deal_id')  # Deal.id
        self.company_id = utils.parse_int(k, 'company_id')  # Company.id
        self.person_id = utils.parse_int(k, 'person_id')  # Person.id
        self.email_template_id = utils.parse_int(k, 'email_template_id')  # EmailTemplate.id
        self.sender = utils.parse_str(k, 'sender')
        self.sender_name = utils.parse_str(k, 'sender_name')
        self.to = utils.parse_str(k, 'to')
        self.to_name = utils.parse_str(k, 'to_name')
        self.reply_to = utils.parse_str(k, 'reply_to')
        self.cc = utils.parse_str(k, 'cc')
        self.cco = utils.parse_str(k, 'cco')
        self.subject = utils.parse_str(k, 'subject')
        self.sent_at = utils.parse_date(k, 'sent_at')
        self.status = utils.parse_int(k, 'status')
        self.type = utils.parse_int(k, 'type')
        self.is_important = utils.parse_bool(k, 'important')
        self.is_trash = utils.parse_bool(k, 'trash')
        self.attachments_count = utils.parse_int(k, 'attachments_count')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class EmailTemplate:
    id: int | None
    owner_id: int | None
    name: str | None
    is_active: bool | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.owner_id = utils.parse_int(k, 'user_id')  # User.id
        self.name = utils.parse_str(k, 'name')
        self.is_active = utils.parse_bool(k, 'active')
