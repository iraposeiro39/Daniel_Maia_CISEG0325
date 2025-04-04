#!/bin/python3
# Exercício 6: Uma loja oferece para os seus clientes, um determinado desconto de acordo com o valor da compra efetuada.
# O desconto é de 10%, se o valor da compra for até 200.00€, 15% se for maior que 200€ e menor
# ou igual a  500,00E e 20% se for acima de 500,00€. Crie um algoritmo que leia o nome do cliente e o valor da compra.
# Mostre ao final o nome do cliente, o valor da compra,o percentual de desconto
# e o seu valor, e o valor total a pagar deste cliente. (só fazer duas Contas)
#
# 10% desconto < 200€
# 15% desconto >= 200 and <= 500
# 20% desconto > 500€
#
# Input
name = input("Insira o seu nome: ")
value = int(input("Insira o valor da compra: "))

# Logica
desc = 0
if value < 200:
    desc = 0.1
elif value >= 200 and value <= 500:
    desc = 0.15
elif value > 500:
    desc = 0.2

desc_value = value * desc

# Output
print(f"Nome: {name}")
print(f"Percentagem de desconto: {desc * 100}%")
print(f"Valor original: {value}€")
print(f"Valor com desconto: {value - desc_value}€")
