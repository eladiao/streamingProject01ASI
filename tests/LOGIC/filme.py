filmes = []

def adicionar_filme(titulo,genero,ano):    
    filme = [titulo,genero,ano]
    filmes.append(filme)
    
def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return f
    return None

def buscar_filme_por_genero(genero):
    for f in filmes:
        if (f[0] == genero):
            return f
    return None

def remover_filmes(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            filmes.remove(f)
            return True
    return False
    
def iniciar_filmes():
    adicionar_filme("Charles", "Aventura", 2017)
    adicionar_filme("Joao", "Horror", 1997)