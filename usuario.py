from Banco import banco

class Usuario(object):

    def __init__(self, idusuario=0, nome="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.senha = senha
    
    def inserirUsuario(self):
        armaze = banco()

        try:
            b = armaze.conection.cursor()

            print(f"Inserindo usuário: {self.nome}, senha: {self.senha}")
            b.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (self.nome, self.senha))
            armaze.conection.commit()
            b.close()

            return "Usuario Cadastrado com sucesso!!"
        
        
        except Exception as e:
            return f"Ocorreu um erro inesperado,tente novamente!: {e}"
        
        finally:
            armaze.conection.close()
