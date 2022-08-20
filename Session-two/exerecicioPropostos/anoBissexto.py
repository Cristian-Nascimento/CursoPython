"""
Crie um codigo que o usuário digita um ano e fale se ele é bissexto ou não
"""

ano = input("Digite um ano a ferivicar ")

if ano.isdigit():

    if ( len(ano) <= 4):
        ano = int(ano)

        def verifica_ano_bissexto(ano):
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 4 == 0:
                return True
            else:
                return False

        if (verifica_ano_bissexto(ano)):
            print(f'O {ano} é bissexto')

        else:
            print(f'O {ano} não é bissexto')

    else:
        print('Favor insira um ano correto')

else:
        print('Favor insira um ano correto')
