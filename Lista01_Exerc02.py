# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:33:01 2019

@author: alex / isa
"""
import matplotlib.pyplot as plt

#Inicializa as listas
unidades = arange(-1000,5001,1)
receita=(6000*(arange(-1000,5001,1))-((arange(-1000,5001,1))**2)) #calculo da receita
custo=((arange(-1000,5001,1))**2)-(2000*(arange(-1000,5001,1))) #calculo do custo

#Plota as linhas no grafico
plt.plot(unidades, receita)
plt.plot(unidades, custo)

#Insere titulo
plt.title("Receita VS Custo")
plt.xlabel("Unidades")
plt.ylabel("Valores")

#Mostra o grafico
plt.show()
