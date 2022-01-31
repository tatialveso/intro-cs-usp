import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
	raizUm = (-b + math.sqrt(delta)) / (2 * a)

	print("a raiz desta equação é", raizUm)
else: 
	if delta < 0:
		print("esta equação não possui raízes reais")
	else:
		raizUm = (-b + math.sqrt(delta)) / (2 * a)
		raizDois = (-b - math.sqrt(delta)) / (2 * a)

		print("as raízes da equação são", raizUm, "e", raizDois)