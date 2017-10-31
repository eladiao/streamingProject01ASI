filmes_favoritados = []

def adicionar_filme_favoritado(titulo,genero,ano):    
    filme_favoritado = [titulo,genero,ano]
    filmes_favoritados.append(filme_favoritado)
    
def listar_filmes_favoritados():
    return filmes_favoritados

def buscar_filme_favoritado(cod_filme):
    for ff in filmes_favoritados:
        if (ff[0] == cod_filme):
            return ff
    return None

def remover_filmes_favoritados(cod_filme):
    for ff in filmes_favoritados:
        if (ff[0] == cod_filme):
            filmes_favoritados.remove(ff)
            return True
    return False
    
def iniciar_filmes_favoritados():
    adicionar_filme_favoritado("Charles", "Aventura", 2017)