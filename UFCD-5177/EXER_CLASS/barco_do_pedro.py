#!/bin/python3
class Barco:
    def __init__(self, tipo, tamanho, vel, angulo):
        self.tipo = tipo
        self.tamanho = tamanho
        self.angulo = angulo
        self.vel = vel

    def Rumo(self, graus):
        print(f"Ângulo atual: {self.angulo}°")
        if -360 <= graus <= 360:
            self.angulo = (self.angulo + graus) % 360
            print(f"Novo Ângulo: {self.angulo}°")
        else:
            print("Ângulo inválido.")

    def Acelera(self, manete):
        if manete == 1:
            self.vel += 5
        elif manete == 2:
            self.vel += 10
        elif manete == 3:
            self.vel += 15
        else:
            print("Manete inválido.")

    def Desacelera(self, manete):
        if manete == 1:
            self.vel -= 5
        elif manete == 2:
            self.vel -= 10
        elif manete == 3:
            self.vel -= 15
        else:
            print("Manete inválido.")

# Execução principal
Barco1 = Barco("Lancha", "12m", 0, 0)

print("Pronto para arrancar?")
print(f"Ângulo: {Barco1.angulo}°, Velocidade: {Barco1.vel} nós")
input("Pressione Enter para arrancar:")


while True:
    acao = input("\nDeseja acelerar, virar ou sair? (acelerar/virar/sair): ").strip().lower()

    if acao == "acelerar":
        manete = int(input("Qual é a posição da manete? (1, 2 ou 3): "))
        Barco1.Acelera(manete)

    elif acao == "virar":
        graus = int(input("Digite o ângulo de viragem (-360 a 360): "))
        Barco1.Rumo(graus)

    elif acao == "sair":
        print("Encerrando o sistema do barco...")
        break

    else:
        print("Ação inválida. Tente novamente.")

    print(f"Estado atual -> Ângulo: {Barco1.angulo}°, Velocidade: {Barco1.vel} km/h")
