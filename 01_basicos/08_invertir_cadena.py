
def invertir_cadena():
    print(".:Invertir cadena:.")
    texto = input("Ingresa un texto: ")
    
    contador = len(texto)-1
    texto_invertido = ""
    
    for _ in texto:
        contador-=1
        texto_invertido+=f'{texto[contador]}'

    print("Texto invertido: ",texto_invertido)


if __name__ == "__main__":
    invertir_cadena()
    
    print("Programa finalizado")