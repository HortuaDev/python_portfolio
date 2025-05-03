
def palindromo():
    print(".:Palindromo:.")
    texto = input("Ingresa un texto: ")
    
    contador = len(texto)-1
    validador_palindromo = True
    
    
    for letra in texto:
        
        if letra != texto[contador]:
            validador_palindromo=False
                
        contador-=1    
        
    if validador_palindromo:    
        print(f"La palabra {texto} es Palindromo")           
    else:
        print(f"La palabra {texto} NO es Palindromo")           
        

if __name__ == "__main__":
    palindromo()
    print("Programa finalizado")