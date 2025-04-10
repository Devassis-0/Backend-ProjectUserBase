from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, conint
from dotenv import load_dotenv
from pymongo import MongoClient
from typing import List
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["meu_banco"]
usuarios_collection = db["usuarios"]

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    idade: conint(ge=0, le=120)

@app.get("/")
def root():
    return {"mensagem": "API funcionando"}

@app.post("/usuarios/")
def cadastrar_usuario(usuario: Usuario):
    if usuarios_collection.find_one({"email": usuario.email}) or usuarios_collection.find_one({"nome": usuario.nome}):
        raise HTTPException(status_code=400, detail="Usuário já cadastrado com este e-mail ou nome.")
    usuarios_collection.insert_one(usuario.dict())
    return {"mensagem": f"Usuário '{usuario.nome}' cadastrado com sucesso!"}

@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    usuarios = list(usuarios_collection.find({}, {"_id": 0}))
    return usuarios

@app.get("/usuarios/{nome}", response_model=List[Usuario])
def buscar_usuario(nome: str):
    usuarios = list(usuarios_collection.find({"nome": nome}, {"_id": 0}))
    if not usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return usuarios
