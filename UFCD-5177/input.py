#!/bin/python3
# INPUT
#
# Tipo de dados primarios
# int -> 0 ... 9 ex: 098172639081263091263091
# float -> 1,0 ... 9,0 ex: 3,1416
# bool -> True OR False // 0 OR 1
# str -> "Hello World! 9312919231"
#
# Variaveis
num1 = 0
num2 = 0
total = 0
# Inputs
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
# Conta e output
total = num1/num2
print(f"A  divisão dos dois é: {total}")
