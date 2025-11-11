from functions.cadastro_login import cadastro, login
from functions.limpar import limpar_tela
import time

def menu_cadastro():
    print("╔══════════════════════════════════════╗")
    print("║        📝 Cadastro de Usuário        ║")
    print("╠══════════════════════════════════════╣")
    print("║ Por favor, insira os dados abaixo:   ║")
    print("╚══════════════════════════════════════╝")

def menu_login():
    print("╔══════════════════════════════════════╗")
    print("║            🔑 Fazer Login            ║")
    print("╠══════════════════════════════════════╣")
    email = input("Email: ")
    senha = input("Senha: ")
    return email, senha

def menu_logado():
    print("") # criar o sistema de cadastro, avaliaçao e visualizaçao dos pontos turisticos, e poder ver as proprias avaliacoes e de outrem

def menu_principal():
    while True:
        limpar_tela()
        print("╔═══════════════════════════════════════╗")
        print("║   🌴 Sistema de Usuários - Alagoas    ║")
        print("╠═══════════════════════════════════════╣")
        print("║ 1. 📝 Cadastrar novo usuário          ║")
        print("║ 2. 🔑 Fazer login                     ║")
        print("║ 3. ❌ Sair                            ║")
        print("╚═══════════════════════════════════════╝")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️  Opção inválida! Por favor, insira um número.")
            time.sleep(1.5)
            continue  # volta p o menu

        if opcao == 1:
            limpar_tela()
            menu_cadastro()
            cadastro()
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == 2:
            limpar_tela()
            email, senha = menu_login()
            sucesso = login(email, senha)
            if sucesso:
                print("\n✅ Login realizado com sucesso!")
                menu_logado()
            else:
                print("\n❌ Falha no login. Verifique seus dados.")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == 3:
            print("\n👋 Saindo do sistema...")
            time.sleep(1)
            break

        else:
            print("⚠️  Opção inválida! Tente novamente.")
            time.sleep(1.5)