"""''''
Iterando strings com while
"""
#       012345678910
'''nome = 'Breno James'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
nova_string = ''
nova_string += '*B*r*e*n*o* *J*a*m*e*s*'''



# Iterando strings com while
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Breno James'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)