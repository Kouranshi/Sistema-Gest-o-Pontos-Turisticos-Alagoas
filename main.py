from db.connection import testar_conexao
from menus.menu import menu_principal

def main():
    testar_conexao()
    menu_principal()

if __name__ == "__main__":
    main()