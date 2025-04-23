import math

def prueba_promedios(numeros, z_alpha):
    n = len(numeros)
    media = sum(numeros) / n
    z_cero = ((media-0.5)*math.sqrt(n))/math.sqrt(1/12)
    print(f"Media = {media:.4f}, z₀ = {z_cero:.4f}")
    if abs(z_cero) < z_alpha:
        print("✅ La secuencia pasa la prueba de los promedios.")
    else:
        print("❌ La secuencia NO pasa la prueba de los promedios.")

def main():
    valores = []
    print("\nPrueba de los promedios:")
    print("--------------------------------------------------")
    nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    z_alpha = float(input("Ingrese el valor de z_alpha: "))
    prueba_promedios(valores, z_alpha)

if __name__ == "__main__":
    main()
