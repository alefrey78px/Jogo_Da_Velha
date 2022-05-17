# Representa o tabuleiro
tabuleiro = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
# Armazena o número de jogadas, serve para ver em quantas
# jogadas um jogador venceu ou para definir o empate
jogadas = 0


# Exibe o tabuleiro na tela.
def exibe():
    print('-------------')
    print('| {} | {} | {} |'.format(tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print('| {} | {} | {} |'.format(tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print('| {} | {} | {} |'.format(tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print('-------------')


# Pede a posição para jogar. Caso esteja vazia coloca o caractere correspondente
# ao jogador na posição. Caso não esteja informa e pede novamente a posição para jogar.
def joga(jogador):
    while True:
        jogada = int(input('Jogador {} >>  '.format(jogador)))
        if tabuleiro[jogada] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            print('Essa posição não está vazia! Tente novamente!')
            continue
        else:
            tabuleiro[jogada] = jogador
            return


# verifica se alguem venceu
def vencedor():
    # horizontais
    if tabuleiro[0] == 'x' and tabuleiro[1] == 'x' and tabuleiro[2] == 'x':
        return True
    elif tabuleiro[3] == 'x' and tabuleiro[4] == 'x' and tabuleiro[5] == 'x':
        return True
    elif tabuleiro[6] == 'x' and tabuleiro[7] == 'x' and tabuleiro[8] == 'x':
        return True
    elif tabuleiro[0] == 'o' and tabuleiro[1] == 'o' and tabuleiro[2] == 'o':
        return True
    elif tabuleiro[3] == 'o' and tabuleiro[4] == 'o' and tabuleiro[5] == 'o':
        return True
    elif tabuleiro[6] == 'o' and tabuleiro[7] == 'o' and tabuleiro[8] == 'o':
        return True
    # verticais
    elif tabuleiro[0] == 'x' and tabuleiro[3] == 'x' and tabuleiro[6] == 'x':
        return True
    elif tabuleiro[1] == 'x' and tabuleiro[4] == 'x' and tabuleiro[7] == 'x':
        return True
    elif tabuleiro[2] == 'x' and tabuleiro[5] == 'x' and tabuleiro[8] == 'x':
        return True
    elif tabuleiro[0] == 'o' and tabuleiro[3] == 'o' and tabuleiro[6] == 'o':
        return True
    elif tabuleiro[1] == 'o' and tabuleiro[4] == 'o' and tabuleiro[7] == 'o':
        return True
    elif tabuleiro[2] == 'o' and tabuleiro[5] == 'o' and tabuleiro[8] == 'o':
        return True
    # diagonais
    elif tabuleiro[0] == 'x' and tabuleiro[4] == 'x' and tabuleiro[8] == 'x':
        return True
    elif tabuleiro[2] == 'x' and tabuleiro[4] == 'x' and tabuleiro[6] == 'x':
        return True
    elif tabuleiro[0] == 'o' and tabuleiro[4] == 'o' and tabuleiro[8] == 'o':
        return True
    elif tabuleiro[2] == 'o' and tabuleiro[4] == 'o' and tabuleiro[6] == 'o':
        return True


# Verifica se foi empate
def empate():
    if not vencedor() and jogadas == 9:  # se não teve vencedor e ja foram 9 jogadas
        return True  # retorna True que foi empate
    else:
        return False


# joga computador
# def joga_computador():


# programa principal
exibe()
while True:
    # joga o X
    joga('x')
    jogadas += 1
    exibe()
    if vencedor():
        print('O jogador *x* venceu com {} jogadas.' .format(jogadas))
        break
    elif empate():
        print('Empate! Acabaram as 9 jogadas e ninguém ganhou!')
        break
    # joga o O
    joga('o')
    jogadas += 1
    exibe()
    if vencedor():
        print('O jogador *o* venceu com {} jogadas.' .format(jogadas))
        break
    elif empate():
        print('Empate!')
        break
