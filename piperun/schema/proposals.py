from dataclasses import dataclass
from datetime import datetime

from piperun import utils
from piperun.schema.items import Item, Characteristic


@dataclass
class Currency:
    id: int | None
    name: str | None
    origin_country: str | None
    symbol: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.origin_country = utils.parse_str(k, 'origin_country')
        self.symbol = utils.parse_str(k, 'symbol')


@dataclass
class ProposalItems:
    id: int | None
    description_html: str | None
    description_text: str | None
    quantity: int | None
    value: float | None
    discount_type: int | None
    discount_value: float | None
    duration: int | None
    ipi_tax: float | None
    order: int | None
    custom_field_id: int | None
    formula_text: str | None
    contract_start_at: datetime | None
    contract_end_at: datetime | None
    type_of_charge: int | None
    commission_value: float | None
    commission_type: int | None
    commission_incidence_type: int | None
    cost: float | None
    markup_value: float | None
    markup_type: int | None
    product_name: str | None
    delivery_forecast_date: datetime | None
    item: Item | None
    characteristics: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.quantity = utils.parse_int(k, 'quantity')
        self.value = utils.parse_float(k, 'value')
        self.discount_type = utils.parse_int(k, 'discount_type')
        self.discount_value = utils.parse_float(k, 'discount_value')
        self.duration = utils.parse_int(k, 'duration')
        self.ipi_tax = utils.parse_float(k, 'ipi_tax')
        self.order = utils.parse_int(k, 'order')
        self.custom_field_id = utils.parse_int(k, 'custom_field_id')  # CustomField.id
        self.formula_text = utils.parse_str(k, 'formula_text')
        self.contract_start_at = utils.parse_date(k, 'contract_start_at')
        self.contract_end_at = utils.parse_date(k, 'contract_end_at')
        self.type_of_charge = utils.parse_int(k, 'type_of_charge')
        self.commission_value = utils.parse_float(k, 'commission_value')
        self.commission_type = utils.parse_int(k, 'commission_type')
        self.commission_incidence_type = utils.parse_int(k, 'commission_incidence_type')
        self.cost = utils.parse_float(k, 'cost')
        self.markup_value = utils.parse_float(k, 'markup_value')
        self.markup_type = utils.parse_int(k, 'markup_type')
        self.product_name = utils.parse_str(k, 'product_name')
        self.delivery_forecast_date = utils.parse_date(k, 'delivery_forecast_date')
        self.item = utils.parse_obj(k, 'item', Item)
        self.characteristics = utils.parse_list(k, 'characteristics', Characteristic)


@dataclass
class PaymentMethod:
    id: int | None
    payment_method_type_id: int | None
    description_html: str | None
    description_text: str | None
    discount: str | None
    temp: str | None
    term: str | None
    interval: str | None
    parcels: str | None
    type: int | None
    down_payment: str | None
    config_active: int | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.payment_method_type_id = utils.parse_int(k, 'payment_method_type_id')  # PaymentMethodsType.id
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')
        self.discount = utils.parse_str(k, 'discount')
        self.temp = utils.parse_str(k, 'temp')
        self.term = utils.parse_str(k, 'term')
        self.interval = utils.parse_str(k, 'interval')
        self.parcels = utils.parse_str(k, 'parcels')
        self.type = utils.parse_int(k, 'type')
        self.down_payment = utils.parse_str(k, 'down_payment')
        self.config_active = utils.parse_int(k, 'config_active')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class ProposalModel:
    id: int | None
    name: str | None
    description_html: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class ProposalLayout:
    id: int | None
    name: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')


@dataclass
class PaymentMethodsType:
    id: int | None
    name: str | None
    description_html: str | None
    description_text: str | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.name = utils.parse_str(k, 'name')
        self.description_html = utils.parse_str(k, 'description')
        self.description_text = utils.parse_html2text(k, 'description')


