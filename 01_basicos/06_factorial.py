
def factorial():
    
    print("\n.:Factorial de un numero:.")
    numero = int(input("Ingresa un numero: "))
    
    contador = 1
    texto = ""
    
    for num in range(numero):
        
        contador *= num+1
        
        if((num+1)==1):
            texto += f"\n[{num+1} x"
        elif((num+1)<numero):
            texto += f" {num+1} x"
        elif((num+1)==numero):
            texto += f" {num+1}] = {contador}"
            
    print(texto)        
        



if __name__ == "__main__":
    factorial()
    print("\nPrograma finalizado")