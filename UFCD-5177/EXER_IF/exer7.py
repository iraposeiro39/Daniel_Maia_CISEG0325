#!/bin/python3
# Exercício 7: O sistema de avaliação de determinada disciplina, é composto por três provas Nota (0 a 10).
# A primeira prova tem peso 2, a Segunda tem peso 3 e a terceira prova tem peso 5.
# Faça um algoritmo para calcular a média final de um aluno desta disciplina e se a média for maior
# ou igual a 6, mostrar APROVADO, senão, mostrar REPROVADO.
#
# Input
name = input("Insira o nome do aluno: ")
prova1 = float(input("Insira o valor da prova nº1 (0-10): "))
prova2 = float(input("Insira o valor da prova nº2 (0-10): "))
prova3 = float(input("Insira o valor da prova nº3 (0-10): "))

# Logica
var1 = prova1 * 0.2
var2 = prova2 * 0.3
var3 = prova3 * 0.5
nota_final = var1+var2+var3

# Output
print(f"Nome do aluno: {name}")
print(f"Nota Final: {nota_final}")
print("Situação final:")
if nota_final >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
