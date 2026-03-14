#generator = (n for n in range(100000)) # generator é função que vai pausando

def generator(n=0, maximum=10): # o yild vai pausar
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

        


gen = generator(maximum=10000000)
for n in gen:
    print(n)
