import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import ssl
import certifi
from urllib.request import urlopen
import io

# Paramètres de connexion.
username = "root"
password = "" 
host = "localhost"
port = 3306
database = "my_dbt_db"

# Création de l'engine SQLAlchemy
DATABASE_URI = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URI)

# Création de la base de données si elle n'existe pas.
if not database_exists(engine.url):
    create_database(engine.url)

# SSL context sécurisé pour GitHub
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Liste des tables à importer
liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

import ssl
from urllib.request import urlopen
import io

# Création d’un contexte SSL non vérifié (contournement)
ssl._create_default_https_context = ssl._create_unverified_context

# Boucle sur chaque table
for table in liste_tables:
    csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"
    print(f"Téléchargement de {csv_url}...")

    response = urlopen(csv_url)
    df = pd.read_csv(io.BytesIO(response.read()))

    # Envoi dans MySQL
    df.to_sql(f"raw_{table}", engine, if_exists="replace", index=False)
    print(f"✅ Table raw_{table} chargée.")