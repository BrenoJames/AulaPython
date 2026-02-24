""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ': # se tiver o espaço, o break é acionado, o loop é interrompido e o else não é executado
     break# Interrompe o loop, não executa o else!!!!! o BREAK SEMPRE INTERROMPE O LOOP, NÃO EXECUTA O ELSE
# por isso no terminal so aparece o valor!!
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')