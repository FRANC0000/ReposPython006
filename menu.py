#menu de opciones
#crear menu con tres opciones

import os
seguir=True

def numeros():
    #ingresar n numeros
    #mostar cantidad de: n.positivos, n.negativos, n=0
    
    mayor=0
    menor=0
    igual=0

    cantidad=int(input("ingrese cantidad de números a ingresar: "))

    for i in range (cantidad):
        n=int(input(str(i+1)+".- Ingresa un número "))

        if (n>0):
            mayor+=1
        elif (n<0):
            menor+=1
        else:
            igual+=1
    
    print("cantidad de números positivos: "+str(mayor))
    print("cantidad de números negativos: "+str(menor))
    print("cantidad de 0: "+str(igual))

    pausa=input("Presione enter.")


def personas():
    #ingresar para n personas nombre y edad
    #mostrar promedio de todas las edades

    sumita=0
    contadorcito=0

    n=int(input("cantidad de personas a ingresar: "))

    for i in range (n):
        nombre=input("ingrese nombre: ")
        edad=int(input("ingrese edad: "))
        contadorcito+=1    
        sumita+=edad

    print("promedio de las edades: "+str(sumita/contadorcito))

    pausa=input("Presione enter.")


while (seguir):
    os.system('cls')
    print("1. Números ")
    print("2. Datos Personales ")
    print("3. Finalizar")

    op=int(input("Digite una opción 1, 2, 3: "))

    if (op==1):
        numeros()
    if (op==2):
        personas()
    if  (op==3):
        print("Finalizando programa...")
        pausa=input("Enter para continuar.")
        break

