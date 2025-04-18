'''#1036
digitos = input('Digite três números: ').split()
a = float(digitos[0])
b = float(digitos[1])
c = float(digitos[2])
delta = b**2-(4*a*c)
if delta < 0 or a == 0:
    print('Impossível calcular')
else:
    r1 = (-b+(delta)**(1/2))/(2*a)
    r2 = (-b-(delta)**(1/2))/(2*a)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')


#1044
nume = input('Digite dois números: ').split()
n1 = float(nume[0])
n2 = float(nume[1])
if n1%n2 == 0 or n2%n1 == 0:
    print('São múltiplos')
else:
    print('Não são múltiplos')'''

#1049


#1050

'''#2424
numbers = input('Digite as coordenadas em que a bola bateu: ').split()
x = int(numbers[0])
y = int(numbers[1])
if 0 <= x <= 432 and 0 <= y <= 468:
    print('Dentro')
else:
    print('Fora')

#2670
a1 = int(input('Digite o número de pessoas no primeiro piso: '))
a2 = int(input('Digite o número de pessoas no segundo piso: '))
a3 = int(input('Digite o número de pessoas no terceiro piso: '))
primeiro_andar = a3*4 + a2*2
segundo_andar = a3*2 + a1*2
terceiro_andar = a1*4 + a2*2
print(f'{min(primeiro_andar, segundo_andar, terceiro_andar)} minutos')'''

#1059

#1151