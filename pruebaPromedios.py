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
    """nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    z_alpha = float(input("Ingrese el valor de z_alpha: "))"""
    valores = [
    0.792, 0.396, 0.01, 0.158, 0.178, 0.248, 0.99, 0.089, 0.436, 0.149,
    0.644, 0.376, 0.941, 0.416, 0.079, 0.901, 0.277, 0.594, 0.703, 0.248,
    0.426, 0.218, 0.96, 0.594, 0.188, 0.584, 0.168, 0.713, 0.119, 0.04
    ]
    z_alpha=1.5
    prueba_promedios(valores, z_alpha)

if __name__ == "__main__":
    main()
