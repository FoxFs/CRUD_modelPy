import sqlite3

class banco(object):

    def __init__(self):
        self.conection = sqlite3.connect('Banco_Registro.db')

        self.CriarTable()

    def CriarTable(self):
        b = self.conection.cursor() #isso vai fazer ele fazer uma varredura e mexer no arquivo .db
    
        b.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                     idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                     nome TEXT,
                     senha TEXT)""")
        self.conection.commit()

        b.close()

    def SelectTable(self):
        b = self.conection.cursor() #isso vai fazer ele fazer uma varredura e mexer no arquivo .db
        
        b.execute("""SELECT * FROM usuarios""")
        resultados = b.fetchall()
        b.close()
        return resultados
    
    def deleteUser(self, idusuario):
        b = self.conection.cursor()
        b.execute("DELETE FROM usuarios WHERE idusuario = ?", (idusuario,))
        self.conection.commit()
        b.close()