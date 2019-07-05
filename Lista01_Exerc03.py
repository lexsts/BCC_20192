# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:49:55 2019

@author: alex / isa
"""

import matplotlib.pyplot as plt

#Inicializa as listas
tempo=arange(1,7,1)
bacterias_inicial = 1000
bacterias_final= bacterias_inicial*4^(arange(1,7,1))


#Plota as linhas no grafico
plt.plot(tempo, bacterias_final)

#Insere titulo
plt.title("Bacterias VS Tempo")
plt.xlabel("Tempo")
plt.ylabel("Bacterias")

#Mostra o grafico
plt.show()
