import time

from congruencial_multiplicativo import metodo_congruencial_multiplicativo
from congruencialAditivo import metodo_congruencial_aditivo
from congruencialMixto import metodo_congruencial_mixto
from lehmer import metodo_lehmer
from parteCentralCuadrado import metodo_parte_central_cuadrado
from pruebaCorrida import prueba_corrida
from pruebaFrecuencia import prueba_frecuencia
from pruebaKS import prueba_ks
from pruebaPromedios import prueba_promedios
from pruebaSerie import prueba_serie


def validacion_enteros(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
        except ValueError:
            print("❌ Error: La entrada no es un número entero válido.")
            continue
        if valor <= 0:
            print("❌ El número debe ser un entero positivo.")
            continue
        break
    return valor


def validacion_flotantes(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
        except ValueError:
            print("❌ Error: La entrada no es un número flotante válido.")
            continue
        if valor <= 0.0:
            print("❌ El número debe ser un flotante positivo.")
            continue
        break
    return valor


def mostrar_menu_pruebas(resultados):
    while True:
        print("\nSeleccione una prueba estadística:")
        print("1. Prueba de los Promedios")
        print("2. Prueba de la Frecuencia")
        print("3. Prueba de la Serie")
        print("4. Prueba de K-S")
        print("5. Prueba de Corrida Abajo y Arriba de la Media")
        print("6. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "1":
            print("\nPrueba de los promedios:")
            print("--------------------------------------------------")
            z_alpha = validacion_flotantes("Ingrese el valor de z_alpha: ")
            prueba_promedios(resultados, z_alpha)
            print("--------------------------------------------------")

        elif opcion == "2":
            print("\nPrueba de la Frecuencia:")
            print("--------------------------------------------------")
            nro_intervalos = validacion_enteros("Ingrese el número de intervalos: ")
            z_alpha = validacion_flotantes("Ingrese el valor de z_alpha: ")

            prueba_frecuencia(resultados, nro_intervalos, z_alpha)
            print("--------------------------------------------------")

        elif opcion == "3":
            print("\nPrueba de la Serie")
            print("--------------------------------------------------")
            estadistico = validacion_flotantes("Ingrese el valor del estadístico: ")
            x = validacion_enteros("Ingrese el valor de x: ")
            prueba_serie(resultados, estadistico, x)
            print("--------------------------------------------------")

        elif opcion == "4":
            print("\nPrueba de K-S")
            print("--------------------------------------------------")
            d = validacion_flotantes("Ingrese el valor del estadístico: ")
            prueba_ks(resultados, d)
            print("--------------------------------------------------")

        elif opcion == "5":
            print("\nPrueba de Corrida Abajo y Arriba de la Media")
            print("--------------------------------------------------")
            estadistico = validacion_flotantes("Ingrese el valor del estadístico: ")
            prueba_corrida(resultados, estadistico)
            print("--------------------------------------------------")

        elif opcion == "6":
            print("Volviendo al menú principal...")
            break

        else:
            print("❌ Opción no válida. Por favor seleccione una opción del 1 al 6.")
            print("--------------------------------------------------")


def main():
    resultados = []
    while True:
        print("\nSeleccione un método generador de números pseudoaleatorios:")
        print("1. Método de la parte central del cuadrado")
        print("2. Método de Lehmer")
        print("3. Método Congruencial Mixto")
        print("4. Método congruencial Multiplicativo")
        print("5. Método congruencial Aditivo")
        print("6. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("Generador Pseudoaleatorio - Método de la Parte Central del Cuadrado")

            seed = validacion_enteros("Ingrese la semilla (M): ")
            n_digitos = validacion_enteros(
                "Ingrese el número de dígitos deseados (N): "
            )
            cantidad = validacion_enteros("¿Cuántos números desea generar?: ")

            resultados = metodo_parte_central_cuadrado(seed, n_digitos, cantidad)

            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")

            mostrar_menu_pruebas(resultados)
            print("--------------------------------------------------")

        elif opcion == "2":
            print("Generador Pseudoaleatorio - Método de Lehmer")
            seed = validacion_enteros("Ingrese la semilla (n₀): ")
            t = validacion_enteros("Ingrese el valor de t: ")
            k = len(str(t))
            cantidad = validacion_enteros("¿Cuántos números desea generar?: ")
            resultados = metodo_lehmer(seed, t, k, cantidad)
            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")
            mostrar_menu_pruebas(resultados)

        elif opcion == "3":
            print("\nMétodo Congruencial Mixto:")
            print("--------------------------------------------------")

            # Validación de 'a' (multiplicador)
            while True:
                entrada = input("Multiplicador a: ")
                try:
                    a = int(entrada)
                    if a <= 0:
                        print("❌ El número debe ser un entero positivo.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            # Validación de 'c' (incremento)
            while True:
                entrada = input("Incremento c: ")
                try:
                    c = int(entrada)
                    if c <= 0:
                        print("❌ El número debe ser un entero positivo.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            # Validación de 'm' (módulo)
            while True:
                entrada = input("Módulo m: ")
                try:
                    m = int(entrada)
                    if m <= 0:
                        print("❌ El módulo m debe ser un entero positivo.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            # Validación de 'x0' (semilla)
            while True:
                entrada = input("Semilla inicial x0: ")
                try:
                    x0 = int(entrada)
                    if not (0 <= x0 < m):
                        print(f"❌ La semilla x0 debe estar entre 0 y {m - 1}.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            # Validación de 'n' (cantidad de números a generar)
            while True:
                entrada = input("¿Cuántos números querés generar? n: ")
                try:
                    n = int(entrada)
                    if n <= 0:
                        print("❌ El número debe ser un entero positivo.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            resultados = metodo_congruencial_mixto(a, c, m, x0, n)
            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")
            mostrar_menu_pruebas(resultados)

        elif opcion == "4":
            print("\nGenerador Pseudoaleatorio - Método Congruencial Multiplicativo")
            print("--------------------------------------------------")

            while True:
                entrada = input("Ingrese la semilla (n₀): ")
                try:
                    semilla = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if semilla <= 0 or semilla % 2 == 0 or semilla % 5 == 0:
                    print(
                        "❌ La semilla debe ser un número impar, mayor que 0 y no divisible por 5."
                    )
                    continue
                break

            while True:
                entrada = input("Ingrese la constante multiplicativa (a): ")
                try:
                    a = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if a <= 0:
                    print("❌ La constante multiplicativa debe ser mayor que 0.")
                    continue
                break

            while True:
                entrada = input("Ingrese el módulo (m): ")
                try:
                    m = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if m <= 0:
                    print("❌ El módulo debe ser mayor que 0.")
                    continue
                break

            while True:
                entrada = input("¿Cuántos números desea generar?: ")
                try:
                    cantidad = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if cantidad <= 0:
                    print("❌ La cantidad debe ser mayor que 0.")
                    continue
                break

            while True:
                entrada = input(
                    "Ingrese la cantidad de dígitos de precisión (por ejemplo, 4): "
                )
                try:
                    digitos_precision = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if digitos_precision <= 0 or digitos_precision >= 10:
                    print(
                        "❌ La cantidad de dígitos debe ser mayor que 0 y menor que 10."
                    )
                    continue
                break

            try:
                resultados = metodo_congruencial_multiplicativo(
                    semilla, a, m, cantidad, digitos_precision
                )
                print("\nNúmeros pseudoaleatorios generados:")
                for i, r in enumerate(resultados):
                    print(f"{i + 1}: {r:.{digitos_precision}f}")
                mostrar_menu_pruebas(resultados)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif opcion == "5":
            print("\nMétodo Congruencial Aditivo:")
            print("--------------------------------------------------")

            # Validación de semillas
            while True:
                semillas_input = input(
                    "Ingresá las semillas (números separados por comas): "
                )
                try:
                    semillas = [int(x.strip()) for x in semillas_input.split(",")]
                    if len(semillas) < 2:
                        print("❌ Error: Debés ingresar al menos dos semillas.")
                        continue
                    if any(s <= 0 for s in semillas):
                        print("❌ Todas las semillas deben ser enteros positivos.")
                        continue
                    break
                except ValueError:
                    print(
                        "❌ Error: Asegurate de ingresar solo números enteros separados por comas."
                    )

            # Validación de módulo m
            while True:
                entrada = input("Módulo m: ")
                try:
                    m = int(entrada)
                    if m <= 0:
                        print("❌ El módulo m debe ser un entero positivo.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            # Validación de cantidad n
            while True:
                entrada = input("¿Cuántos números querés generar? n: ")
                try:
                    n = int(entrada)
                    if n <= 0:
                        print("❌ El número debe ser un entero positivo.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")

            resultados = metodo_congruencial_aditivo(semillas, m, n)

            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")
            mostrar_menu_pruebas(resultados)

        elif opcion == "6":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Por favor selec2cione una opción del 1 al 6.")
            print("--------------------------------------------------")


if __name__ == "__main__":
    main()
