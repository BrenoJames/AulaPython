'''import re
import sys

#cpf_enviado_usuario = "444.99.0108-88".replace('.', '-', ' ')\)

entrada = input('CPF [444.99.0108-88]: ')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('CPF Inválido: Sequência de números repetidos')
    sys.exit()

'''

import random

for _ in range(10):

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    print(nove_digitos)

    #sys.exit() Para não executar o código abaixo, que é o mesmo da aula62.py




    '''Calculo do primeiro dígito do CPF'''
    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultador_digito_2 = 0
    for digito in dez_digitos:
        resultador_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultador_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0


    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)
    '''if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
        print(f'CPF é Válido: {cpf_enviado_usuario}')
    else:    print(f'CPF Inválido: {cpf_enviado_usuario}')'''