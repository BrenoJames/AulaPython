#generator expression
import sys

iterable = ['eu', 'Tenho', '__iter__']
iterator = iter(iterable)# tem __iter__ e __next__ #2 underline se chama dunder
lista = [n for n in range(1000)]
generator = (n for n in range(1000)) 

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))  #sys nao esta definida

print(generator)


#for n in generator:
#    print(n)


