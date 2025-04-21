from generador import randomGenerate

def obtener_semilla():
    while True:
        entrada = input("Ingresa una semilla (o presiona Enter para usar la hora del sistema): ")
        if entrada == "":
            return None  # hora del sistema si no se ingresa ninguna semilla
        try:
            semilla = int(entrada)  # validar que la entrada sea un número 
            return semilla
        except ValueError:
            print("Por favor ingresa un número válido.")

def main():
    semilla = obtener_semilla()
    generador = randomGenerate(semilla)
    
    print("Números pseudoaleatorios: ")
    for _ in range(100): #cantidad a imprimir
        print(generador.siguiente())


#pruebas futuras


if __name__ == "__main__":
    main()
