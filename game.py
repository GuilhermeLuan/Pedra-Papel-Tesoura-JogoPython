from random import choice
from time import sleep

def jogo(pc, jogador):
    print(13*'-=')
    print(f'Computador jogou {pc} \nJogador Jogou {jogador}')
    print(13 * '-=')

def resultado(pc, jogador):
    if computador == 'PEDRA':
        if opcão == 'PEDRA':
            print('EMPATE !')
        elif opcão == 'PAPEL':
            print('JOGADOR VENCEU! ')
        elif opcão == 'TESOURA':
            print('COMPUTADOR VENCEU! ')

    if computador == 'PAPEL':
        if opcão == 'PAPEL':
            print('EMPATE')
        elif opcão == 'TESOURA':
            print('JOGADOR VENCEU!')
        elif opcão == 'PEDRA':
            print('COMPUTADOR VENCEU!')

    if computador == 'TESOURA':
        if opcão == 'TESOURA':
            print('EMPATE:')
        elif opcão == 'PEDRA':
            print('JOGADOR VENCEU! ')
        elif opcão == 'PAPEL':
            print('COMPUTADOR VENCEU! ')

while True:
    continuar = ' '
    opcão = ' '
    opcão_pc = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = choice(opcão_pc) #Sorteia uma opcão para o computador


    print(f'{"==== PEDRA, PAPEL, TESOURA ===":^30}')
    while opcão not in 'PEDRAPAPELTESOURA':
        opcão = str(input('Suas opções: \n - PEDRA \n - PAPEL \n - TESOURA \n Qual é a sua escolha? ')).upper().strip()

    print('JO')
    sleep(0.3)
    print('KEN')
    sleep(0.3)
    print('PO!!!')
    sleep(0.3)

    jogo(computador, opcão)
    resultado(computador, opcão)

    print(13*'-=')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ?')).upper().strip()[0]
    if continuar == 'N':
        break
