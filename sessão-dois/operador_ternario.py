"""
Operador ternario em Python
"""

logged_user = False

if logged_user == True:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar.'

print (msg)

# ou

# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

#--------------------------------------------------------------------------------------

idade = input('digite a sua idade')

if not idade.isnumeric():
    print('invalid idade')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msa = 'pode acessar' if e_de_maior else 'Não pode acessar'

    print(msa)
