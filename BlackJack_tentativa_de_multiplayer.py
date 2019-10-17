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

#Nome dos participantas

nome_jogador = input('Olá, jogador 1, digite aqui seu nome: ').upper()
nome_jogador_2 = input('Olá, jogador 2, digite aqui seu nome: ').upper()

#Valor inicial 
dinheiro_inicial = 100
aposta = 0
dinheiro_jogador = dinheiro_inicial + aposta

aposta2 = 0
dinheiro_jogador_2 = dinheiro_inicial + aposta2
print('{0} começará com 100 dinheiros para apostar no seu jogo de Blackjack'.format(nome_jogador))
print('{0} começará com 100 dinheiros para apostar no seu jogo de Blackjack'.format(nome_jogador_2))

#Aposta inicial
apostando=False
while apostando == False:
    aposta = float(input('Quanto {0} deseja apostar? '.format(nome_jogador)))
    if aposta > dinheiro_inicial:
        print("Aposta Invalida")
    elif aposta > dinheiro_jogador:
        print('Aposta Inválida')
    elif aposta < 0:
        print("Aposta Invalida")
    else:
        apostando=True
        
apostando=False
while apostando == False:
    aposta2 = float(input('Quanto {0} deseja apostar? '.format(nome_jogador_2)))
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


def jogada_jogador_2(baralho):
    mao_jogador_2 = []
    for i in range(2):
	    random.shuffle(baralho)
	    carta = baralho.pop()
	    if carta == 11:carta = "J"
	    if carta == 12:carta = "Q"
	    if carta == 13:carta = "K"
	    if carta == 14:carta = "A"
	    mao_jogador_2.append(carta)
        
    total_jogador_2 = 0
    for carta in mao_jogador_2:
        if carta == "J" or carta == "Q" or carta == "K":
            total_jogador_2+= 10
        elif carta == "A":
            if total_jogador_2 >= 11:
                total_jogador_2+= 1
            else: 
                total_jogador_2+= 11
        else: 
            total_jogador_2 += carta
            
    return mao_jogador_2, total_jogador_2

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

