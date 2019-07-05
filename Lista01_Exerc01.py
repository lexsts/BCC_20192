# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:10:31 2019

@author: alex / isa
"""

#Inicializa as listas
from numpy import arange
segundos = arange(-1,6,0.1)
altura=-(arange(-1,6,0.1))**2+4*(arange(-1,6,0.1))+6 
   
#Monta o gráfico   
from matplotlib.pyplot import plot #importar a função plot da bliblioteca matplotlib
plot(segundos, altura)
