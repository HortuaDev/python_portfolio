
def buscador_elementos():
    
    print(".:Busqueda de elementos:.")
    
    
    lista = []
    
    for _ in range(5):
        
        numero = int(input("Ingresa un numero: "))
        
        lista.append(numero)
        
    numero_busqueda = int(input("Ingresa el numero de busqueda: "))
    
    validador = False
    
    for i in lista:
        
        if i == numero_busqueda:        
            validador = True
            

    if validador:
        print("Numero coincide")
    else:
        print("Numero no coincide")    

if __name__ == "__main__":
    buscador_elementos()
    print("Programa finalizado")