@dataclass
class ProposalParcel:
    id: int | None
    parcel: int | None
    due_date: datetime | None
    discount: float | None
    value: float | None
    proposal_id: int | None
    payment_method_type_id: int | None
    commission_type: int | None
    remaining_value: float | None
    commission_paid: float | None
    paid_at: datetime | None
    payment_status: int | None
    paid_value: float | None
    commission_value: float | None
    commission_value_money: float | None
    commission_value_percent: float | None
    parcel_type: int | None
    created_at: datetime | None
    updated_at: datetime | None

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.parcel = utils.parse_int(k, 'parcel')
        self.due_date = utils.parse_date(k, 'due_date')
        self.discount = utils.parse_float(k, 'discount')
        self.value = utils.parse_float(k, 'value')
        self.proposal_id = utils.parse_int(k, 'proposal_id')  # Proposal.id
        self.payment_method_type_id = utils.parse_int(k, 'payment_method_type_id')  # PaymentMethodsType.id
        self.commission_type = utils.parse_int(k, 'commission_type')
        self.remaining_value = utils.parse_float(k, 'remaining_value')
        self.commission_paid = utils.parse_float(k, 'commission_paid')
        self.paid_at = utils.parse_date(k, 'paid_at')
        self.payment_status = utils.parse_int(k, 'payment_status')
        self.paid_value = utils.parse_float(k, 'paid_value')
        self.commission_value = utils.parse_float(k, 'commission_value')
        self.commission_value_money = utils.parse_float(k, 'commission_value_money')
        self.commission_value_percent = utils.parse_float(k, 'commission_value_percent')
        self.parcel_type = utils.parse_int(k, 'parcel_type')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')


