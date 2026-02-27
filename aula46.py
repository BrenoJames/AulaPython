for i in range(10): # Loop de 0 a 9
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8: # Quando i é 8, o loop é interrompido
       print('i é 8, seu else não executará')
    break

    for j in range(1, 3): # Loop de 1 a 2
        print(i, j)
else: # Este else é associado ao primeiro for, não ao segundo
    print('For completo com sucesso!')