#Ler 10 números e imprimir quantos são pares e quantos são ímpares.
cont = 0
cont2 = 0
for c in range(1, 11):
    n = int(input('digite 10 numeros: '))
    if n%2 == 0:
        cont += 1
    else:
        cont2 += 1
print(f'numero de pares {cont} numero de impares {cont2}')
