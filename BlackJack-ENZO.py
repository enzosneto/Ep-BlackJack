# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:57:31 2019

@author: enzo & antonio 
"""

#Importando as bibliotecas

import random


#Definindo os dois baralhos
total=0
n=int(input("Com quantos baralhos voce quer jogar? "))
baralho_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
baralho=baralho_*n

#Valor inicial 
dinheiro_inicial = 100
apostando=False
print('Você começará com 100 dinheiros para apostar no seu jogo de Blackjack')

#Aposta inicial
while apostando == False:
    aposta = float(input('Quanto deseja apostar? '))
    if aposta > dinheiro_inicial:
        print("Aposta Invalida")
    elif aposta < 0:
        print("Aposta Invalida")
    else:
        apostando=True

#Definindo as cartas na mão

def jogada(baralho):
    mao = []
    for i in range(2):
	    random.shuffle(baralho)
	    carta = baralho.pop()
	    if carta == 11:carta = "J"
	    if carta == 12:carta = "Q"
	    if carta == 13:carta = "K"
	    if carta == 14:carta = "A"
	    mao.append(carta)
    return mao



#definindo o valor das cartas da mão
    
def pontos(mao,total):
    print(mao)
    for carta in mao:
        if carta == "J" or carta == "Q" or carta == "K":
            total+= 10
        elif carta == "A":
            if total >= 11:
                total+= 1
            else: 
                total+= 11
        else: 
            total += carta
    return total

print(pontos(jogada(baralho),total))

