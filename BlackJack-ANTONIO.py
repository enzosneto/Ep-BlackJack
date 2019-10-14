# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:57:31 2019

@author: enzo & antonio 
"""

#Importando as bibliotecas

import random


#Definindo os dois baralhos

baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*8


#Valor inicial 
dinheiro_inicial = 100

print('Você começará com 100 dinheiros para apostar no seu jogo de Blackjack')

#Aposta inicial
aposta = float(input('Quanto deseja apostar? '))
total_croupie = 0
total_jogador = 0
dinheiro_jogador = dinheiro_inicial + aposta

#Definindo as cartas na mão

def jogada_jogador(baralho):
    mao_jogador = []
    for i in range(2):
	    random.shuffle(baralho)
	    carta = baralho.pop()
	    if carta == 11:carta = "J"
	    if carta == 12:carta = "Q"
	    if carta == 13:carta = "K"
	    if carta == 14:carta = "A"
	    mao_jogador.append(carta)
    return mao_jogador

def jogada_croupie(baralho):
    mao_croupie = []
    for i in range(2):
	    random.shuffle(baralho)
	    carta = baralho.pop()
	    if carta == 11:carta = "J"
	    if carta == 12:carta = "Q"
	    if carta == 13:carta = "K"
	    if carta == 14:carta = "A"
	    mao_croupie.append(carta)
    return mao_croupie

jogadas = 0

while dinheiro_jogador >= 0:
    
    
        #definindo o valor das cartas da mão
    
    def pontos(mao_jogador, mao_croupie, total):
        
        print(mao_jogador, mao_croupie)
        
        for carta in mao_jogador:
            if carta == "J" or carta == "Q" or carta == "K":
              total+= 10
            elif carta == "A":
                if total >= 11:
                    total+= 1
                else: 
                    total+= 11
            else: 
                total += carta
                
        for carta in mao_croupie:
            if carta == "J" or carta == "Q" or carta == "K":
              total+= 10
            elif carta == "A":
                if total >= 11:
                    total+= 1
                else: 
                    total+= 11
            else: 
                total += carta

            return total_jogador, total_croupie

