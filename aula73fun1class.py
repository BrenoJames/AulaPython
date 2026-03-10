"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome): #essa função recebe dois argumentos, msg e nome, e retorna uma string /
     #formatada que combina a mensagem e o nome.
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Breno') #aqui passa a função saudacao como argumento 
    #para a função executa, e os argumentos 'Bom dia' e 'Breno' são passados para a função 
    #saudacao dentro da função executa.'''
)
print(
    executa(saudacao, 'Boa noite', 'Thais!!')
)