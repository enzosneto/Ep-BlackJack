# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:57:31 2019

@author: enzos
"""
import random
baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*8

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

def total(mao):
    total = 0
    for carta in mao:
	    if carta == "J" or carta == "Q" or carta == "K":
	        total+= 10
	    elif carta == "A":
	        if total >= 11: total+= 1
	    else: total+= 11
    return total
