#Leia várias idades e calcule a média entre as idades (usar uma variável
#para idade).
som = 0
cont = 0
op = 0

while op != 'N':

    idade = int(input("digite sua idade: "))
    op = str(input('voce deseja digitar outra idade:[S/N]: ')).strip().upper()[0]
    som += idade
    cont += 1
print(f'foram digitadas {cont} idades, a soma de todas as idades é {som} a media das idade é {som / cont}')




