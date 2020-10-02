#crear for que permita ingresar 10 numeros.
#mostrar cuantos son pares y cuantos impares

par=0
impar=0

for i in range (10):
    num=int(input("ingresa un número: "))
    if (num%2==0):
        par+=1
    elif (num%2!=0):
        impar+=1

print("pares = "+str(par))
print("impares = "+str(impar))