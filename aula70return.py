"""
Retorno de valores das funções (return)
"""


def soma(x, y): # -> int: # anotação de tipo (type hint)
    if x > 10:
        return [10, 20] # o return pode retornar qualquer tipo de dado, inclusive mais de um valor 
    #(lista, tupla, dicionário, etc)
    return x + y # o return é a última linha executada da função, ou seja, tudo que estiver depois do return não será executado


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))