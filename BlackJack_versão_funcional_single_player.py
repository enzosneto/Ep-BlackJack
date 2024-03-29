# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:57:31 2019

@author: enzo & antonio 
"""

#Importando as bibliotecas

import random


#Definindo os dois baralhos
print("BlackJack - Ep Design de Software")
print("-"*80)
n=int(input("Com quantos baralhos deseja jogar? "))
print("-"*80)
baralho_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
baralho=baralho_*n

#Valor inicial 
dinheiro_inicial = 100
aposta = 0
dinheiro_jogador = dinheiro_inicial + aposta
print('Você começará com 100 dinheiros para apostar no seu jogo de Blackjack')

#Aposta inicial
apostando=False
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
        
    total_jogador = 0
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
            
    return mao_jogador, total_jogador

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
        
    total_croupier = 0
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
            
    return mao_croupier, total_croupier



#Pegando uma carta aleatória
    
def carta(baralho):
    random.shuffle(baralho)
    carta = baralho[0]
    carta = baralho.pop()
    if carta == 11:carta = "J"
    if carta == 12:carta = "Q"
    if carta == 13:carta = "K"
    if carta == 14:carta = "A"
    
    if carta == "J" or carta == "Q" or carta == "K":
        ponto_carta = 10
    elif carta == "A":
        if total_croupier >= 11:
            ponto_carta = 1
        else: 
            ponto_carta= 11
    else: 
        ponto_carta = carta

        
    return carta, ponto_carta



#Vamos ao jogo
    
jogando = True

while jogando == True and dinheiro_jogador > 0:
    
    #definindo as pontuações

    mao_jogador, total_jogador = jogada_jogador(baralho)
    mao_croupier, total_croupier = jogada_croupier(baralho)
    print("-"*80)
    print('Sua mão: {0}. Seus pontos: {1}'.format(mao_jogador, total_jogador))
    
    if total_jogador == 21:   
        
        aposta = aposta + 1.5*aposta
        dinheiro_jogador = dinheiro_jogador + aposta        
        print('Parabéns!!! Você fez BlackJack!')
        print('Seu saldo é de: {0}'.format(dinheiro_jogador))

        
        
    elif total_jogador < 21:
        
        pergunta = int(input('Se você quiser mais uma carta, digite 0. Caso não queira mais carta, digite 1. Digite aqui sua resposta: '))
            
        while pergunta == 0:
            nova_carta, ponto_nova_carta = carta(baralho)
            print("-"*80)
            print('Carta retirada: {0}'.format(nova_carta))     
            total_jogador += ponto_nova_carta
            print("Pontos do jogador: {0}".format(total_jogador))
            if total_jogador > 21:
                dinheiro_jogador = dinheiro_jogador - aposta
                print('Você estourou o limite')
                print('Seu saldo é de: {0}'.format(dinheiro_jogador))
                break
            elif total_jogador == 21:
                aposta = aposta + 1.5*aposta
                dinheiro_jogador = dinheiro_jogador + aposta        
                print('Parabéns!!! Você fez BlackJack')
                print('Seu saldo é de: {0}'.format(dinheiro_jogador))
                break
            else:
                print("-"*80)
                pergunta = int(input('Se você quiser mais uma carta, digite 0. Caso não queira mais carta, digite 1. Digite aqui sua resposta: '))
    
        if pergunta == 1:
            print("-"*80)
            print('Mão Croupier: {0}. Pontos Croupier: {1}'.format(mao_croupier, total_croupier))

            while total_croupier < 17:
#                mao_croupier, total_croupier = jogada_croupier(baralho)
                nova_carta, ponto_nova_carta = carta(baralho)
                print("-"*80)
                print('Carta retirada: {0}'.format(nova_carta))
                total_croupier += ponto_nova_carta
                
            if total_croupier <= 21 and total_croupier >= 17:
                
                if total_croupier > total_jogador:
                    
                    if total_croupier == 21:
                        
                        dinheiro_jogador = dinheiro_jogador - 2.5*aposta
                        print("-"*80)
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos do jogador: {0}".format(total_jogador))
                        print("-"*80)
                        print("O Croupier conseguiu o Blackjack... foi mal amigo")
                        print("Seu saldo é de: {0}".format(dinheiro_jogador))
                        jogando = False
                        
                    else:
                        
                        dinheiro_jogador = dinheiro_jogador - aposta
                        print("-"*80)
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos do jogador: {0}".format(total_jogador))
                        print("-"*80)
                        print("O Croupier venceu... você perdeu essa")
                        print("Seu saldo é de: {0}".format(dinheiro_jogador))
                        jogando = False
                    
                
                elif total_croupier == total_jogador:
                    
                    dinheiro_jogador = dinheiro_jogador
                    print("-"*80)
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos do jogador: {0}".format(total_jogador))
                    print("-"*80)
                    print("Houve um empate")
                    print("Seu saldo é de: {0}".format(dinheiro_jogador))
                    jogando = False
                    
                    
                else:
                    
                    dinheiro_jogador = dinheiro_jogador + aposta
                    print("-"*80)
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos do jogador: {0}".format(total_jogador))
                    print("-"*80)
                    print("Você ganhou")
                    print("Seu saldo é de: {0}".format(dinheiro_jogador))
                    jogando = False
                    
                    
            else:
                dinheiro_jogador = dinheiro_jogador + aposta
                print("-"*80)
                print("Pontos do Croupier: {0}".format(total_croupier))
                print("Pontos do jogador: {0}".format(total_jogador))
                print("-"*80)
                print("Você ganhou")
                print("Seu saldo é de: {0}".format(dinheiro_jogador))
                jogando = False
                
    pergunta2 = input('Você deseja continuar jogando? Digitem SIM para coninuar e NAO para parar: ')
    
    if pergunta2 == "SIM":
        
        baralho=baralho_*n
        
        apostando=False
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
                
        jogando = True
        
    elif pergunta2 == "NAO": 
        jogando = False
                        

                        
                        
    
                
                
            
            
#PERGUNTAS
#SE O CROUPIER SAI C 14 E RETIRA 2 ELE FICA C 16 OU ESTOURA A PONTUAÇÃO DE 17?
#PROBLEMA COM A APOSTA
#WHILE PRINCIPAL C PROBLEMAS 
