from LOGIC import usuario
from GUI import menu_usuario
from LOGIC import filme
from GUI import menu_filme

def inicializar_dados():
    usuario.iniciar_usuarios()
    filme.iniciar_filmes()

def mostrar_menu():
    run_menu = True
    inicializar_dados()
    menu = ("\n----------------\n" +
            "(1) Menu Usuario \n" +
            "(2) Menu Filmes \n" +
            "(0) Sair\n" +
            "----------------")
    while (run_menu):
        print(menu)
        op = int(input("Digite sua escolha: "))
        if (op == 1):
            menu_usuario.mostrar_menu()
        elif (op == 2):
            menu_filme.mostrar_menu()
        elif (op == 0):
            print("Saindo do programa...")
            run_menu = False
        else:
            print("Valor invalido")