import re
nreal = input('Digite um número qualquer: ')
result = r'([+|-]*)(\d+)(,*)(\d*)'

if re.findall(result, nreal):
    print('OK')
else:
    print('ERRO')