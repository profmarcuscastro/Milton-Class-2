# args - argumento da funcao / kwargs -  argumento com  !pre set!

lista = [1,2,3,4,5]
# desempacotando

n1,*n=lista
print(n1)
print(n)

print('#'*80)

print(lista)
print(*lista)#-->desempacotamento de lista
#n1,n2,n3


def func(*args):
    print(args)

func(lista,10,15)
#(n1,n2,n3)
func(*lista,10,15)