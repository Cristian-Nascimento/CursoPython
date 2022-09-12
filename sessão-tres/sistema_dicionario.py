
perguntas = {
    'pergunta 1': {
        'pergunta': 'Raiz Quadrada de 9?',
        'respostas': {'a':'1', 'b':'2', 'c':'3', 'd':'4',},
        'resposta_certa': 'c',
    },
        'pergunta 2': {
        'pergunta': 'Quanto é 9 * 15?',
        'respostas': {'a':'135', 'b':'200', 'c':'98', 'd':'130',},
        'resposta_certa': 'a',
    },
}
print()

for chave_pergunta, chave_resposta in perguntas.items():
    print(f'{chave_pergunta}: {chave_resposta["pergunta"]}')

    for resposta_key, resposta_values in chave_resposta['respostas'].items():
        print(f'[{resposta_key}]: {resposta_values}')

    print()
    resposta_usuario = input('Selecione a alternativa correta: ')
    
    if resposta_usuario == chave_resposta['resposta_certa']:
        print('Voce Acertou')

    else:
        print('Voce Errou')
