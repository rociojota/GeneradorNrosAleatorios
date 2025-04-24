import math
from collections import Counter
from colorama import Fore, Style, init
init(autoreset=True)

def prueba_corrida(numeros, estadistico):
    """
    Realiza la prueba estadística de corridas arriba y abajo de la media (0.5) para evaluar la aleatoriedad
    de una secuencia de números reales entre 0 y 1.

    La prueba agrupa valores consecutivos iguales (0 si el número <= 0.5, 1 si > 0.5),
    cuenta la cantidad de corridas (grupos de valores iguales consecutivos) y compara
    la frecuencia observada de las longitudes de esas corridas con las frecuencias esperadas
    bajo la hipótesis de aleatoriedad.

    Se calcula un estadístico de prueba (tipo chi-cuadrado) para determinar si la diferencia
    entre frecuencias observadas y esperadas es significativa.

    Parámetros:
    ----------
    numeros : list[float] -> tamaño de la muestra
        Lista de números decimales entre 0 y 1 que representan una secuencia generada, por ejemplo, 
        mediante un generador de números pseudoaleatorios.
    
    estadistico : float
        Valor crítico del estadístico chi-cuadrado con el cual se comparará el valor calculado. 
        Este valor depende del nivel de significancia y los grados de libertad deseados.

    Salida:
    -------
    Imprime en consola:
        - La secuencia codificada en 0s y 1s.
        - La frecuencia observada y esperada de cada longitud de corrida.
        - El valor del estadístico calculado.
        - El resultado de la prueba (si se pasa o no la prueba de aleatoriedad).

    Nota:
    -----
    Esta implementación asume que los valores están uniformemente distribuidos entre 0 y 1.
    El umbral de corte utilizado para diferenciar arriba/abajo de la media es 0.5.
    """ 
    
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
    longitudes = [len(r) for r in corridas]

    # Contar frecuencias observadas por longitud
    freq_obs = Counter(longitudes)
    max_len = max(longitudes)

    print(Style.BRIGHT + "\nFrecuencia observada por longitud:")
    all_lengths = list(range(1, max(max_len, 2) + 1))
    for L in all_lengths:
        print(Style.BRIGHT + f"Longitud {L}: {freq_obs.get(L, 0)}")

    # Calcular frecuencias esperadas
    n = len(numeros)
    print(Style.BRIGHT + "\nFrecuencia esperada por longitud:")
    freq_esperadas = []
    for L in all_lengths:
        fe = (n - L + 3) / (2 ** (L + 1))
        freq_esperadas.append(fe)
        print(Style.BRIGHT + f"Longitud {L}: {fe:.4f}")
    
    # Calcular el estadístico
    calc_estadistico = 0
    for L in all_lengths:
        observed_freq = freq_obs.get(L, 0)
        expected_freq = freq_esperadas[L-1]
        calc_estadistico += ((observed_freq - expected_freq) ** 2)/expected_freq

    print(Style.BRIGHT + f"\nEstadístico: {calc_estadistico:.4f}")
    
    if calc_estadistico < estadistico:
        print(Fore.GREEN + Style.BRIGHT + "✅ La secuencia pasa la prueba de corrida arriba y abajo de la media.")
    else:
        print(Fore.RED + Style.BRIGHT + "❌ La secuencia NO pasa la prueba de corrida arriba y abajo de la media.")


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
