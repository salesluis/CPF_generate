"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

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
    