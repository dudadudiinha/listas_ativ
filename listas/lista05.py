#1
def maior(x,y):
    return max(x,y)
x=int(input('Digite um número: '))
y=int(input('Digite um número: '))
print(maior(x,y))

#2
def maior(x,y,z):
    return max(x,y,z)
x=int(input('Digite um número: '))
y=int(input('Digite um número: '))
z=int(input('Digite um número: '))
print(maior(x,y,z))

#3
def iniciais(nome):
    partes = nome.split()
    letras = ""
    for parte in partes:
        letras += parte[0].upper()
    return iniciais
nome=input('Digite seu nome completo: ')
print(iniciais(nome))

#4
def aprovado(nota1,nota2):
    media=(nota1+nota2)/2
    if media>=60:
        return True
    else:
        return False
nota1=int(input('Digite sua nota no primeiro bimestre: '))
nota2=int(input('Digite sua nota no segundo bimestre: '))
print(aprovado(nota1, nota2))

#5
def formatar_nome(nome):
    return nome.title()
nome=input('Digite seu nome completo: ')
print(formatar_nome(nome))