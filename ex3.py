#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a
#tabuada de 1 a 10 do valor lido.

n = int(input('Digite um numero de 1 a 10: '))
while n > 10 or n < 1:
    print('numero inválido')
    n = int(input('Digite um numero de 1 a 10: '))
for c in range(1, 11):
    print('{:2} x {} = {}'.format(n, c, (c * n)))