def metodo_congruencial_aditivo(semillas, m, n):
    """
    Método congruencial aditivo para generar números pseudoaleatorios.

    Parámetros:
    - semillas: lista de valores iniciales (mínimo 2)
    - m: módulo
    - n: cantidad de números a generar

    Retorna:
    - Una lista de n números pseudoaleatorios normalizados entre 0 y 1.
    """

    
    k = len(semillas)
    resultados = semillas.copy()
    
    for i in range(n):
        nuevo = (resultados[-1] + resultados[-k]) % m
        resultados.append(nuevo)

    # Solo devolvemos los nuevos generados, no las semillas
    normalizados = [x / m for x in resultados[k:k+n]]
    return normalizados
