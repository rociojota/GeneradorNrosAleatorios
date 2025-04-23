import math


def metodo_lehmer(seed, t, k, cantidad):
    resultados = []
    n_actual = seed

    for _ in range(cantidad):
        producto = n_actual * t #producto de la semilla por t
        producto = n_actual * t
        producto_str = str(producto).zfill(len(str(seed)))  
        primeros_k_digitos = producto_str[:k]  # Tomar los primeros k dígitos
        resto_derecha = producto_str[k:]  # Tomar el resto de la cadena
        n_actual = int(resto_derecha) - int(primeros_k_digitos)
        u_i = n_actual / (10 ** len(str(n_actual)))  
        resultados.append(u_i)

    return resultados


def main():
    print("Generador Pseudoaleatorio - Método de Lehmer por Dígitos")
    seed = int(input("Ingrese la semilla (n₀): "))
    t = int(input("Ingrese el número t: "))
    k = len(str(t))
    cantidad = int(input("¿Cuántos números desea generar?: "))

    resultados = metodo_lehmer(seed, t, k, cantidad)

    print("\nNúmeros pseudoaleatorios generados:")
    for i, r in enumerate(resultados):
        print(f"{i + 1}: {r:.5f}")


if __name__ == "__main__":
    main()