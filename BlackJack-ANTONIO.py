# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:57:31 2019

@author: enzo & antonio 
"""

#Importando as bibliotecas

import random


#Definindo os dois baralhos

n=int(input("Com quantos baralhos voce quer jogar? "))
baralho_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
baralho=baralho_*n
print(len(baralho))
#definindo as pontuações

total_jogador=0
total_croupier=0

#Valor inicial 
dinheiro_inicial = 100
aposta = 0
dinheiro_jogador = dinheiro_inicial + aposta
apostando=False
print('Você começará com 100 dinheiros para apostar no seu jogo de Blackjack')

#Aposta inicial
while apostando == False:
    aposta = float(input('Quanto deseja apostar? '))
    if aposta > dinheiro_inicial:
        print("Aposta Invalida")
    elif aposta > dinheiro_jogador:
        print('Aposta Inválida')
    elif aposta < 0:
        print("Aposta Invalida")
    else:
        apostando=True

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

def jogada_croupier(baralho):
    mao_croupier = []
    for i in range(2):
	    random.shuffle(baralho)
	    carta = baralho.pop()
	    if carta == 11:carta = "J"
	    if carta == 12:carta = "Q"
	    if carta == 13:carta = "K"
	    if carta == 14:carta = "A"
	    mao_croupier.append(carta)
    return mao_croupier


#definindo o valor das cartas da mão
    
def pontos_jogador(mao_jogador,total_jogador):
    print(mao_jogador)
    for carta in mao_jogador:
        if carta == "J" or carta == "Q" or carta == "K":
            total_jogador+= 10
        elif carta == "A":
            if total_jogador >= 11:
                total_jogador+= 1
            else: 
                total_jogador+= 11
        else: 
            total_jogador += carta
    return total_jogador

def pontos_croupier(mao_croupier,total_croupier):
    print(mao_croupier)
    for carta in mao_croupier:
        if carta == "J" or carta == "Q" or carta == "K":
            total_croupier+= 10
        elif carta == "A":
            if total_croupier >= 11:
                total_croupier+= 1
            else: 
                total_croupier+= 11
        else: 
            total_croupier += carta
    return total_croupier

#Pegando uma carta aleatória
    
def carta(baralho):
    Baralho = []
    for i in range(baralho):
	    random.shuffle(baralho)
	    carta = baralho.pop()
	    if carta == 11:carta = "J"
	    if carta == 12:carta = "Q"
	    if carta == 13:carta = "K"
	    if carta == 14:carta = "A"
	    Baralho.append(carta)
    return Baralho

def ponto_carta(Baralho):
    ponto_carta = 0
    for carta in Baralho:
        if carta == "J" or carta == "Q" or carta == "K":
            ponto_carta = 10
        elif carta == "A":
            if total_croupier>= 11:
                ponto_carta = 1
            else: 
                ponto_carta= 11
        else: 
            ponto_carta = carta
        return ponto_carta
print(carta(ponto_carta(baralho)))

#print(pontos_croupier(jogada_croupier(baralho),total_croupier))
#print(pontos_jogador(jogada_jogador(baralho),total_jogador))

#Vamos ao jogo
jogando = True

while jogando or dinheiro_jogador>=0:
    
    if total_jogador == 21:   
        
        aposta = aposta + 1.5*aposta        
        print('Parabéns!!! Você fez os 21 pontos e ganhou a rodada')
        
    elif total_jogador < 21:
        
        pergunta = int(input('Se você deseja parar, digite 1. Caso queira continuar, digite 0'))
        
        if pergunta == 1:
            
            while total_croupier <= 17:   
                total_croupier += ponto_carta
                
                if total_croupier <= 21:
                    
                    if total_croupier > total_jogador:
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos do jogador: {0}".format(total_jogador))
                        print("O Croupier venceu... você perdeu essa")
                        print("Seu saldo é de: " )
                    
                    elif total_croupier == total_jogador:
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos do jogador: {0}".format(total_jogador))
                        print("Houve um empate")
                        print("Seu saldo é de: {0}".format(dinheiro_jogador))
                        
                    else:
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos do jogador: {0}".format(total_jogador))
                        print("Você ganhou")
                        print("Seu saldo é de: {0}".format(dinheiro_jogador))
                        
                else:
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos do jogador: {0}".format(total_jogador))
                        print("Você ganhou")
                        print("Seu saldo é de: {0}".format(dinheiro_jogador))
                        
        if pergunta == 0:
            
            jogando = False
            
                
                
                
            
            


