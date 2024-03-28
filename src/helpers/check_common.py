"""Common checks"""

from config import db

import re
from src.utils.utils import regex_mail, regex_phone
from rich import print


def check_email(email):
    return bool(re.fullmatch(regex_mail, email))


def check_phone(phone):
    return bool(re.fullmatch(regex_phone, phone))


def is_email_exist(email, entity):
    return bool(db.query(entity).filter_by(email=email).first())


def check_date():
    return bool()
