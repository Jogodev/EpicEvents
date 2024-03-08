"""Check for inputs"""

import re
from src.utils.utils import regex_mail, regex_mdp, regex_phone



def check_email(email):
    return bool(re.fullmatch(regex_mail, email))

def check_password(password):
    return bool(re.fullmatch(regex_mdp, password))

def check_phone(phone):
    return bool(re.fullmatch(regex_phone, phone))


