

def mayor_de_tres():

    numero_1 = int(input("Ingresa el primer numero: "))
    numero_2 = int(input("Ingresa el segundo numero: "))
    numero_3 = int(input("Ingresa el tercer numero: "))
    
    numeros = [numero_1,numero_2,numero_3]
    
    numero_maximo = 0
    
    for num in numeros:
        
       if num > numero_maximo:
           numero_maximo = num
    
    print(f"El numero mayor es :{numero_maximo}")



if __name__ == "__main__":
    mayor_de_tres()
    print("Programa finalizado")