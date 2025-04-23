from lehmer import metodo_lehmer
from pruebaFrecuencia import prueba_frecuencia
from pruebaPromedios import prueba_promedios
from pruebaCorrida import prueba_corrida
from pruebaSerie import prueba_serie
from pruebaKS import prueba_ks

import time

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

        if opcion == '1':
            print("\nPrueba de los promedios:")
            print("--------------------------------------------------")
            z_alpha = float(input("Ingrese el valor de z_alpha: "))
            prueba_promedios(resultados, z_alpha)
            print("--------------------------------------------------")

        elif opcion == '2':
            print("\nPrueba de la Frecuencia:")
            print("--------------------------------------------------")
            nro_intervalos = int(input("Ingrese el número de intervalos (entero): "))
            z_alpha = float(input("Ingrese el valor del estadístico: "))
            prueba_frecuencia(resultados, nro_intervalos, z_alpha)
            print("--------------------------------------------------")

        elif opcion == '3':
            print("\nPrueba de la Serie")
            print("--------------------------------------------------")
            estadistico = float(input("Ingrese el valor del estadístico: "))
            x= int(input("Ingrese el valor de x: "))
            prueba_serie(resultados, estadistico, x)
            print("--------------------------------------------------")


        elif opcion == '4':
            print("\nPrueba de K-S")
            print("--------------------------------------------------")
            d = float(input("Ingrese el valor del estadístico: "))
            prueba_ks(resultados, d)
            print("--------------------------------------------------")

        elif opcion == '5':
            print("\nPrueba de Corrida Abajo y Arriba de la Media")
            print("--------------------------------------------------")
            estadistico = float(input("Ingrese el valor del estadístico: "))
            prueba_corrida(resultados, estadistico)
            print("--------------------------------------------------")

        elif opcion == '6':
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

        if opcion == '1':
            print("\nMétodo de la parte central del cuadrado:")
            print("--------------------------------------------------")

        elif opcion == '2':
            print("Generador Pseudoaleatorio - Método de Lehmer")
            seed = int(input("Ingrese la semilla (n₀): "))
            t = int(input("Ingrese el número t: "))
            k = len(str(t))
            cantidad = int(input("¿Cuántos números desea generar?: "))
            resultados = metodo_lehmer(seed, t, k, cantidad)
            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")
            mostrar_menu_pruebas(resultados)

        elif opcion == '3':
            print("\nMétodo Congruencial Mixto:")
            print("--------------------------------------------------")
            resultados = metodo_congruencial_mixto()
            print(f"Resultados: {resultados}")

        elif opcion == '4':
            print("\nMétodo Congruencial Multiplicativo:")
            print("--------------------------------------------------")
            resultados = metodo_congruencial_multiplicativo()
            print(f"Resultados: {resultados}")

        elif opcion == '5':
            print("\nMétodo Congruencial Aditivo:")
            print("--------------------------------------------------")
            resultados = metodo_congruencial_aditivo()
            print(f"Resultados: {resultados}")

        elif opcion == '6':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Por favor seleccione una opción del 1 al 6.")
            print("--------------------------------------------------")



if __name__ == "__main__":
    main()