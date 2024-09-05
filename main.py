
cpf_usuario = input('qual o cpf a ser analisado?')
digitos_1 = cpf_usuario[:9]
contador = 10
primeiro_dig = 0
segundo_dig = 0

for digito in digitos_1:
    primeiro_dig += int(digito) * contador
    contador -= 1
    
primeiro_dig = (primeiro_dig * 10) % 11
if primeiro_dig <= 9:
    primeiro_dig
else:
    primeiro_dig = 0


digitos_2 = digitos_1 + str(primeiro_dig)
contador_2 = 11

for digito in digitos_2:
    segundo_dig += int(digito) * contador_2
    contador_2 -= 1
segundo_dig = (segundo_dig * 10) % 11
if segundo_dig <= 9:
    segundo_dig
else:
    segundo_dig = 0

cpf_gerado = f'{digitos_1}{primeiro_dig}{segundo_dig}'

if cpf_usuario == cpf_gerado:
    print('o cpf é válido')
else:
    print('o cpf é invalido')
    
