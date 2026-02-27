"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Breno' #iteravel
iteratador = iter(texto)  # iterator

while True:
    try:
        print(next(iteratador))
        print('letra')
    except StopIteration:
      break




    
# iterador é um objeto que pode ser iterado, ou seja, que pode ser percorrido elemento por elemento. Ele é criado a partir de um iterável usando a função iter() e pode ser percorrido usando a função next() para obter o próximo elemento. Quando não há mais elementos para percorrer, uma exceção StopIteration é levantada.