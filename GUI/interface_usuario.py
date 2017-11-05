from LOGIC import usuario
from GUI import menu_usuario
from LOGIC import filme
from GUI import menu_filme
from LOGIC import serie
from GUI import menu_serie
from LOGIC import anime
from GUI import menu_anime

def inicializar_dados():
    usuario.iniciar_usuarios()
    filme.iniciar_filmes()

def mostrar_menu():
    run_menu = True
    inicializar_dados()
    menu = ("\n----------------\n" +
            "(1) Menu Usuario \n" +
            "(2) Menu Filmes \n" +
            "(3) Menu Series \n" +
            "(4) Menu Animes \n" +
            "(0) Sair\n" +
            "----------------")
    while (run_menu):
        print(menu)
        op = int(input("Digite sua escolha: "))
        if (op == 1):
            menu_usuario.mostrar_menu()
        elif (op == 2):
            menu_filme.mostrar_menu()
        elif (op == 3):
            menu_serie.mostrar_menu()
        elif (op == 4):
            menu_anime.mostrar_menu()
        elif (op == 0):
            print("Saindo do programa...")
            run_menu = False
        else:
            print("Valor invalido")
