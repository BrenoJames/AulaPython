# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10) #lista = [numero * 2 for numero in range(10) taboada 2
]
print(list(range(10)))
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # mapeamento de dados, se o preço for maior que 20, aumenta 5%, senão mantém o mesmo preço
    if produto['preco'] > 20 else {**produto} #mapeamento
    for produto in produtos
]

#p(novos_produtos)
#print(*novos_produtos, sep='\n') 
#lista = [ n for n in range(10) if n < 5] #filtragem de dados, só pega os números pares
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # mapeamento de dados, se o preço for maior que 20, aumenta 5%, senão mantém o mesmo preço
    if produto['preco'] > 20 else {**produto} #mapeamento
    for produto in produtos
    if (produto['preco'] >= 20 and produto ['preco'] * 1.05 > 10) #filtragem de dados, só pega os produtos com preço maior que 15
]
# esquerda do for é mapeamento, direita do for é filtragem
p(novos_produtos)
