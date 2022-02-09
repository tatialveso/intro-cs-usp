number = int(input("Digite um número inteiro: "))

sum = 0

while (number != 0):
    rest = number % 10
    number = (number - rest) // 10
    sum = sum + rest

print(sum)