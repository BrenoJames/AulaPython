#COMPREENÇÃO DE DICIONARIO
produto = {
    'nome' : 'Caneta',
    'preço': 1.50,
    'categoria': 'Papelaria',
}

dc = {
    chave : valor 
    if isinstance(valor, str) else valor #verifica se o valor é um número, se for, mantém o mesmo valor, senão, transforma em maiúscula 
    for chave, valor
    in produto.items()
    if chave != 'categoria' or chave == 'preço' #filtra os dados, só pega a categoria e o preço
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor
    in lista
} 

s1 = {2 ** i for i in range(10)}   
print(s1)



# "!#" diferente
#isinstance é uma função que verifica se um objeto é uma instância de uma classe ou de uma tupla de classes.
#Ela retorna True se o objeto for uma instância da classe ou de uma tupla de classes, 
#e False caso contrário.

#print(dict(lista))



