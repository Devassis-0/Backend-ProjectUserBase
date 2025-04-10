import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.usuario import Usuario

def test_to_dict():
    usuario = Usuario("João", "joao@email.com", 30)
    esperado = {
        "nome": "João",
        "email": "joao@email.com",
        "idade": 30
    }
    assert usuario.to_dict() == esperado
