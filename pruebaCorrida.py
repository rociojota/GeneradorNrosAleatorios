import math
from collections import Counter

def prueba_corrida(numeros, estadistico):
    secuencia_s = [0 if num <= 0.5 else 1 for num in numeros]
    print(f"Secuencia S: {secuencia_s}")

    # Agrupar corridas consecutivas
    corridas = []
    run = [secuencia_s[0]]
    for x in secuencia_s[1:]:
        if x == run[-1]:
            run.append(x)
        else:
            corridas.append(run)
            run = [x]
    corridas.append(run)

    # Calcular longitudes
    longitudes = []
    for r in corridas:
        longitudes.append(len(r))

    # Contar frecuencias observadas por longitud
    freq_obs = Counter(longitudes)
    max_len = max(longitudes)

    print("\nFrecuencia observada por longitud:")
    all_lengths = list(range(1, max(max_len, 2) + 1))
    for L in all_lengths:
        print(f"Longitud {L}: {freq_obs.get(L, 0)}")

    # Calcular frecuencias esperadas según la fórmula para cada longitud L
    n = len(numeros)
    print("\nFrecuencia esperada por longitud:")
    freq_esperadas = []
    for L in all_lengths:
        fe = (n - L + 3) / (2 ** (L + 1))
        freq_esperadas.append(fe)
        print(f"Longitud {L}: {fe:.4f}")
    
    # Calcular el estadístico
    calc_estadistico = 0
    for L in all_lengths:
        # Si la longitud no aparece en freq_obs, la frecuencia observada es 0
        observed_freq = freq_obs.get(L, 0)
        expected_freq = freq_esperadas[L-1]
        calc_estadistico += ((observed_freq - expected_freq) ** 2)/expected_freq

    print(f"\nEstadístico: {calc_estadistico:.4f}")
    
    if calc_estadistico < estadistico:
        print("✅ La secuencia pasa la prueba de corrida arriba y abajo de la media.")
    else:
        print("❌ La secuencia NO pasa la prueba de corrida arriba y abajo de la media.")



def main():
    valores = []
    print("\nPrueba de los promedios:")
    print("--------------------------------------------------")
    """ 
    nro_valores = int(input("¿Cuántos números desea ingresar?: "))
    for i in range(nro_valores):
        valores.append(float(input(f"Ingrese el número {i + 1}: ")))
    estadistico = float(input("Ingrese el valor del estadístico: "))
    """
    
    valores = [0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426]
    estadistico = 7.81  
    
    prueba_corrida(valores, estadistico)

if __name__ == "__main__":
    main()
