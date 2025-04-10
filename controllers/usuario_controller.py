from models.usuario import Usuario # type: ignore
from config import usuarios_collection

import re

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email)

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()

    if not validar_email(email):
        print("❌ E-mail inválido. Cadastro cancelado.\n")
        return

    try:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 120:
            raise ValueError
    except ValueError:
        print("❌ Idade inválida. Cadastro cancelado.\n")
        return

    usuario = Usuario(nome, email, idade)
    usuarios_collection.insert_one(usuario.to_dict())
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!\n")


    # Validação simples da idade
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("❌ Idade inválida. Cadastro cancelado.\n")
        return
    
    #Validação email

    

    # Cria e insere o usuário no banco
    usuario = Usuario(nome, email, idade)
    usuarios_collection.insert_one(usuario.to_dict())
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!\n")

def listar_usuarios():
    """
    Lista todos os usuários cadastrados no banco de dados.
    """
    print("\n--- Lista de Usuários ---")
    usuarios = list(usuarios_collection.find())

    if not usuarios:
        print("⚠️ Nenhum usuário encontrado.\n")
        return

    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {u['nome']}, E-mail: {u['email']}, Idade: {u['idade']}")
    print()

def buscar_usuario():
    """
    Busca usuários pelo nome no banco de dados.
    """
    print("\n--- Buscar Usuário ---")
    nome = input("Digite o nome do usuário: ").strip()

    usuarios = list(usuarios_collection.find({"nome": nome}))

    if not usuarios:
        print("🔍 Usuário não encontrado.\n")
    else:
        for u in usuarios:
            print(f"Nome: {u['nome']}, E-mail: {u['email']}, Idade: {u['idade']}")
    print()
