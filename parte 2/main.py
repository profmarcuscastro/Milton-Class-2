import sqlite3

#Vamos usar a base de agenda telefonica 

class AgendaDB:
    def __init__(self,arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
#CRUD = CREATE ,  RESQUEST, UPDATE, DELETE
    def inserir(self,nome,telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta,(nome,telefone))
        self.conn.commit()

    def editar(self,nome,telefone,id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta,(nome,telefone,id))
        self.conn.commit()

    def excluir(self,id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta,(id,))
        self.conn.commit()
        print(f"O id:{id} foi excluido com sucesso!")

   # def buscar(self,valor):
    #    pass

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()




ag1 = AgendaDB('Aula Python.db')

ag1.inserir('Marcus','36520147')
ag1.inserir('Marcelo','7152450147')
ag1.inserir('Milton','255547147')
ag1.inserir('Ana','9652440147')

ag1.listar()