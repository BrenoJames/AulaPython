# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Thais', 1, 2, 3, 'Zu']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Zu', 'Zezim', ],  # 0
    # 0
    ['Maria', ],  # 1
    # 0       1       2
    ['Breno', 'João', 'Thais', ],  # 2
]

#p, b, *_, ap, u = lista
#print(p, u, ap)

print('Maria', 'Thais', 1, 2, 3, 'Zu')
print(*lista)
print(*string)
print(*tupla)

print(* lista, sep='\n')