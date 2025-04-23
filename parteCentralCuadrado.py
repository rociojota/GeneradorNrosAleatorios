

def metodo_parte_central_cuadrado(seed, n_digitos, cantidad):
    resultados = []
    m_actual = seed

    for _ in range(cantidad):
        x = m_actual ** 2
        x_str = str(x)

        # Asegurarse de que X tiene al menos N dígitos
        if len(x_str) < n_digitos:
            x_str = x_str.zfill(n_digitos)

        diferencia = len(x_str) - n_digitos

        # Si la diferencia es impar, multiplicamos X por 10
        if diferencia % 2 != 0:
            x = int(x_str) * 10
            x_str = str(x)

        # Si aún tiene menos de N dígitos, rellenar con ceros
        if len(x_str) < n_digitos:
            x_str = x_str.zfill(n_digitos)

        # Obtener los N dígitos centrales
        total_digitos = len(x_str)
        inicio = (total_digitos - n_digitos) // 2
        digitos_central = x_str[inicio:inicio + n_digitos]

        m_actual = int(digitos_central)
        u_i = m_actual / (10 ** n_digitos)
        resultados.append(u_i)

    return resultados

def main():
    print("Generador Pseudoaleatorio - Método de la Parte Central del Cuadrado")
    seed = int(input("Ingrese la semilla (M): "))
    n_digitos = int(input("Ingrese el número de dígitos deseados (N): "))
    cantidad = int(input("¿Cuántos números desea generar?: "))

    resultados = metodo_parte_central_cuadrado(seed, n_digitos, cantidad)

    print("\nNúmeros pseudoaleatorios generados:")
    for i, r in enumerate(resultados):
        print(f"{i + 1}: {r:.5f}")


if __name__ == "__main__":
    main()
