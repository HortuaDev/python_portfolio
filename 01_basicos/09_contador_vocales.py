
def contador_vocales():
    print(".:Contador de vocales:.")
    texto = input("Ingresa un texto: ")
    
    vocales = ['a','e','i','o','u']
    contador = 0
    
    for letra in texto:
        
        if letra in vocales:
            contador+=1

    print(f'Total de vocales: [{contador}]')

if __name__ == "__main__":
    contador_vocales()
    
    print("Programa finalizado")