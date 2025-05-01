
def fibonacci():
    print(".:Fibonacci:.")
    numero = int(input("Ingresa un numero: "))

    a = 0
    b = 1

    for num in range(numero):
        print(a)
        a, b = b, a + b
        
        
if __name__ == "__main__":
    fibonacci()
    print("Programa finalizado")