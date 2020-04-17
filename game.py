from random import choice
from time import sleep
def jo_ken_pô(msg):
    print(msg)
    sleep(0.3)
def jogo(pc, jogador):
    print(13*'-=')
    print(f'Computador jogou {pc} \nJogador Jogou {jogador}')
    print(13 * '-=')
def resultado(pc, jogador, v):
    if computador == 'PEDRA':
        if opcão == 'PEDRA':
            print('EMPATE !')
        elif opcão == 'PAPEL':
            print('JOGADOR VENCEU! ')
            lista[0].append(1)
        elif opcão == 'TESOURA':
            print('COMPUTADOR VENCEU! ')
            lista[1].append(1)
    if computador == 'PAPEL':
        if opcão == 'PAPEL':
            print('EMPATE')
        elif opcão == 'TESOURA':
            print('JOGADOR VENCEU!')
            lista[0].append(1)
        elif opcão == 'PEDRA':
            print('COMPUTADOR VENCEU!')
            lista[1].append(1)
    if computador == 'TESOURA':
        if opcão == 'TESOURA':
            print('EMPATE:')
        elif opcão == 'PEDRA':
            print('JOGADOR VENCEU! ')
            lista[0].append(1)
        elif opcão == 'PAPEL':
            print('COMPUTADOR VENCEU! ')
            lista[1].append(1)
lista = [[], []]
while True:
    continuar = ' '
    opcão = ' '
    opcão_pc = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = choice(opcão_pc) #Sorteia uma opcão para o computador
    print(f'{"==== PEDRA, PAPEL, TESOURA ===":^30}')
    while opcão not in 'PEDRAPAPELTESOURA':
        opcão = str(input('Suas opções: \n - PEDRA \n - PAPEL \n - TESOURA \n Qual é a sua escolha? ')).upper().strip()
    jo_ken_pô('JO')
    jo_ken_pô('KEN')
    jo_ken_pô('PÔ')
    jogo(computador, opcão)
    resultado(computador, opcão, lista)
    print(13*'-=')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ?')).upper().strip()[0]
    if continuar == 'N':
        print(13*'-=')
        print(f'O computador venceu {sum(lista[1])} vezes \nO jogador venceu {sum(lista[0])}')
        print(13*'-=')
        break
