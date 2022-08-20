"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; se tiver entre 5 e 7 letras "Seu nome é normal";
caso tenhas mais que 7 letras "Seu nome é longo"
"""

teclado = input('Por favor insira seu nome')
tamanho = len(teclado)

if tamanho <= 4:
    print ('Seu nome é curto')
elif tamanho <= 7:
    print ('Seu nome é normal')
else:
    print ('Seu nome é longo')
