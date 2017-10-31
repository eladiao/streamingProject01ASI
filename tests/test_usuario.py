import unittest
from LOGIC import usuario

class TestUsuario (unittest.TestCase):
    
    def setUp(self):
        usuario.remover_todos_usuarios()
        
    def test_sem_usuarios(self):
        usuarios = usuario.listar_usuarios()
        self.assertEqual(0, len(usuarios))
        
    def test_adicionar_um_usuario(self):
        usuario.adicionar_usuario(2222, "Charles", "charles@charles.com", "998877665")

        usuarios = usuario.listar_usuarios()
        self.assertEqual(1, len(usuarios))

        u = usuarios[0]
        
        self.assertEqual(2222, u[0])        
        self.assertEqual("Charles", u[1])
        self.assertEqual("RUA 998877665", u[2])
        self.assertEqual("RUA 998877665", u[3])

    def test_adicionar_dois_usuario(self):
        usuario.adicionar_usuario(2222, "Charles", "charles@charles.com", "998877665")
        usuario.adicionar_usuario(1111, "Joao", "joao@joao.com", "98765432112")
        usuarios = usuario.listar_usuarios()
        self.assertEqual(2, len(usuarios))

    def test_buscar_usuario(self):
        usuario.adicionar_usuario(2222, "Charles", "charles@charles.com", "998877665")
        usuario.adicionar_usuario(1111, "Joao", "joao@joao.com", "98765432112")

        u = usuario.buscar_usuario(1111)
        self.assertEqual(1111, u[0])
        self.assertEqual("Maria", u[1])
        
    def test_remover_usuario(self):
        usuario.adicionar_usuario(2222, "Charles", "charles@charles.com", "998877665")
        usuario.adicionar_usuario(1111, "Joao", "joao@joao.com", "98765432112")
        
        usuario.remover_usuario(1111)
        
        u = usuario.buscar_usuario(1111)        
        self.assertIsNone(u)
        
    def test_iniciar_usuarios(self):
        usuario.iniciar_usuarios()
        usuarios = usuario.listar_usuarios()
        self.assertEqual(2, len(usuarios))
            
if __name__ == '__main__':
    unittest.main(exit=False)