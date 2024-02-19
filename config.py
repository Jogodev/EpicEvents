import psycopg2
from decouple import config

connexion = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('HOST'),
            port=config('PORT'),
            database=config('DATABASE'),
)



connexion.commit()

connexion.close()