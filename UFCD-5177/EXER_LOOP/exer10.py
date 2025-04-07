#!/bin/python3
# Exercício 10: Elabore um programa que lê um número e escreve quantos divisores ele possui.
#
divisores = []
num = int(input("Insira um número: "))

for i in range(1,num+1):
    if num % i == 0:
        divisores.append(i)

print(f"O número {num} possui {len(divisores)} divisores: {divisores}")
