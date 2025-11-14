from db.connection import testar_conexao
from menus.menu import menu_principal

def main():
    if testar_conexao():
        menu_principal()
    else:
        print("Não foi possível conectar. Verifique o .env ou a conexão com o Banco de Dados e tente novamente.")

if __name__ == "__main__":
    main()