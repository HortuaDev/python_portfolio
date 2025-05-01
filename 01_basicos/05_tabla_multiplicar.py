def tabla_multiplicar():
    
    print(".:Tabla de multiplicar:.")
    numero = int(input("Ingresa un numero: "))
    
    print(f".:Tabla del [{numero}]:.")
    for num in range(10):
        print(f"{numero} X {num+1} = [{numero*(num+1)}]")
        

if __name__ == "__main__":
    tabla_multiplicar()
    print("Programa finalizado")