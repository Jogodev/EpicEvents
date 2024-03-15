"""Check for inputs"""

import re
import bcrypt
from src.utils.utils import regex_mail, regex_mdp, regex_phone


def check_email(email):
    return bool(re.fullmatch(regex_mail, email))


def check_password(password):
    return bool(re.fullmatch(regex_mdp, password))


def check_phone(phone):
    return bool(re.fullmatch(regex_phone, phone))


# Hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_hash_password(password, hashed_password):
    hashed_password = hash_password(password)
    return bool(bcrypt.checkpw(password.encode(), hashed_password))
