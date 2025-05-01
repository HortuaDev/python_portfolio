def par_impar():
    print(".: Par Impar :.")
    
    numero = int(input("Ingresa un numero: "))
    
    if numero % 2 == 0:
        print(f"Numero [{numero}] Par")
    else:
        print(f"Numero [{numero}] Impar")
    

if __name__=="__main__":
    par_impar()
    print("Programa finalizado")