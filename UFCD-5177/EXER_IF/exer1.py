#!/bin/python
# Exercício 1: Desenvolva um programa que assuma uma entrada em Segundos
# e transforme em Horas, Minutos e Segundos.
#
# Input
seg = int(input("Insira os segundos que deseja calcular: "))

# Calculos
min = seg / 60
hora = min / 60

# Output
print(f"Horas: {hora:.2f}")
print(f"Minutos: {min:.2f}")
print(f"Segundos: {seg}")
