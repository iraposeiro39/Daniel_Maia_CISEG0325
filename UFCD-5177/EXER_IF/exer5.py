#!/bin/python3
# Ler 3 valores INTEIROS para as variáveis Num1, Num2, Num3.
# Apresentar os valores dispostos em ordem crescente e decrescente.
#
# Input
num1 = int(input("Insira um valor para o numero 1: "))
num2 = int(input("Insira um valor para o numero 2: "))
num3 = int(input("Insira um valor para o numero 3: "))

# Logica
maior = 0
meio = 0
menor = 0
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Nao podes ter numeros repetidos!")
else:
    if num1 > num2 and num1 > num3:
        if num2 > num3 and num2 < num1:
            maior = num1
            meio = num2
            menor = num3
        elif num3 > num2 and num3 < num1:
            maior = num1
            meio = num3
            menor = num2

    elif num2 > num3 and num2 > num1:
        if num1 > num3 and num1 < num2:
            maior = num2
            meio = num1
            menor = num3
        elif num3 > num1 and num3 < num2:
            maior = num2
            meio = num3
            menor = num1

    elif num3 > num1 and num3 > num2:
        if num1 > num2 and num1 < num3:
            maior = num3
            meio = num1
            menor = num2
        elif num2 > num1 and num2 < num3:
            maior = num3
            meio = num2
            menor = num1

# Output
    print(f"Crescente: {menor}, {meio}, {maior}")
    print(f"Decrescente: {maior}. {meio}, {menor}")
