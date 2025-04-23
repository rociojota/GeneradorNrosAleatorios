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
    while True:
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


    """valores = [
    0.792, 0.396, 0.01, 0.158, 0.178, 0.248, 0.99, 0.089, 0.436, 0.149,
    0.644, 0.376, 0.941, 0.416, 0.079, 0.901, 0.277, 0.594, 0.703, 0.248,
    0.426, 0.218, 0.96, 0.594, 0.188, 0.584, 0.168, 0.713, 0.119, 0.04
    ]
    z_alpha=1.5"""
    prueba_promedios(valores, z_alpha)

if __name__ == "__main__":
    main()
