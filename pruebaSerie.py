import math

def prueba_serie(numeros, z_alpha, x):
    n = len(numeros)
    n_2 = int(n/2)
    if n % 2 != 0:
        print("❌ La cantidad de números debe ser para realizar la prueba.")
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
    nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    z_alpha = float(input("Ingrese el valor de z_alpha: "))
    x= int(input("Ingrese el valor de x: "))
    """valores = [0.01,0.079,0.168,0.858,0.901,0.74,0.713,0.478,0.277,0.019,0.548,0.426]
    z_alpha = 0.675
    x=2"""
    prueba_serie(valores, z_alpha, x)

if __name__ == "__main__":
    main()
