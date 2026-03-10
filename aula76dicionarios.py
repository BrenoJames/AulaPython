# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#    'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
""" pessoa = {
    'nome': 'Breno',
    'sobrenome': 'James',
    'idade': 29,
    'altura': 1.76,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave]) """


""" pessoa = {}


chave = 'nome'

pessoa [chave] ='Breno James'
pessoa ['sobrenome'] = 'Matos'


print(pessoa[chave])

pessoa[chave] = 'Thaisss'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#print(pessoa.get('sobrenome')) # get é um método de dicionário que retorna o valor da chave especificada, ou um valor padrão se a chave não existir.
if pessoa.get('sobrenome') is None:
   print('NÃO EXISTE!!!!')
else:
    print(pessoa['sobrenome'])
 """

#print('Isso nao vai ser impresso')
'''
p1 = {
    'nome': 'Breno',
    'sobrenome': 'James',
}
#print(p1.get('nome'))
#print(p1.get('sobrenome'))

nome = p1.pop('nome') # pop é um método de dicionário que remove a chave especificada e retorna o valor correspondente. Se a chave não existir, ele levanta um KeyError.
print(nome)
print(p1) '''

""" ultima_chave = p1.popitem() # popitem é um método de dicionário que remove e retorna um par chave-valor arbitrário do dicionário. Se o dicionário estiver vazio, ele levanta um KeyError.
print(ultima_chave)
print(p1) 


p1.update({

    'sobrenome': 'Matos',
    'idade': 29,    
})1
print(p1) 


import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy() # copy é um método de dicionário que retorna uma cópia rasa do dicionário.

d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2) 


 pessoa = {
    'nome': 'Breno',
    'sobrenome': 'James',
    'idade': 29,
#    'altura': 1.76,
}

pessoa.setdefault('altura', 1.76) # setdefault é um método de dicionário que retorna o valor da chave especificada. Se a chave não existir, ela é adicionada ao dicionário com o valor padrão fornecido.
print(pessoa['altura']) """

#print(len(pessoa)) # len() retorna o número de itens em um dicionário, ou seja, o número de pares chave-valor.
#print(list(pessoa.keys())) # keys() retorna uma visão das chaves do dicionário.
#print(list(pessoa.values())) # values() retorna uma visão dos valores do dicionário.
#print(list(pessoa.items())) # items() retorna uma visão dos pares chave-valor do dicionário.

#for valor in pessoa.values():
#   print(valor)

#for chave, valor in pessoa.items():
#    print(chave, valor)"""