#!/bin/python3
# Exercício 3: Crie 2 variáveis (num1 e num2) e leia o valor para cada um deles.
# Mostre os valores de forma crescente e decrescente.
#
# Input
num1 = int(input("Insira um valor para o numero 1: "))
num2 = int(input("Insira um valor para o numero 2: "))

# Logica
if num1 > num2:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")
elif num1 < num2:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print("Os numeros são iguais!")
