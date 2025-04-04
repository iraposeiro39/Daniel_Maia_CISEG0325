#!/bin/python3
# Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média.
notas = []
for i in range(10):
    nota = float(input(f"Insira a nota nº{i+1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f"A media das notas é: {media:.2f}")
