#!/bin/python3
# Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255)
# e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa.
# 
for i in range(0, 256):
    print(f"Num: {i} -> ASCII: {chr(i)!r}")
    if i % 20 == 0 and i != 0:
        opt = input("\nQueres Continuar(return) ou queres sair(s)?: \n")
        if opt.lower() == "s":
            break
