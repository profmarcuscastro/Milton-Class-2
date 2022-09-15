# Parte 4 - Funções

## Oq é uma Funcão?

Primeiramente, vamos entender oq são as funções na matematica para que possamos entender melhor na computação.

Obs: Já usamos muitas funções durante o curso.

EX:

```python
def hello():
    print("hello word\n")

hello()
hello()
hello()
```

Mas porque as funções são MUITO uteis no seu programa?

## Usando parametros

EX:

```python
#TUDO QUE ESTA DENTRO DOS PARENTESES SAO VARIAVEIS 
#TBM CHAMADOS DE ARGUMENTO
def funcao(msg):
    print(msg)

funcao(msg)
funcao(msg)
funcao(msg)
funcao()
#voce consegue prever oq vai acontecer e como corrigir?

```

Ex:

```python
def funcao(msg='ola',nome='Marcus'):
    nome=nome.replace("u","o")
    print(msg, nome)
    return f'{msg} {nome}'
    #qual a diferenca? se atribuir a val oq da?

funcao(msg)
funcao(msg)
funcao(msg)
funcao()

```

ex3:Coisas loucas

```python
def funcao(msg):
    print(msg)

def dumb():
    return f

val=dumb()

```

### Exercicios de fixação

- P1 - Saudação
- P2 - Soma de valores
- P3
  - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
- P4
  - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.

## Funçoes (def) em python

### *Args e **kwargs

Primeiramente vamos nos lembrar do desempacotamento de de listas

```python
lista =[1,2,3,4,5]
n1,n2,*n=lista
print(n1,n2,n)
print(*lista,sep='-')

#Agor vamos fazer semelhante com a lista
#quando não sabemos o numeros de variaveis na funcao

def func(*args):#serve para quando nao sabemos
    a quantidade de variaveis
    #args =  list(args) # transformando em lista

    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)

```

Expandindo mais conceitos

```python

def func(*args):
    print(args)

lista = [0,1,2,3,4,5]
lista2= [10,20,30,40,50]

func(*lista,*lista2)


````

### Sobre os Kwargs

```Python

def func(*args,**kwargs):
    print(args)
    print(kwargs)
    #print (kwargs['nome'])

    nome = kwargs.get('nome')
    print(nome)

lista = [0,1,2,3,4,5]
lista2= [10,20,30,40,50]

func(*lista,*lista2,nome = 'Marcus',sobrenome = 'castro')


````

Problemas:

- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.

```python
def fun1(func):
    return func+5

def fun2(x):
    x = x +10
    return x

num = int(input())

fun2(num)


print(fun1(fun2(num)))
```

### Variaveis Globais na Função

O que ira acontecer nesse codigo?

```python
var = 'valor'
#declarado globalmente
def fun1():
    print(var)

def fun2():
    #global var #isso n é recomendado
    var='outro valor'
    print(var)

fun1()
fun2()
print(var)
```

- Problema:
  - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 executar duas funções que recebam um número diferente de argumentos

```python
#Registre sua solução
def mestre(funcao,*args,**kwargs):
    return funcao(*args,**kwargs) #fun1(2,3) = 2+3

def fun1(x,y):
    return x+y

v = mestre(fun1,2,3)

print (v)

```

## Funções anônimas - Expressões Lambda

```python
def func(arg1,arg2):

    return arg1*arg2

a = lambda x,y : x*y

print(func(2,2))

print(a(2,2))
```

aplicação:

```python
produtos =[
    ['P1',8],
    ['P2',40],
    ['P3',32],
    ['P4',50],
    ['P5',33]
    
]

produtos.sort()
print(produtos)

#qual é o metodo de ordenação?

def ordem(item):
    return item[1]

produtos.sort(key=ordem)
print(produtos)

# Solucao alternativa

produtos.sort(key=lambda x: x[1], reverse=True)
print(produtos)

#ordenar sem mudar a lista original

#print(produtos)
#print(sorted(produtos,key = lambda i:i[1],reverse=True))
#print(produtos)
```

### Tuplas

Geralmente usamos tao estrutura quando não queremos editar os elementos da mesma.

Quando queremos atualizar elementos em tuplas devemos usar listas

Vamos ver algumas formas de implementar tuplas

```python
t1=(1,2,3,'Marcus')
print(t1[2:])

t2 = 2,
print(type(t2))

#tbm pode ser desempacotado e usar multiplicador 
#podem ser convertidas em lista e viseversa
```

## Recursao fibonacci

``` python
def fib(n):
    if n ==1 or n ==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(100))
    
```

## Dicionários

```python

#craiando um dicionario

d1 = {
    'chave1':"001"
}

#vou add uma nova chave ao dicionario

d1['chave2']='outro valor'
#Lembre de fazer analogia com os Kwargs

print(f'valor de d1: {d1}')
print()
#Há tambem uma forma alternativa de fazer a criacao
#Usa o construtor dict

d2 =  dict(chave1 = 'valor')

print(f'valor de d2: {d2}')
#  Obs:Chaves possuem valores unicos
print()
d3 = { 'valor': 2,'valor':3,'valor': 4}
print(f'valor de D3 {d3}')

#Tambem é possivel ulitizar varias formatos 
#de chaves

d4={
    'str':'valor',
    123:'outro valor',
    (1,2,3): 'Tupla'
}

print(f'\n valor do dic na tupla {d4[(1,2,3)]}\n')

#Tambem podemos usar o comando get

print(d4.get(123))

# Vamos analisar o codigo a seguir
# Qual é a diferenca entre os dois codigos?
for k in d1:
    print(k)

for i in d1.values():
    print(i)

for j in d1.items():
    print(j)

for j,v in d1.items():
    print(j, v)
```

### Aprofundando o conhecimento de Dicionário

```python

# Agora, alem de aprodundar o conceito de dicionario
#vamos entender um pouco mais afundo sobre 
#igualdade no python

#EXEMPLO:

d1 = { 1:'a',2:'b',3:'c'
}

v= d1

print(d1)
print(v)

#Agora vamos modificar um valor em d1

d1[1]='r'

print(d1)
print(v)

#oq aconteceu na saida do codigo?

x= d1.copy()

x[2]='mudei'

print(f'\n dicionario x: {x}')
print(f'\n dicionairo {d1}')
print()

#porem ele não consegue realmente copiar tudo
#como por exemplo se quiser acessar a chave dentro
# de um dicionario dentro de outro

#Para que realmente seja feita uma copia é
#preciso usar o import copy
#essa biblioteca fara uma copia por meio de comando
# y = copy.deepcopy(d1)

#Tambem é possivel construir dicionarios apartir
#de listas usando o dict() assim como list()

## usar comando pop(), popitem()

print(f'A LISTA D1 esta no seguinte formato{d1}\n')
d1.pop(2)

print(f'D1 depois do pop(2){d1}\n')

d1.popitem()
print(f' d1 depois do popitem(): {d1}\n')
```
