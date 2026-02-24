'''senha_salva = '123456'
senha_digitada = ''
repeticoes = 0 

while senha_salva != senha_digitada:
    senha_digitada = input('Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas!')
'''
# usa p while quando voce nao sabe precisamente quantas vezes vai usar

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    print(novo_texto + '*')
# se a letra no texto exiba a letra na tela