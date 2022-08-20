"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. EX: Bom dia, Boa tarde, Boa noite.
"""

teclado = input('insira uma hora')

if teclado.isdigit():
    teclado = float(teclado)

    if teclado < 0 or teclado > 23:
        print('Por favor insira um horario correto')

    else:
        if teclado <= 11:
            print('Bom dia')
        elif teclado <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')

else:
    print('Por favor insira um horario correto')
