# jogo da velha
# versão 0.2
# autor: Alexandre Frey
# Descrição: jogo simples para treinar python

import random  # para gerar numeros aleatorios

# Início da função exibe.
# Exibe o tabuleiro na tela.
def exibe(tabuleiro):
    print('┌───┬───┬───┐')
    print('│ {} │ {} │ {} │'.format(tabuleiro[1], tabuleiro[2], tabuleiro[3]))
    print('├───┼───┼───┤')
    print('│ {} │ {} │ {} │'.format(tabuleiro[4], tabuleiro[5], tabuleiro[6]))
    print('├───┼───┼───┤')
    print('│ {} │ {} │ {} │'.format(tabuleiro[7], tabuleiro[8], tabuleiro[9]))
    print('└───┴───┴───┘')
# Final da função exibe.


# Início da função joga.
# Pede a posição para jogar. Caso esteja vazia coloca o caractere correspondente
# ao jogador na posição. Caso não esteja informa e pede novamente a posição para jogar.
def joga_humano(tabuleiro, jogador):
    while True:
        try:
            jogada = int(input('Jogador {} informe a posição para jogar: '.format(jogador)))
            if jogada not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('Por favor informe uma das posições válidas listadas no tabuleiro!')
                continue
        except:
            print('Por favor informe uma das posições válidas listadas no tabuleiro!')
            continue

        if tabuleiro[jogada] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Essa posição não está vazia! Tente novamente!')
            continue
        else:
            tabuleiro[jogada] = jogador
            break
# Final da função joga.


# Início da função joga_computador.
# Nessa função o computador joga de forma aleatória em um espaço livre.
def joga_computador(tabuleiro, jogador):
    vagas = []
    i = len(tabuleiro)
    for i in range(1, i, 1):
        if tabuleiro[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            vagas.append(i)

    jogada = random.choice(vagas)
    tabuleiro[jogada] = jogador
    print('O jogador {} (computador) jogou na posição: {}'.format(jogador, jogada))
# Final da função joga_computador.


# Inicio da função vencedor, verifica se alguém venceu
def vencedor(tabuleiro):
    # horizontais
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3]:
        return True
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6]:
        return True
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9]:
        return True
    # verticais
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        return True
    elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9]:
        return True
    # diagonais
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9]:
        return True
    elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7]:
        return True
# Final da função vencedor


# Início da função empate.
def empate(tabuleiro, rodadas):
    if not vencedor(tabuleiro) and rodadas == 9:  # se não teve vencedor e ja foram 9 rodadas
        return True  # retorna True que foi empate
    else:
        return False
# Final da função empate.


# Início da função jogando.
def jogando(modo):
    tabuleiro = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    rodadas = 0

    if rodadas == 0:
        print('Início do jogo.')

    if modo == 'H':
        print('Jogando Humano vs. Humano')
    elif modo == 'C':
        print('Jogando Computador vs. Humano')

    exibe(tabuleiro)

    while True:
        # joga o X

        if modo == 'H':
            joga_humano(tabuleiro, 'X')
        elif modo == 'C':
            joga_computador(tabuleiro, 'X')

        rodadas += 1
        exibe(tabuleiro)
        if vencedor(tabuleiro):
            print('O jogador X venceu com {} rodadas.' .format(rodadas))
            break
        elif empate(tabuleiro, rodadas):
            print('Empate! Acabaram as 9 rodadas e ninguém ganhou!')
            break

        # joga o O
        joga_humano(tabuleiro, 'O')
        rodadas += 1
        exibe(tabuleiro)
        if vencedor(tabuleiro):
            print('O jogador O venceu com {} rodadas.' .format(rodadas))
            break
        elif empate(tabuleiro, rodadas):
            print('Empate!')
            break
# Final da função jogando.


# Inicio do programa principal
print('***** Bem vindo ao jogo da velha *****')
while True:
    print('Escolha o modo de jogo:')
    print('H. Humano vs. Humano')
    print('C. Computador vs. Humano')
    print('S. Sair')
    opcao = input('>> ')
    opcao = opcao.upper()
    if opcao == 'H':
        jogando('H')
    elif opcao == 'C':
        jogando('C')
    elif opcao == 'S':
        print('Saindo...')
        break
# Final do programa principal
