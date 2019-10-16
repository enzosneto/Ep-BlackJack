# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:57:34 2019

@author: Tonera
"""
import random

total_croupier = 0
total_jogador_1 = 0
total_jogador_2 = 0

mao_croupier = []
mao_jogador_1 = []
mao_jogador_2 = []

n=int(input("Com quantos baralhos voce quer jogar? "))
baralho_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
baralho=baralho_*n


def carta(baralho):
    random.shuffle(baralho)
    carta = baralho[0]
    carta = baralho.pop()
    if carta == 11:carta = "J"
    if carta == 12:carta = "Q"
    if carta == 13:carta = "K"
    if carta == 14:carta = "A"      
    return carta



def ponto_carta(carta):
    print(carta)
    ponto_carta = 0
    if carta == "J" or carta == "Q" or carta == "K":
        ponto_carta = 10
    elif carta == "A":
        if total_croupier >= 11 or total_jogador_1 >= 11 or total_jogador_2 >= 11:
            ponto_carta = 1
        else: 
            ponto_carta= 11
    else: 
        ponto_carta = carta
    return ponto_carta
print(ponto_carta(carta(baralho)))

def mao_jogador(carta):


    jogador = []
    
    
    
    
    if total_jogador > 21:
                    print('Você estourou... uma pena')
                    print('Pontos do jogador: {0}'.format(total_jogador))
                    break

                elif total_jogador == total_croupier:
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos do jogador: {0}".format(total_jogador))
                    print("Houve um empate")
                    print("Seu saldo é de: {0}".format(dinheiro_jogador))
                    
                    
                elif total_croupier > total_jogador:
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos do jogador: {0}".format(total_jogador))
                    print("O Croupier venceu... você perdeu essa")
                    print("Seu saldo é de: {0}".format(dinheiro_jogador))
                else:
                    print("Pontos do Croupier: {0}".format(total_croupier))
                    print("Pontos do jogador: {0}".format(total_jogador))
                    print("Você ganhou")
                    print("Seu saldo é de: {0}".format(dinheiro_jogador))