import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # recarregar o modulo
    print(i)

print('Fim')