""" ex1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impart = entrada_int % 2 == 0
    par_impart_text = 'impar'

    if par_impart:
        par_impart_text = 'par'

    print(f'O numero {entrada_int} é {par_impart_text}')
else:
    print('Voce não digitou um numero inteiro')'''


'''try:
    entrada_int = float(entrada)
    par_impart = entrada_int % 2 == 0
    par_impart_text = 'impar'

    if par_impart:
        par_impart_text = 'par'

    print(f'O numero {entrada_int} é {par_impart_text}')
except:
    print('Voce não digitou um numero inteiro')'''


    

""" EX2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''entrada = input('Digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!!!')
    elif hora >= 11 and hora <= 17:
        print('Boa Tarde!!!')
    elif hora >= 181 and hora <= 23:
        print('Boa Noite!!!')
    else:
        print('Não conheço essa hora')
except: 
    print('Por favor, digite apenas numeors inteiros')
    ...'''



""" EX3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')