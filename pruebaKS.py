import math

def prueba_ks(numeros, d):
    n_ordenados = sorted(numeros)
    
    #Distribución acumulada para cada número
    distribucion_acumulada = []
    for i in range(len(numeros)):
        distribucion_acumulada.append((i + 1) / len(numeros))

    #Calcular el estadístico ks
    diferencia = []
    for i in range(len(numeros)):
        diferencia.append(round(abs(distribucion_acumulada[i] - n_ordenados[i]), 3))
    d_n = max(diferencia)

    print(f"Dn: {d_n}")
    if abs(d_n) < d:
        print("✅ La secuencia pasa la prueba de KS.")
    else:
        print("❌ La secuencia NO pasa la prueba de KS.")
        


def main():
    valores = []
    print("\nPrueba de K-S:")
    print("--------------------------------------------------")
    #nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    """for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    d = float(input("Ingrese el valor del estadístico: "))"""
    valores = [0.01,0.079,0.168,0.858,0.901,0.74,0.713,0.478,0.277,0.019,0.548,0.426]
    d=0.375
    prueba_ks(valores, d)

if __name__ == "__main__":
    main()
