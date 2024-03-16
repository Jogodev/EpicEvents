"""Common checks"""

import re
from src.utils.utils import regex_mail, regex_mdp
from rich import print


def check_email(email):
    return bool(re.fullmatch(regex_mail, email))
