import re
import random
import sys

print('--- VALIDADOR E GERADOR DE CPF ---')
print('1 - Validar CPF')
print('2 - Gerar CPF')

opcao = input('Escolha uma opção: ')

# ---------------- VALIDADOR ----------------

if opcao == '1':

    entrada = input('CPF DO USUARIO: ')
    cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)

    entrada_e_sequencial = (
        cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
    )

    if entrada_e_sequencial:
        print('CPF Inválido❌: Sequência de números repetidos 😒')
        sys.exit()

    nove_digitos = cpf_enviado_usuario[:9]

    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)

    contador_regressivo_2 = 11
    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
        print(f'CPF é válido 👍: {cpf_enviado_usuario}')
    else:
        print(f'CPF inválido ❌: {cpf_enviado_usuario}')


# ---------------- GERADOR ----------------

elif opcao == '2':

    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)

    contador_regressivo_2 = 11
    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    print(f'CPF gerado: {cpf_gerado}')

else:
    print('Opção inválida')
