from rich import print
from sqlalchemy import create_engine, URL
from decouple import config
from src.utils.utils import Base, sessionmaker
from src.models import collaborater, customer, contract, event

USERNAME=config("DB_USER")
PASSWORD=config("DB_PASSWORD")
HOST=config("HOST")
PORT=config("PORT")
DATABASE=config("DATABASE")

def db_init():

    db_url = URL.create(
        "postgresql+psycopg2",
        username=f"{USERNAME}",
        password=f"{PASSWORD}",
        host=f"{HOST}",
        port=f"{PORT}",
        database=f"{DATABASE}",
    )

    engine = create_engine(db_url, echo=True)


    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        print('[bold green]Base connecté[/bold green]')
    except Exception as error:
        print(error)
        print('[bold red]La connexion à la base à échoué[/bold red]')  

# db_init()


db_url = URL.create(
    "postgresql+psycopg2",
    username=f"{USERNAME}",
    password=f"{PASSWORD}",
    host=f"{HOST}",
    port=f"{PORT}",
    database=f"{DATABASE}",
)

engine = create_engine(db_url, echo=True)

Session = sessionmaker(engine)
db = Session()

cursor = db_url
