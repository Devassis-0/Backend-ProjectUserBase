# app.py

# Importando as funções do controller de usuários
from controllers.usuario_controller import ( # type: ignore
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario
)

def exibir_menu():
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.
    """
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Buscar Usuário")
    print("4. Sair")
    return input("Escolha uma opção: ")

def executar_opcao(opcao):
    """
    Executa a ação correspondente à opção escolhida.
    """
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        listar_usuarios()
    elif opcao == '3':
        buscar_usuario()
    elif opcao == '4':
        print("Encerrando o sistema. Até logo!")
        return False
    else:
        print("Opção inválida! Tente novamente.\n")
    return True

def menu():
    """
    Loop principal do sistema.
    """
    continuar = True
    while continuar:
        opcao = exibir_menu()
        continuar = executar_opcao(opcao)

# Este bloco garante que o menu só será executado se este arquivo for o principal
if __name__ == "__main__":
    menu()
