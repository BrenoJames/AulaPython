lista = []
for x in range (3):
 for y in range (3):
  lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)

]
lista = [
    [(x, letra) for letra in 'Breno']
    for x in range(6)

]

print(lista)
# lado esquerdo for e para o mapeamento!!!
# lado direito for e para a filtragem!!!