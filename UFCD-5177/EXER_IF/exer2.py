#!/bin/python3
# Exercício 2: Fazer um programa que analise 3 valores inteiros (através das variáveis num1, num2 e num3),
# e informa qual o maior e qual o menor deles.
#
# Vars
num1 = 0
num2 = 0
num3 = 0

# Input
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))
num3 = int(input("Introduza o terceiro número: "))

# MAIOR
if num1 > num2 and num1 > num3:
    print(f"O maior número é o primeiro ({num1})")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é o segundo ({num2})")
else:
    print(f"O maior número é o terceiro ({num3})")

# MENOR
if num1 < num2 and num1 < num3:
    print(f"O menor número é o primeiro ({num1})")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é o segundo ({num2})")
else:
    print(f"O menor número é o terceiro ({num3})")
