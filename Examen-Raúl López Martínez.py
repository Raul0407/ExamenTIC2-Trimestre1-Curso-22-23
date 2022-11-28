def Menu3(numero3:int, numero4:int):
    return numero3 + numero4
def Interfaz():
    print("1-Sumar")
    print("2-Salir")




#Parte 4
Interfaz()


#Parte 6
numero = 0
numero3 = 0
numero4 = 0
print("Parte 6")
while numero != 2:
    Interfaz()
    try:
        numero = (int)(input("Dime la opción que eliges:\n"))
    except:
        print("La opción tiene que ser un número")
    if numero == 1:
        try:
            numero3 = (int)(input("Dime un número:\n"))
            numero4 = (int)(input("Dime otro número:\n"))
        except:
            print("Tienes que poner un número en ambas variables")
        print("La suma de los numeros es:", Menu3(numero3, numero4))
print("---Programa Finalizado---")