#Faça um algoritmo que leia um número positivo e imprima seus
#divisores.

divisor = 1
n = int(input('digite um numero inteiro positivo: '))
for divisor in range(divisor, n):
    if n % divisor == 0:
        print(n)
