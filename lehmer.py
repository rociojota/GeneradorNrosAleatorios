import math


def metodo_lehmer(seed, t, k, cantidad):
    resultados = []
    n_actual = seed

    for _ in range(cantidad):
        producto = n_actual * t
        producto_str = str(producto).zfill(len(str(seed)) + k)
        primeros_k_digitos = producto_str[:k]
        resto_derecha = producto_str[k:]

        # Verificamos si resto_derecha está vacío
        if resto_derecha == '':
            resto_derecha = '0'  # Rellenamos con un 0 si está vacío

        # Ahora podemos convertir a entero sin problemas
        n_actual = abs(int(resto_derecha) - int(primeros_k_digitos))
        u_i = n_actual / (10 ** len(str(n_actual)))  
        resultados.append(u_i)

    return resultados


def main():
    print("Generador Pseudoaleatorio - Método de Lehmer por Dígitos")
    while True:
        entrada = input("Ingrese la semilla (n₀): ")
        try:
            seed = int(entrada)               
        except ValueError:
            print("❌ Error: La entrada no es un número entero válido.")
            continue                        

        if seed <= 0:                      
            print("❌ El número debe ser un entero positivo.")
            continue                        
        break     

    while True:
        entrada = input("Ingrese el valor de t: ")
        try:
            t = int(entrada)               
        except ValueError:
            print("❌ Error: La entrada no es un número entero válido.")
            continue                        

        if t <= 0:                      
            print("❌ El número debe ser un entero positivo.")
            continue                        
        break                          
    k = len(str(t))
    while True:
        entrada = input("¿Cuántos números desea generar?: ")
        try:
            cantidad = int(entrada)
        except ValueError:
            print("❌ Error: La entrada no es un número entero válido.")
            continue    
        if cantidad <= 0:
            print("❌ El número debe ser un entero positivo.")
            continue
        break
    resultados = metodo_lehmer(seed, t, k, cantidad)

    print("\nNúmeros pseudoaleatorios generados:")
    for i, r in enumerate(resultados):
        print(f"{i + 1}: {r:.5f}")


if __name__ == "__main__":
    main()