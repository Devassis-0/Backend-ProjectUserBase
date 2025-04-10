class Usuario:
    """
    Representa um usuário com nome, e-mail e idade.
    """

    def __init__(self, nome: str, email: str, idade: int):
        self.nome = nome
        self.email = email
        self.idade = idade

    def to_dict(self) -> dict:
        """
        Converte o objeto Usuario para um dicionário.
        Útil para inserção no banco de dados.
        """
        return {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade
        }
