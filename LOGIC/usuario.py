usuarios = []

def adicionar_usuario(cpf, nome, email, senha):    
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            return u
    return None

def remover_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            usuarios.remove(u)
            return True
    return False
	
def iniciar_usuarios():
    adicionar_usuario(22222222222, "Charles", charles@charles.com, 998807766)
    adicionar_usuario(11111111111, "Joao", joao@joao.com, 98765432112)