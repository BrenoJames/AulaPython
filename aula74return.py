"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):  #essa função criar_saudacao recebe um argumento saudacao
    #, que é uma string representando a saudação desejada (por exemplo, 'Bom dia' ou 'Boa noite').
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Thais', 'Breno', 'Zuleide']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))