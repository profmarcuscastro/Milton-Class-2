# Parte 1  - Função

## Conceitos Basicos

     - Funcao matematica: y=f(x) cconeito de retorno a algum lugar

```python 

def div(x,y):
    x=x/y
    print(x)


div(2,3)

def mult(a,b,x=1,y=1):
    c=a*b*x*y
    print(c)
    return c

mult(2,3)
mult(2,3,3,4)

def msg(nome = 'Milton',txt='BOA NOITE'):
    print(txt,nome)
    
msg('Marcus')
msg('Bom Tarde')

```