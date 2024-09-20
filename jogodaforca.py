import random

# Criando uma lista de palavras que serão sorteadas
palavras = ['python', 'programacao', 'adson', 'variavel', 'aula', 'timeti']

# Escolhemos uma das palavras
palavra_sorteada = random.choice(palavras)

# Criamos uma string com traços que representam as letras
palavra_escondida = '*' * len(palavra_sorteada)

# Criamos uma lista vazia para armazenar as letras que já foram faladas
letras_adivinhadas = []

# Definindo o número máximo de tentativas
max_tentativas = 6

# Loop principal do jogo
while True:
    # Mostra na tela a palavra escondida
    print(palavra_escondida)

    # Pedimos ao jogador para digitar uma letra
    letra = input('Digite uma letra: ')

    # Verificamos se a letra já foi digitada
    if letra in letras_adivinhadas:
        print('Você já digitou essa letra')
        continue

    # Adiciona a letra à lista de letras digitadas
    letras_adivinhadas.append(letra)

    # Verificar se a letra digitada está na palavra sorteada
    if letra in palavra_sorteada:
        lista = list(palavra_escondida)
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista[indice] = letra
        palavra_escondida = ''.join(lista)  # Atualiza a palavra escondida
    else:
        # Letra não está na palavra sorteada
        max_tentativas -= 1
        print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas')

    # Verificamos se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print('Parabéns, você ganhou!!')
        break
    elif max_tentativas == 0:
        print(f'Você perdeu! A palavra era: {palavra_sorteada}')
        break
        print('VocÊ perdeu. A palavra era {palavra_sorteada}.')
        break
