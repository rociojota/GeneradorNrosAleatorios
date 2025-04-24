from math import trunc


def truncar(num, digitos):
    factor = 10**digitos
    return trunc(num * factor) / factor


def metodo_congruencial_multiplicativo(semilla, a, m, cantidad, digitos_precision=4):
    """
    Genera una secuencia de números pseudoaleatorios utilizando el método
    congruencial multiplicativo.
    :param semilla: Semilla inicial (debe ser un número impar, mayor que 0 y no divisble por 5)
    :param a: Constante multiplicativa (debe ser mayor que 0)
    :param m: Módulo (debe ser mayor que 0)
    :param cantidad: Cantidad de números a generar (debe ser mayor que 0)
    :param digitos_precision: Cantidad de dígitos de precisión para cada número generado. El valor por defecto es 4 (debe ser mayor que 0 y menor que 10)
    :return: Lista de números pseudoaleatorios generados
    """
    if semilla % 2 == 0 or semilla <= 0 or semilla % 5 == 0:
        raise Exception(
            "La semilla debe ser un número impar, mayor que 0 y no divisible por 5"
        )
    if a <= 0:
        raise Exception("La constante multiplicativa debe ser mayor que 0")
    if m <= 0:
        raise Exception("El módulo debe ser mayor que 0")
    if cantidad <= 0:
        raise Exception("La cantidad de números a generar debe ser mayor que 0")
    if digitos_precision <= 0 or digitos_precision >= 10:
        raise Exception(
            "La cantidad de dígitos de precisión debe ser mayor que 0 y menor que 10"
        )

    secuencia = []

    for _ in range(0, cantidad):
        semilla = (a * semilla) % m
        num_generado = truncar(semilla / m, digitos_precision)
        secuencia.append(num_generado)

    return secuencia


# Ejemplo de uso
if __name__ == "__main__":
    semilla = 1317
    a = 5631
    m = 547
    cantidad = 8
    digitos_precision = 3

    try:
        secuencia = metodo_congruencial_multiplicativo(
            semilla, a, m, cantidad, digitos_precision
        )
        print("Secuencia generada:", secuencia)
    except Exception as e:
        print("Error:", e)
