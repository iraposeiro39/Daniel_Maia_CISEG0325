#!/bin/python3
# Init vars
lista = []

# Classes
class Carros:
    def __init__(self,marca,modelo,ano,vel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.vel = vel

    def Acelerar(self,nivel):
        if nivel == 1:
            self.vel += 10
        if nivel == 2:
            self.vel += 15
        if nivel == 3:
            self.vel += 20

    def Travar(self,nivel):
        if nivel == 1:
            self.vel -= 10
        if nivel == 2:
            self.vel -= 15
        if nivel == 3:
            self.vel -= 20


Carro1 = Carros("Opel","Astra",1994,0)

print(f"Velocidade: {Carro1.vel}")
Carro1.Acelerar(1)
print(f"Velocidade: {Carro1.vel}")
Carro1.Acelerar(2)
print(f"Velocidade: {Carro1.vel}")
print("MULHER NO TRANSITO!!!")
Carro1.Travar(3)
print(f"Velocidade: {Carro1.vel}")


# ### Stand
# num = int(input("Insira o número de carros: "))

# for i in range(num):
#     print(f"== Carro nº{i} ==")
#     w = input("Insira a marca: ")
#     x = input("Insira o modelo: ")
#     y = int(input("Insira o ano: "))
#     carro = Carros(w, x, y, 0)
#     lista.append(carro)

# for i in range(len(lista)):
#     print(f"\n== Carro nº{i} ==")
#     print(f"Marca: {lista[i].marca}")
#     print(f"Modelo: {lista[i].modelo}")
#     print(f"Ano: {lista[i].ano}")
