#Faça um algoritmo que leia 10 números inteiros, armazene-os em uma
#lista e imprima em ordem crescente.
listanum = []
cont = 0
for i in range(0, 10):
    num = int(input('digite um numero: '))
    listanum.append(num)
    cont += 1

listanum.sort()
print(listanum)