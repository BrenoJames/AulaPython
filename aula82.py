def executa(funcao, *args):
    return funcao(*args)

#lambda é uma função anônima, ou seja, sem nome, que pode ser definida em uma única linha.
#Ela é útil para criar funções simples e rápidas, especialmente quando você precisa passar 
#uma função como argumento para outra função.
#args é um parâmetro especial que permite passar um número variável de argumentos para uma função.
# def soma(x, y):
#     return x + y


#def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)