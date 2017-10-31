from LOGIC import filme

def imprimir_filme(filme):
    titulo = filme[0]
    genero = filme[1]
    ano = filme[2]
    cod_filme = filme[3]
    print ("Titulo: ",  titulo[0])
    print ("Genero: ", genero[1])
    print ("Ano: ", ano[2])        
    print ("Codigo do filme: ", cod_filme[3])        
    print() 

def menu_adicionar():
    print ("\nAdicionar filme\n")
    titulo = str(input("Titulo: "))
    cod_filme = int(input("Codigo do filme: "))
    ano = int (input("Ano: "))
    genero = str(input("Genero: "))
    adicionou = filme.adicionar_filme(titulo,ano,genero,cod_filme)
    print ("Filme Adicionado")
    
def menu_listar():
    print ("\nListar filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

def menu_buscar():
    print ("\nBuscar filme \n")
    cod_filme = int(input("Código do filme: "))
    f = filme.buscar_consulta(cod_filme)
    if (f == None):
        print ("filme não encontrado")
    else:
        imprimir_filme(f)

def menu_remover():
    print ("\nRemover filmes \n")
    cod_filme = int(input("Codigo do filme: "))
    f = filme.remover_consulta(cod_filme)
    if (f == False):
        print ("filme não encontrada")
    else:
        print ("filme removido")
    
def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Listar filme \n" +
             "(2) Buscar filme por código \n" +
             "(3) Remover filme \n" +
             "(0) Voltar\n"+
            "----------------")
    while(run_filme):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_listar()
        elif(op == 2):       
            menu_buscar()
        elif (op == 3):
            menu_remover()
        elif (op == 0):
            run_filme = False