def ingreso_numeros():
    numero_1 = int(input("Ingresa el numero 1: "))
    numero_2 = int(input("Ingresa el numero 2: "))

    return [numero_1,numero_2]
 
 
def calculadora():
    verificador = False

    while verificador==False:
        print(".:MENU:.")
        print("[1] Sumar")
        print("[2] Restar")
        print("[3] Multiplicar")
        print("[4] Dividir")
        print("[0] Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if(opcion.__eq__("1")):
            numeros = ingreso_numeros()
            print(f"El resultado es: {numeros[0]+numeros[1]}")

        elif(opcion.__eq__("2")):
            numeros = ingreso_numeros()
            print(f"El resultado es: {numeros[0]-numeros[1]}")
            
        elif(opcion.__eq__("3")):
            numeros = ingreso_numeros()
            print(f"El resultado es: {numeros[0]*numeros[1]}")
                    
        elif(opcion.__eq__("4")):
            numeros = ingreso_numeros()
            print(f"El resultado es: {numeros[0]/numeros[1]}")
            
        elif(opcion.__eq__("0")):  
            verificador = True    
        else:
            print("Opcion invalida, si quieres salir presiona 0 [cero]")

if __name__=="__main__":
    calculadora()
    
    print("Programa terminado")

