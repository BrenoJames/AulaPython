#exemplos!!!

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())  # Convertendo para minúscula para evitar duplicatas

    if 'l' in letras:
        print('A letra "l" foi digitada, encerrando o programa.')
        break

    print(letras)