#Utilizando a estrutura de repetição for, faça um programa que receba 10
#números e conte quantos deles estão no intervalo [10,20] e quantos
#deles estão fora do intervalo.


cont1 = 0
cont2 = 0
for c in range(1, 11):
    n = int(input('digite 10 numeros: '))
    if n >= 10 and n <= 20:
        cont1 += 1
    else:
        cont2 += 1
print(f'foram digitados {cont1} numero no intervalo de 10 a 20, e {cont2} fora desse intervalo')
