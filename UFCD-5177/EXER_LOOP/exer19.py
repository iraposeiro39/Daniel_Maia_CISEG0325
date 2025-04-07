#!/bin/python3
# Exercícios 19:Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
# 1, 1, 2, 3, 5, 8, 13, 21.
# Como se constrói.
# 1+1=2
#     1+2=3
#         2+3=5
num1 = 1
num2 = 1
num3 = 0
contador = 1
while True:
    num3 = num1 + num2
    print(f"nº{contador} -> {num1} + {num2} = {num3}")
    num1 = num2
    num2 = num3
    contador += 1
    if contador > 60:
        break
