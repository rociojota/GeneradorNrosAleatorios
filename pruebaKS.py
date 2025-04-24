import math
from colorama import Fore, Style, init
init(autoreset=True)

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

    print(Style.BRIGHT + f"Dn: {d_n}")
    if abs(d_n) < d:
        print(Fore.GREEN + Style.BRIGHT +"✅ La secuencia pasa la prueba de KS.")
    else:
        print(Fore.RED + Style.BRIGHT +"❌ La secuencia NO pasa la prueba de KS.")
        


def main():
    valores = []
    print("\nPrueba de K-S:")
    print("--------------------------------------------------")
    #nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    """for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    d = float(input("Ingrese el valor del estadístico: "))"""
    valores = [
    0.792, 0.396, 0.01, 0.158, 0.178, 0.248, 0.99, 0.089, 0.436, 0.149,
    0.644, 0.376, 0.941, 0.416, 0.079, 0.901, 0.277, 0.594, 0.703, 0.248,
    0.426, 0.218, 0.96, 0.594, 0.188, 0.584, 0.168, 0.713, 0.119
    ]
    d=0.130
    prueba_ks(valores, d)

if __name__ == "__main__":
    main()
