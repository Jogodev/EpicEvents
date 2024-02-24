from rich import print
from sqlalchemy import create_engine, URL
from decouple import config


USERNAME=config("DB_USER")
PASSWORD=config("DB_PASSWORD")
HOST=config("HOST")
PORT=config("PORT")
DATABASE=config("DATABASE")


db_url = URL.create(
    "postgresql+psycopg2",
    username=f"{USERNAME}",
    password=f"{PASSWORD}",
    host=f"{HOST}",
    database=f"{DATABASE}",
)

engine = create_engine(db_url, echo=True)

try:
    conn = engine.connect()
    print('Base connecté')
except Exception as error:
    print(error)
    print('La connexion à la base à échoué')  


