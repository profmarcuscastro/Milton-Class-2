from distutils.util import execute
import sqlite3# biblioteca que traz ferramentas de sql 

# 2 itens basico para fazer conexao
# - 1 - connect 
# - 2 - cursor

conexao = sqlite3.connect('basededados1.db')#criar uma base
cursor = conexao.cursor()#quem vai realizar suas interacaos com a base

#CRIANDO TABELAaa

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')'
)

# formas de inserir de dados

# Primeira

cursor.execute('INSERT INTO clientes (nome,peso) VALUES ("LUIZ",80.5)')

#SEGUNDO

cursor.execute(
    'INSERT INTO clientes (nome,peso) VALUES (:nome,:peso)',
    {
        'nome':'Milton',
        'peso':75.0
    }

)

#Terceira forma

cursor.execute(
    'INSERT INTO clientes VALUES (:id,:nome,:peso)',
    {
        'id':None,
        'nome':'Marcus',
        'peso':63.0
    }
)

conexao.commit()

cursor.execute('SELECT * FROM clientes')#seleciona tudo
#cursor.execute('SELECT nome,peso FROM clientes WHERE peso>:peso',
#{'peso':70

#})

for linha in cursor.fetchall():#tranforma em uma lista todas as linhas do sql
    print(linha)

#update de dados

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',{
'nome':'Joao',
'id':2
})

cursor.execute('DELETE FROM clientes WHERE id=:id',
    {'id':6}
)

conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():#tranforma em uma lista todas as linhas do sql
    print(linha)

cursor.close()
conexao.close()