#Mini jogo de Forca

palavra_secreta = 'awesome'
letras_digitadas = []
chances = 10

while True:

    if chances <= 0:
        print ('Voce perdeste!')
        break

    letra = input(' Digite uma letra: ')

    if len (letra) > 1:
        print (' Digite uma letra Apenas, zé')
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print (f' Eeeeeea, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f' Aff a "{letra}" não existe na palavra secreta')
        letras_digitadas.pop()

    print(letras_digitadas)

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        print(f' Bacana zé, oce acertou a palavra secreta :3 !!! a palavra era "{secreto_temporario}". ')
        break
    else:
        print(f' A palavra secreta está assim: {secreto_temporario}')

    if letra not in palavra_secreta:
        chances -= 1

    print(f'Voce ainda tem {chances} chances')
    print()
