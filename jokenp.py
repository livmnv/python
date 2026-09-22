from random import randint
from time import sleep

opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

print('-' * 30)

print(f'Você jogou {opcoes[jogador]}')
print(f'Computador jogou {opcoes[computador]}')

if computador == jogador:
    print('EMPATE')

elif (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1) or \
     (jogador == 0 and computador == 2):
    print('VOCÊ VENCEU')

else:
    print('VOCÊ PERDEU')