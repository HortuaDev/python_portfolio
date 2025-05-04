
def ordenar_lista():
    print(".:Ordenar listas:.")
    
    lista = []
    print("Lista de 5 espacios")
    
    for _ in range(5):
    
        numero = int(input("Ingresa un numero: "))
    
        lista.append(numero)

    print("Ordenacion...")
    
    for i in range(len(lista)):
        
        for j in range(len(lista)-1):
            
            if lista[j] > lista[j+1]:
                
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                
    print("Lista ordenada: ",lista)    
    
    

if __name__ == "__main__":
    ordenar_lista()
    print("Programa finalizado")