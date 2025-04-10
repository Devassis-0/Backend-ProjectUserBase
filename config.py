# config.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

# Obtém a URL do MongoDB de forma segura
MONGO_URI = os.getenv("MONGO_URI")

# Inicializa o cliente e define banco e coleção
client = MongoClient(MONGO_URI)
db = client["meu_banco"]
usuarios_collection = db["usuarios"]
