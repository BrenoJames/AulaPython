# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
""" s1 = set()  # vazio
s1 = {'Breno', 1, 2, 3}  # com dados
print(s1)
 """


""" l1 = (1, 2, 3, 2, 3, 3, 1)
s1 = set(l1)
l2 = list(s1)
print(s1)  # {1, 2, 3}
print(l2)  # [1, 2, 3] """

s1 = {1, 2, 3}
#print(4 in s1)  # False
# for numero in s1:
#     print(numero)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add("Breno")
s1.add(1)
s1.update(("Olá mundo!", 1, 2, 3, 4))
#s1.clear()  # limpa o set
s1.discard("Olá mundo!")  # remove o valor, se existir
s1.discard("Breno")  # não gera erro
#print(s1)  # {'Olá', 1, 2, 3, 'Breno', 'mundo!'}


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos



s1 = {1, 2, 3,}
s2 = {2, 3, 4,}
s3 = s1 | s2  # {1, 2, 3, 4}  não tem valores duplicados
s3 = s1 & s2  # {2, 3}  apenas os valores presentes em ambos
s3 = s1 - s2  # {1}  apenas os valores presentes no s1
s3 = s1 ^ s2  # {1, 4}  apenas os valores que não estão em ambos
print(s3)