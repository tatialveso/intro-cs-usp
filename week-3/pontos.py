import math

firstX = int(input("Digite um número para a coordenada X do primeiro ponto: "))
firstY = int(input("Digite um número para a coordenada Y do primeiro ponto: "))

secondX = int(input("Digite um número para a coordenada X do segundo ponto: "))
secondY = int(input("Digite um número para a coordenada Y do segundo ponto: "))

distanceX = firstX - secondX
x = (distanceX ** 2)

distanceY = firstY - secondY
y = (distanceY ** 2)

distanceSqrt = x + y

distance = math.sqrt(distanceSqrt)

if distance >= 10:
    print("longe")
else:
    print("perto")