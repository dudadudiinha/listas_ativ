#1004
num1 = int(input('Digite um número: ')) 
num2 = int(input('Digite um número: ')) 
print(f'Produto = {num1*num2}')

#1005
n1 = float(input('Digite sua nota no primeiro bimestre: '))
n2 = float(input('Digite sua nota no segundo bimestre: '))
print(f'Média = {(n1*3.5+n2*7.5)/11:.5f}')

#1011
raio = int(input('Digite o valor do raio da esfera: '))
print(f'Volume = {(4.0/3)*3.14159*raio**3:.3f}')

#2416
numbs1 = input('Digite dois números: ').split()
c = int(numbs1[0])
n = int(numbs1[1])
print(f'{c%n:.0f}')

#1015
nums1 = input('Digite dois números: ').split()
x1 = float(nums1[0])
y1 = float(nums1[1])
nums2 = input('Digite dois números: ').split()
x2 = float(nums2[0])
y2 = float(nums2[1])
print(f'{((x2-x1)**2+(y2-y1)**2)**(1/2):.4f}')

#1930
Ts = input('Digite quatro números: ').split()
t1 = int(Ts[0])
t2 = int(Ts[1])
t3 = int(Ts[2])
t4 = int(Ts[3])
print(f'{(t1+t2+t3+t4)-3:.0f}')