@dataclass
class Proposal:
    id: int | None
    user_id: int | None
    deal_id: int | None
    proposal_model_id: int | None
    payment_method_id: int | None
    payment_method_mrr_id: int | None
    currency_id: int | None
    name: str | None
    discount_value: float | None
    value: float | None
    value_mrr: float | None
    status: int | None
    status_text: str | None
    introduction_html: str | None
    introduction_text: str | None
    deal_date: datetime | None
    expiration_date: datetime | None
    delivery_forecast_date: datetime | None
    discount_type: int | None
    payment_method: str | None
    observation_html: str | None
    observation_text: str | None
    visualized_in: datetime | None
    version: int | None
    shipping_type: int | None
    shipping_value: float | None
    first_payment_date: datetime | None
    first_payment_mrr_date: datetime | None
    first_parcel_interval: int | None
    number: int | None
    due_date: int | None
    due_date_mrr: int | None
    monthly_date: int | None
    invoice_date: datetime | None
    created_at: datetime | None
    updated_at: datetime | None
    closed_at: datetime | None
    brand_id: int | None
    shipping_company_id: int | None
    billing_company_id: int | None
    triangular_company_id: int | None
    purchase_order: str | None
    parcels: int | None
    parcels_mrr: int | None
    down_payment_percent: float | None
    interval: int | None
    payment_comment_html: str | None
    payment_comment_text: str | None
    payment_comment_mrr_html: str | None
    payment_comment_mrr_text: str | None
    commission_type: int | None
    commission_value: float | None
    proposal_layout_id: int | None
    proposal_number: str | None
    commission_type_mrr: int | None
    commission_value_mrr: float | None
    currency: Currency | None
    proposalModel: ProposalModel | None
    layout: ProposalLayout | None
    items: list

    def __init__(self, **k):
        self.id = utils.parse_int(k, 'id')
        self.user_id = utils.parse_int(k, 'user_id')  # User.id
        self.deal_id = utils.parse_int(k, 'deal_id')  # Deal.id
        self.proposal_model_id = utils.parse_int(k, 'proposal_model_id')  # proposal_model.id
        self.payment_method_id = utils.parse_int(k, 'payment_method_id')  # PaymentMethod.id
        self.payment_method_mrr_id = utils.parse_int(k, 'payment_method_mrr_id')  # PaymentMethod.id
        self.currency_id = utils.parse_int(k, 'currency_id')  # Currency.id
        self.name = utils.parse_str(k, 'name')
        self.discount_value = utils.parse_float(k, 'discount_value')
        self.value = utils.parse_float(k, 'value')
        self.value_mrr = utils.parse_float(k, 'value_mrr')
        self.status = utils.parse_int(k, 'status')
        self.status_text = {0: 'open', 1: 'approved', 2: 'declined', 3: 'canceled', 4: 'sent_to_sign', 5: 'signed', None: None}.get(self.status)
        self.introduction_html = utils.parse_str(k, 'introduction')
        self.introduction_text = utils.parse_html2text(k, 'introduction')
        self.deal_date = utils.parse_date(k, 'deal_date')
        self.expiration_date = utils.parse_date(k, 'expiration_date')
        self.delivery_forecast_date = utils.parse_date(k, 'delivery_forecast_date')
        self.discount_type = utils.parse_int(k, 'discount_type')
        self.payment_method = utils.parse_str(k, 'payment_method')
        self.observation_html = utils.parse_str(k, 'observation')
        self.observation_text = utils.parse_html2text(k, 'observation')
        self.visualized_in = utils.parse_date(k, 'visualized_in')
        self.version = utils.parse_int(k, 'version')
        self.shipping_type = utils.parse_int(k, 'shipping_type')
        self.shipping_value = utils.parse_float(k, 'shipping_value')
        self.first_payment_date = utils.parse_date(k, 'first_payment_date')
        self.first_payment_mrr_date = utils.parse_date(k, 'first_payment_mrr_date')
        self.first_parcel_interval = utils.parse_int(k, 'first_parcel_interval')
        self.number = utils.parse_int(k, 'number')
        self.due_date = utils.parse_int(k, 'due_date')
        self.due_date_mrr = utils.parse_int(k, 'due_date_mrr')
        self.monthly_date = utils.parse_int(k, 'monthly_date')
        self.invoice_date = utils.parse_date(k, 'invoice_date')
        self.created_at = utils.parse_date(k, 'created_at')
        self.updated_at = utils.parse_date(k, 'updated_at')
        self.closed_at = utils.parse_date(k, 'closed_at')
        self.brand_id = utils.parse_int(k, 'brand_id')  # Company.id
        self.shipping_company_id = utils.parse_int(k, 'shipping_company_id')  # Company.id
        self.billing_company_id = utils.parse_int(k, 'billing_company_id')  # Company.id
        self.triangular_company_id = utils.parse_int(k, 'triangular_company_id')  # Company.id
        self.purchase_order = utils.parse_str(k, 'purchase_order')
        self.parcels = utils.parse_int(k, 'parcels')
        self.parcels_mrr = utils.parse_int(k, 'parcels_mrr')
        self.down_payment_percent = utils.parse_float(k, 'down_payment_percent')
        self.interval = utils.parse_int(k, 'interval')
        self.payment_comment_html = utils.parse_str(k, 'payment_comment')
        self.payment_comment_text = utils.parse_html2text(k, 'payment_comment')
        self.payment_comment_mrr_html = utils.parse_str(k, 'payment_comment_mrr')
        self.payment_comment_mrr_text = utils.parse_html2text(k, 'payment_comment_mrr')
        self.commission_type = utils.parse_int(k, 'commission_type')
        self.commission_value = utils.parse_float(k, 'commission_value')
        self.proposal_layout_id = utils.parse_int(k, 'proposal_layout_id')
        self.proposal_number = utils.parse_str(k, 'proposal_number')
        self.commission_type_mrr = utils.parse_int(k, 'commission_type_mrr')
        self.commission_value_mrr = utils.parse_float(k, 'commission_value_mrr')
        self.currency = utils.parse_obj(k, 'currency', Currency)
        self.proposalModel = utils.parse_obj(k, 'proposalModel', ProposalModel)
        self.layout = utils.parse_obj(k, 'layout', ProposalLayout)
        self.items = utils.parse_list(k, 'items', ProposalItems)
