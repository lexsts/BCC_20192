# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""O valor das variaveis pode ser alterado a qualquer momento"""
print("<<< O valor das variaveis pode ser alterado a qualquer momento >>>")
var = 134 # valor inteiro
print(var)
var = 4.2 # valor decimal
print(var)
var = "hello world" # texto
print(var)

"""O nome das variaveis pode conter letras, numeros, simbolo underline mas não pode começar com número"""
print("<<< O nome das variaveis pode conter letras, numeros, simbolo underline mas não pode começar com número >>>")
numero = -5
print(numero)

nome_professor = "Thiago"
print("O nome do professor e'", nome_professor)

Valor1 = 12.4
print(Valor1)
Valor2 = 56
print(Valor2)


"""Erros que podem ocorrer"""
#3invalido = 4 >>essa linha gera erro de sintaxe SyntaxError: invalid syntax

#nome_professor = "Thiago Ferreira Covões"
#print(nome_profesor)  >>essa linha gera erro porque o nome da variavel está errado (falta um s)

#sala_do_prof = "517-2"
#print("A sala do professor é", Sala_do_prof) >>essa linha gera erro porque o nome da variavel está errado (é case sensitive)


"""Operações numéricas - O Python executa as operações na seguinte ordem: **, *, /, //, %, + e -"""
print("<<< Operações numéricas - O Python executa as operações na seguinte ordem: **, *, /, //, %, + e - >>>")
print(4 + 67)
print(9 - 4)
print(3 * 2) 
print(19 / 5) # o símbolo "/" indica divisão exata 
print(19 // 5) # o símbolo "//" indica divisão inteira 
print(3**2) # o símbolo "**" indica exponenciação
print(4 + 3 * 5 - 8 + 2**3 / 4)

expressao = 2 ** 3 - 1 + 2 * 100 #atribuindo o resultado da operação matematica
print(expressao) #mostrando o resultado da operação matematica

print(0.1 + 0.1)
print(0.54 * 4)
print(0.1 + 0.2) #operação com números de ponto flutuante apresentam um comportamento esperado que será explicado posteriormente


"""Strings"""
print("<<< Strings >>>")
uma_string = "essa é uma string válida"
print(uma_string)
outra_string = "Essa também, mesmo contendo números (3 5 4) e símbolos (* $ & @ %)"
print(outra_string)


"""Atribuições"""
print("<<< Atribuições >>>")
x = 3
f = 2 * x + 4
print(f)

x = 7
print(x)
x = x + 4
print(x)

resultado = 8
expressao = resultado**2 + 4


C = 55 #graus Celsius
F = C * 9/5 + 32 #Conversão em Fahrenheit
print(F)

b =10
B =20
h =5
area =((b+B)*h)/2 #calculo da area do trapezio
print(area)

#troca de variaveis com perda do primeiro valor da variavel x
x = 4
y = -9
print("O valor de x e'", x, "e o valor de y e'", y)
x = y
print("O valor de x e'", x, "e o valor de y e'", y)

#troca de variaveis
x = 4
y = -9
print("O valor de x e'", x, "e o valor de y e'", y)

# salve na variável "aux" o valor atual de x:
aux = x
# agora atualize o valor de x:
x = y
# o valor de y recebe o antigo valor de x, que está salvo em "aux":
y = aux
print("O valor de x e'", x, "e o valor de y e'", y)


"""Listas"""
print("<<< Listas >>>")
lista = ["primeiro", "segundo", "terceiro"]
print(lista)

aula_bases = ["sexta-feira", 10, "salaX", "Thiago"]

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

print("A aula acontece toda", aula_bases[0], "na sala", aula_bases[2])


print("<<< Listas numéricas >>>")
primeiros_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(primeiros_10)

primeiros_10 = list(range(1,11))
print(primeiros_10)
primeiros_100 = list(range(1,101))
print(primeiros_100)

lista = list(range(6,17))
print(lista)

lista = list(range(7)) #a lista inicia em 0 nesse caso
print(lista)

lista = list(range(6,17,2)) #a lista inicia em 6, seguindo 2 unidades até o limite em 17
print(lista)
lista = list(range(6,17,3)) #a lista inicia em 6, seguindo 3 unidades até o limite em 17
print(lista)


"""Graficos"""
print("<<< Graficos >>>")
intervalo = list(range(-10,11))

from numpy import power #importar a função power da bliblioteca numpy
valor_x_2 = power(intervalo, 2) #a função power faz exponenciação
print(valor_x_2)

from matplotlib.pyplot import plot #importar a função plot da bliblioteca matplotlib
plot(intervalo, valor_x_2)


from numpy import multiply, sin
x = list(range(0,8))
seno_de_x = sin(x)
y = multiply(seno_de_x, 5)
plot(x,y)


from numpy import divide
x = list(range(5,15))
y = divide(10, power(x, 2))
plot(x,y)