while jogando == True and dinheiro_jogador > 0 and dinheiro_jogador_2 > 0:
    
    #definindo as pontuações

    mao_jogador, total_jogador = jogada_jogador(baralho)
    mao_jogador_2, total_jogador_2 = jogada_jogador_2(baralho)
    mao_croupier, total_croupier = jogada_croupier(baralho)
    
    
    print('Mão de {2}: {0}. Seus pontos: {1}'.format(mao_jogador, total_jogador, nome_jogador.upper()))
    print('Mão de {2}: {0}. Seus pontos: {1}'.format(mao_jogador_2, total_jogador_2, nome_jogador_2.upper()))
    
    if total_jogador == 21:   
        
        aposta = aposta + 1.5*aposta
        dinheiro_jogador = dinheiro_jogador + aposta + aposta2 
        aposta2 = aposta2 + 1.5*aposta2
        dinheiro_jogador2 = dinheiro_jogador - aposta2
        print('Parabéns {0}!!! Você fez os 21 pontos e ganhou a rodada'.format(nome_jogador))
        print('{1}, seu saldo é de: {0}'.format(dinheiro_jogador, nome_jogador))
        print('{1}, seu saldo é de: {0}'.format(dinheiro_jogador_2, nome_jogador_2))
        
    elif total_jogador_2 == 21:
        
        aposta = aposta + 1.5*aposta
        dinheiro_jogador = dinheiro_jogador - aposta
        aposta2 = aposta2 + 1.5*aposta2
        dinheiro_jogador2 = dinheiro_jogador + aposta2 + aposta
        print('Parabéns {0}!!! Você fez os 21 pontos e ganhou a rodada'.format(nome_jogador_2))
        print('{1}, seu saldo é de: {0}'.format(dinheiro_jogador_2, nome_jogador_2))
        print('{1}, seu saldo é de: {0}'.format(dinheiro_jogador, nome_jogador))
        
    elif total_jogador == 21 and total_jogador_2 == 21:
        
        aposta = aposta + 1.5*aposta
        dinheiro_jogador = dinheiro_jogador + aposta
        aposta2 = aposta2 + 1.5*aposta2
        dinheiro_jogador_2 = dinheiro_jogador_2 + aposta2 
        print('Parabéns!!! Os dois fizeram 21 pontos e ganharam a rodada')
        print('Seu saldo é de: {0}'.format(dinheiro_jogador))
        print('Seu saldo é de: {0}'.format(dinheiro_jogador_2))
        
    elif total_jogador < 21 and total_jogador_2 < 21:
        
        pergunta = int(input('Se {0} quiser mais uma carta, digite 0. Caso não queira mais carta, digite 1. Digite aqui sua resposta: '.format(nome_jogador)))
        
        
        while pergunta == 0:
            nova_carta, ponto_nova_carta = carta(baralho)
            print('Carta retirada: {0}'.format(nova_carta))     
            total_jogador += ponto_nova_carta
            print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
            if total_jogador > 21:
                dinheiro_jogador = dinheiro_jogador - aposta
                print('Você estourou o limite')
                print('{1}, seu saldo é de: {0}'.format(dinheiro_jogador, nome_jogador))
                break
            elif total_jogador == 21:
                aposta = aposta + 1.5*aposta
                dinheiro_jogador = dinheiro_jogador + aposta        
                print('Parabéns!!! {0} fez os 21 pontos e ganhou a rodada'.format(nome_jogador))
                print('Seu saldo é de: {0}'.format(dinheiro_jogador))
                break
            else:
                pergunta = int(input('Se {0} quiser mais uma carta, digite 0. Caso não queira mais carta, digite 1. Digite aqui sua resposta: '.format(nome_jogador)))
    
        pergunta2 = int(input('Se {0} quiser mais uma carta, digite 0. Caso não queira mais carta, digite 1. Digite aqui sua resposta: '.format(nome_jogador_2)))
        
        while pergunta2 == 0:
                nova_carta, ponto_nova_carta = carta(baralho)
                print('Carta retirada: {0}'.format(nova_carta))     
                total_jogador_2 += ponto_nova_carta
                print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                if total_jogador_2 > 21:
                    dinheiro_jogador_2 = dinheiro_jogador_2 - aposta2
                    print('Você estourou o limite')
                    print('{1}, seu saldo é de: {0}'.format(dinheiro_jogador_2, nome_jogador_2))
                    break
                elif total_jogador_2 == 21:
                    aposta2 = aposta2 + 1.5*aposta2
                    dinheiro_jogador_2 = dinheiro_jogador_2 + aposta2        
                    print('Parabéns!!! {0} fez os 21 pontos e ganhou a rodada'.format(nome_jogador_2))
                    print('Seu saldo é de: {0}'.format(dinheiro_jogador_2))
                    break
                else:
                    pergunta = int(input('Se {0} quiser mais uma carta, digite 0. Caso não queira mais carta, digite 1. Digite aqui sua resposta: '.format(nome_jogador_2)))
        
    
    if pergunta == 1 and pergunta2 == 1:
            
            print('Mão Croupier: {0}. Pontos Croupier: {1}'.format(mao_croupier, total_croupier))

            while total_croupier < 17:

                nova_carta, ponto_nova_carta = carta(baralho)
                print('Carta retirada: {0}'.format(nova_carta))
                total_croupier += ponto_nova_carta
                
            if total_croupier <= 21 and total_croupier >= 17:
                
                if total_croupier > total_jogador and total_croupier > total_jogador_2:
                    
                    if total_croupier == 21:
                        
                        dinheiro_jogador = dinheiro_jogador - 2.5*aposta
                        dinheiro_jogador_2 = dinheiro_jogador_2 - 2.5*aposta2
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                        print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                        print("O Croupier conseguiu o Blackjack... foi mal amigo")
                        print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                        print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                        
                        jogando = False
                        
                        
                    else:
                        
                        dinheiro_jogador = dinheiro_jogador - aposta
                        dinheiro_jogador_2 = dinheiro_jogador_2 - aposta2
                        print("Pontos do Croupier: {0}".format(total_croupier))
                        print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                        print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                        print("O Croupier venceu... vocês perderam essa")
                        print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                        print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                        jogando = False
                    
                
                elif total_croupier == total_jogador and total_jogador == total_jogador_2:
                    
                    dinheiro_jogador = dinheiro_jogador
                    dinheiro_jogador_2 = dinheiro_jogador_2
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                    print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                    print("Houve um empate")
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                    jogando = False
                    
                    
                elif total_jogador > total_jogador_2 and total_jogador > total_croupier:
                    
                    dinheiro_jogador = dinheiro_jogador + aposta + aposta2
                    dinheiro_jogador_2 = dinheiro_jogador_2 - aposta2
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                    print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                    print("{0}, você ganhou".format(nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                    jogando = False
                    
                elif total_jogador_2 > total_jogador and total_jogador_2 > total_croupier:
                    
                    dinheiro_jogador_2 = dinheiro_jogador_2 + aposta + aposta2
                    dinheiro_jogador = dinheiro_jogador - aposta
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                    print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                    print("{1}, você ganhou".format(nome_jogador_2))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                    jogando = False
                    
                    
            else:
                
                if total_jogador > total_jogador_2:
                    
                    dinheiro_jogador = dinheiro_jogador + aposta + aposta2
                    dinheiro_jogador_2 = dinheiro_jogador_2 - aposta2
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                    print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                    print("{1}, você ganhou".format(nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                    jogando = False
                    
                elif total_jogador_2 > total_jogador:
                    
                    dinheiro_jogador_2 = dinheiro_jogador_2 + aposta + aposta2
                    dinheiro_jogador = dinheiro_jogador - aposta
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos de {1}: {0}".format(total_jogador, nome_jogador))
                    print("Pontos de {1}: {0}".format(total_jogador_2, nome_jogador_2))
                    print("{1}, você ganhou".format(nome_jogador_2))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador, nome_jogador))
                    print("{1}, seu saldo é de: {0}".format(dinheiro_jogador_2, nome_jogador_2))
                    jogando = False
                    
                
    pergunta2 = input('Vocês desejam continuar jogando? Digite SIM para coninuar e NAO para parar: ')
    
    if pergunta2 == "SIM":
        
        baralho=baralho_*n
        
        apostando=False
        while apostando == False:
            aposta = float(input('Quanto {0} deseja apostar? '.format(nome_jogador)))
            if aposta > dinheiro_inicial:
                print("Aposta Invalida")
            elif aposta > dinheiro_jogador:
                print('Aposta Inválida')
            elif aposta < 0:
                print("Aposta Invalida")
            else:
                apostando=True

        apostando=False
        while apostando == False:
            aposta2 = float(input('Quanto {0} deseja apostar? '.format(nome_jogador_2)))
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
        if dinheiro_jogador > dinheiro_jogador_2:
            print('Parabéns, {0} ganhou'.format(nome_jogador))
        elif dinheiro_jogador_2 > dinheiro_jogador:
            print('Parabéns, {0} ganhou'.format(nome_jogador_2))
        else:
            print('Vocês empataram')
        jogando = False
                        

                        
                        
    
                
                
            
            
#PERGUNTAS
#SE O CROUPIER SAI C 14 E RETIRA 2 ELE FICA C 16 OU ESTOURA A PONTUAÇÃO DE 17?
#PROBLEMA COM A APOSTA
#WHILE PRINCIPAL C PROBLEMAS 
