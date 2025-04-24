import math

def prueba_serie(numeros, z_alpha, x):
    n = len(numeros)
    n_2 = int(n/2)
    if n % 2 != 0:
        print("❌ La cantidad de números debe ser par para realizar la prueba.")
        return
    
    subintervalos = []
    for i in range(0, n, 2):  # avanza de 2 en 2
        inicio = numeros[i]
        fin = numeros[i + 1]
        subintervalos.append((inicio, fin))

     # Inicializar matriz de frecuencias observadas FO[i][j]
    FO = [[0 for _ in range(x)] for _ in range(x)]

    for xi, yi in subintervalos:
        fila = int(xi * x)  # coordenada vertical
        col  = int(yi * x)  # coordenada horizontal

        # Corrección si el valor es 1.0 (que caería fuera del índice)
        fila = min(fila, x - 1)
        col  = min(col, x - 1)

        FO[fila][col] += 1

    print("Matriz de frecuencias observadas:")

    for fila in FO:
        print(fila)

    frecuencia_esperada = n_2 / (x**2)
    print(f"Frecuencia esperada Fe: {frecuencia_esperada:.2f} ")

    # Calcular el estadístico Chi-cuadrado
    chi_cuadrado = 0
    for i in range(x):
        for j in range(x):
            fo = FO[i][j]
            chi_cuadrado += ((fo - frecuencia_esperada) ** 2) * (x**2/n_2)
    print(f"\nChi-cuadrado = {chi_cuadrado:.4f}")

    if abs(chi_cuadrado) < z_alpha:
        print("✅ La secuencia pasa la prueba de la serie.")
    else:
        print("❌ La secuencia NO pasa la prueba de la serie.")

def main():
    valores = []
    print("\nPrueba de la serie:")
    print("--------------------------------------------------")
    """while True:
        entrada = input("¿Cuántos números desea ingresar?: ")
        try:
            nro_valores = int(entrada)               
        except ValueError:
            print("❌ Error: La entrada no es un número entero válido.")
            continue                        
        if nro_valores <= 0.0:                      
            print("❌ El número debe ser un entero positivo.")
            continue                        
        break
    valores = []
    for i in range(nro_valores):
        while True:
            entrada = input(f"Ingrese el número {i + 1}: ")
            try:
                valor = float(entrada)               
            except ValueError:
                print("❌ Error: La entrada no es un número flotante válido.")
                continue                        
            if valor <= 0.0:                      
                print("❌ El número debe ser un flotante positivo.")
                continue                        
            break
        valores.append(valor)
    while True:
        entrada = input("Ingrese el valor de z_alpha: ")
        try:
            z_alpha = float(entrada)               
        except ValueError:
            print("❌ Error: La entrada no es un número flotante válido.")
            continue                        
        if z_alpha <= 0.0:                      
            print("❌ El número debe ser un flotante positivo.")
            continue                        
        break
    while True:
        entrada = input("Ingrese el valor de x: ")
        try:
            x = int(entrada)               
        except ValueError:
            print("❌ Error: La entrada no es un número flotante válido.")
            continue                        
        if x <= 0:                      
            print("❌ El número debe ser un flotante positivo.")
            continue                        
        break """
    valores = [
    0.792, 0.396, 0.01, 0.158, 0.178, 0.248, 0.99, 0.089, 0.436, 0.149, 0.644, 0.376,
    0.941, 0.416, 0.079, 0.901, 0.277, 0.594, 0.703, 0.248, 0.426, 0.218, 0.96, 0.594,
    0.188, 0.584, 0.168, 0.713, 0.119, 0.04, 0.762, 0.792, 0.396, 0.01, 0.158, 0.178,
    0.248, 0.99, 0.089, 0.436, 0.149, 0.644, 0.376, 0.941, 0.366, 0.287, 0.713, 0.05
    ]
    x= 3
    z_alpha= 15.51
    prueba_serie(valores, z_alpha, x)

if __name__ == "__main__":
    main()
