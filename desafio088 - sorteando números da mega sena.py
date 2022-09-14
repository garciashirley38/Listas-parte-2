"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep
print("-"*30)
print('JOGO DA MEGA SENA')
print("-"*30)

totaljogos = int(input('Quantos jogos quer sortear?'))
sleep(1)
for c in range(0, totaljogos):
    jogo = []
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {c+1}:{sorted(jogo)}')
    sleep(1)
print('-'"BOA SORTE"'-')
