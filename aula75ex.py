""" def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadriplicar(numero):
    return numero * 4


print(duplicar(2))      # Saída: 4
print(triplicar(2))     # Saída: 6
print(quadriplicar(2))  # Saída: 8  """

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))      # Saída: 4
print(triplicar(2))     # Saída: 6
print(quadruplicar(2))  # Saída: 8

