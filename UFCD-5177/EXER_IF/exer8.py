#!/bin/python3
# Exercício 8: Crie um programa que leia a nota de 10 alunos, calcule a média e mostre essa média
# e mostre também quantos alunos ficaram com a sua nota igual ou acima da média. (NOTAS de 0 a 20).
#
# Input
lista_notas = []
for i in range(10):
    nota = float(input(f"Insira a nota nº{i+1}: "))
    lista_notas.append(nota)

# Logica
media = sum(lista_notas) / len(lista_notas)

notas_acima_igual=[]
notas_abaixo=[]

for i in lista_notas:
    if i >= media:
        notas_acima_igual.append(i)
    if i < media:
        notas_abaixo.append(i)

# Output
print(f"A media das notas é: {media:.2f}")
print(f"Quantidade de alunos com a nota igual ou acima da média: {len(notas_acima_igual)}")
print(f"Quantidade de alunos com a nota abaixo da média: {len(notas_abaixo)}")
