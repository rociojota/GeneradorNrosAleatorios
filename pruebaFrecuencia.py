def prueba_frecuencia(numeros, nro_intervalos, z_alpha):
    n = len(numeros)
    tamaño_subintervalo = 1 / nro_intervalos
    subintervalos = []

    for i in range(nro_intervalos):
        inicio = round(i * tamaño_subintervalo, 2)
        fin = round((i + 1) * tamaño_subintervalo, 2)
        subintervalos.append((inicio, fin))

    frecuencia_esperada = n / nro_intervalos
    print(f"Frecuencia esperada Fe: {frecuencia_esperada:.2f} por intervalo")

    # Agrupar los números en los intervalos para obtener la frecuencia observada
    frecuencias = [0] * len(subintervalos)
    for numero in numeros:
        for i, (inicio, fin) in enumerate(subintervalos):
            # Para evitar que 1.0 se quede fuera, lo incluimos en el último intervalo
            if i == len(subintervalos) - 1:
                if inicio <= numero <= fin:
                    frecuencias[i] += 1
                    break
            else:
                if inicio <= numero < fin:
                    frecuencias[i] += 1
                    break

    # Mostrar resultados
    print("\nFrecuencia observada:")
    for i, ((inicio, fin), frecuencia) in enumerate(zip(subintervalos, frecuencias)):
        print(f"Intervalo {i + 1} ({inicio}, {fin}): {frecuencia} datos")

    #Calcular el estadístico Chi-cuadrado
    chi_cuadrado = 0
    for frecuencia in frecuencias:
        chi_cuadrado += ((frecuencia - frecuencia_esperada) ** 2)*(nro_intervalos/n)
    print(f"\nChi-cuadrado = {chi_cuadrado:.4f}")

    if abs(chi_cuadrado) < z_alpha:
        print("✅ La secuencia pasa la prueba de los promedios.")
    else:
        print("❌ La secuencia NO pasa la prueba de los promedios.")


def main():
    valores = []
    print("\nPrueba de la frecuencia:")
    print("--------------------------------------------------")
    nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    nro_intervalos = int(input("¿Cuántos intervalos desea?: "))
    z_alpha = float(input("Ingrese el valor de z_alpha: "))
    prueba_frecuencia(valores, nro_intervalos, z_alpha)

if __name__ == "__main__":
    main()