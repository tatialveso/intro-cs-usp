n = int(input("Digite o valor de um número inteiro e positivo: "))

if (n > 1):
    for i in range(2, n):
        if(n % i) == 0:
            print("não é primo")
    else:
        print("primo")
else:
    print("não é primo")