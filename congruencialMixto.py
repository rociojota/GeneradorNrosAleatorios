def metodo_congruencial_mixto(a, c, m, x0, n):
    """
    Método congruencial mixto para generar números pseudoaleatorios.
    
    Parámetros:
    - a: multiplicador
    - c: incremento
    - m: módulo
    - x0: semilla
    - n: cantidad de números a generar
    
    Retorna:
    - Una lista con n números pseudoaleatorios normalizados entre 0 y 1.
    """
    print("Generador de números pseudoaleatorios (congruencial mixto)")
    # Pedimos todos los parámetros
    

    # Validaciones mínimas
    if m <= 0:
        print("Error: el módulo m debe ser un entero positivo.")
        return
    if not (0 <= x0 < m):
        print(f"Error: la semilla x0 debe estar entre 0 y {m-1}.")
        return

    numeros = []
    x = x0
    for _ in range(n):
        x = (a * x + c) % m
        r = x / m  # Normalización
        numeros.append(r)
    return numeros
