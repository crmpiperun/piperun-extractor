import re
import warnings
from datetime import datetime
from typing import Type, TypeVar, Any
from urllib.parse import urlparse

import pandas
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning

T = TypeVar('T')
warnings.filterwarnings('ignore', category=MarkupResemblesLocatorWarning)


def parse_list(raw: dict, key: str, cast: Type[T]) -> list[T]:
    return [cast(**value) for value in raw.get(key, [])]


def parse_obj(raw: dict, key: str, cast: Type[T]) -> T | None:
    value = raw.get(key, None)
    return cast(**value) if isinstance(value, dict) else None


def parse_int(raw: dict, key: str) -> int | None:
    value: str|None = raw.get(key, None)
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None


def parse_bool(raw: dict, key: str) -> bool | None:
    value = raw.get(key, None)
    try:
        return bool(value) if value is not None else None
    except ValueError:
        return None


def parse_float(raw: dict, key: str) -> float | None:
    value: str|None = raw.get(key, None)
    try:
        return float(value) if value is not None else None
    except ValueError:
        return None


def parse_str(raw: dict, key: str) -> str | None:
    value = raw.get(key, None)
    try:
        return str(value) if value is not None else None
    except ValueError:
        return None


def parse_html2text(raw: dict, key: str) -> str | None:
    value = raw.get(key, '')
    return BeautifulSoup(value, 'html.parser').get_text() if value else None


def parse_mail(raw: dict, key: str) -> str | None:
    value = raw.get(key, '')

    if not value or not isinstance(value, str):
        return None

    return value if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value) else None


def parse_url(raw: dict, key: str) -> str | None:
    value: str = raw.get(key, '')

    if not value or not isinstance(value, str):
        return None

    try:
        parsed = urlparse(value)

        if parsed.netloc and parsed.scheme in ['http', 'https']:
            return value
    except ValueError:
        pass

    return None


def parse_date(raw: dict, key: str) -> datetime | None:
    value = raw.get(key, '')

    if not value or not isinstance(value, str):
        return None

    date_formats = [
        '%Y-%m-%dT%H:%M:%S.%fZ',
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d/%m/%y',
    ]

    for date_format in date_formats:
        try:
            date = datetime.strptime(value, date_format)
            return date if pandas.Timestamp.min <= date <= pandas.Timestamp.max else None
        except ValueError:
            continue

    return None


def parse_origin(url: str) -> str | None:
    try:
        parsed = urlparse(url)
        if parsed.scheme and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc}"
    except ValueError:
        pass
    return None

def parse_string_array_fields(raw: dict[str, Any], key: str) -> list[Any]:
    value = raw.get(key)
    if isinstance(value, list):
        return value
    else:
        return []
