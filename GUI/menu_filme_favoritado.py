from LOGIC import filme_favoritado

def imprimir_filme_favoritado(filme_favoritado):
    titulo = filme_favoritado[0]
    genero = filme_favoritado[1]
    ano = filme_favoritado[2]
    cod_filme = filme_favoritado[3]
    print ("Titulo: ",  titulo[0])
    print ("Genero: ", genero[1])
    print ("Ano: ", ano[2])        
    print ("Codigo do filme: ", cod_filme[3])        
    print() 

def menu_adicionar():
    print ("\nAdicionar filme favoritado\n")
    titulo = str(input("Titulo: "))
    cod_filme = int(input("Codigo do filme: "))
    ano = int (input("Ano: "))
    genero = str(input("Genero: "))
    adicionou = filme_favoritado.adicionar_filme(titulo,ano,genero,cod_filme)
    print ("Filme Favoritado Adicionado")
    
def menu_listar():
    print ("\nListar filmes favoritados\n")
    listar_filmes_favoritados = filme_favoritado.listar_filmes_favoritados()
    for ff in listar_filmes_favoritados:
        imprimir_filme_favoritado(ff)

def menu_buscar():
    print ("\nBuscar filme favoritado\n")
    cod_filme = int(input("Código do filme favoritado: "))
    ff = filme_favoritado.buscar_consulta(cod_filme)
    if (ff == None):
        print ("Filme favoritado não encontrado")
    else:
        imprimir_filme_favoritado(ff)

def menu_remover():
    print ("\nRemover filmes \n")
    cod_filme = int(input("Codigo do filme: "))
    ff = filme_favoritado.remover_consulta(cod_filme)
    if (ff == False):
        print ("Filme favoritado não encontrada")
    else:
        print ("Filme favoritado removido")
    
def mostrar_menu():
    run_filme_favoritado = True
    menu = ("\n----------------\n"+
             "(1) Listar filme favoritado \n" +
             "(2) Buscar filme favoritado por código \n" +
             "(3) Remover filme favoritado \n" +
             "(0) Voltar\n"+
            "----------------")
    while(run_filme_favoritado):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_listar()
        elif(op == 2):       
            menu_buscar()
        elif (op == 3):
            menu_remover()
        elif (op == 0):
            run_filme_favoritado = False