#dir, hasattre e get attr em python

string = 'Breno'
metodo = 'strip'

if hasattr(string , 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)( ))
    print(string)