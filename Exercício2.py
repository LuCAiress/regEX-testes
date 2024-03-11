import re

Telefone = r'(([0]*)\d{2}|\(([0]*)\d{2}\))( *)((\d{4,5})( |-*)(\d{4}))'

ntel = 1

while ntel:
    ntel = input('Digite um número de telefone (Com DDD): ')
    if(re.search(Telefone, ntel)):
        print('<<Este número é valido>>')
        continue
    else:
        print('<<Este número é invalido>>')
        continue
