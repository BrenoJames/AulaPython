def gen1():
    print('ComeçouGEN1')
    yield 1
    yield 2
    yield 3
    print('AcabouGEN1')

def gen3(gen):
    print('ComeçouG3')
    yield 10
    yield 20
    yield 30
    print('ACABOUG3')

def gen2(gen):
    print('ComeçouG2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOUG2')

g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)