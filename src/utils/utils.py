"""Utils"""

from sqlalchemy.orm import declarative_base, sessionmaker
import os, sys


# DB
Base = declarative_base()


# Check

regex_mail = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
regex_mdp = r"^(?=.*?[a-z])(?=.*?[0-9]).{6,}$"
regex_phone = r"(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}"


# clear
def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")
