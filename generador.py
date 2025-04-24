from lehmer import metodo_lehmer
from pruebaFrecuencia import prueba_frecuencia
from pruebaPromedios import prueba_promedios
from pruebaCorrida import prueba_corrida
from pruebaSerie import prueba_serie
from pruebaKS import prueba_ks
from parteCentralCuadrado import metodo_parte_central_cuadrado

import time

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

        if opcion == '1':
            print("\nPrueba de los promedios:")
            print("--------------------------------------------------")
            z_alpha = validacion_flotantes("Ingrese el valor de z_alpha: ")
            prueba_promedios(resultados, z_alpha)
            print("--------------------------------------------------")

        elif opcion == '2':
            print("\nPrueba de la Frecuencia:")
            print("--------------------------------------------------")
            nro_intervalos = validacion_enteros("Ingrese el número de intervalos: ")
            z_alpha = validacion_flotantes("Ingrese el valor de z_alpha: ")

            prueba_frecuencia(resultados, nro_intervalos, z_alpha)
            print("--------------------------------------------------")

        elif opcion == '3':
            print("\nPrueba de la Serie")
            print("--------------------------------------------------")
            estadistico = validacion_flotantes("Ingrese el valor del estadístico: ")
            x = validacion_enteros("Ingrese el valor de x: ")
            prueba_serie(resultados, estadistico, x)
            print("--------------------------------------------------")


        elif opcion == '4':
            print("\nPrueba de K-S")
            print("--------------------------------------------------")
            d = validacion_flotantes("Ingrese el valor del estadístico: ")
            prueba_ks(resultados, d)
            print("--------------------------------------------------")

        elif opcion == '5':
            print("\nPrueba de Corrida Abajo y Arriba de la Media")
            print("--------------------------------------------------")
            estadistico = validacion_flotantes("Ingrese el valor del estadístico: ")
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
            
            print("Generador Pseudoaleatorio - Método de la Parte Central del Cuadrado")
    
            seed = validacion_enteros("Ingrese la semilla (M): ")
            n_digitos = validacion_enteros("Ingrese el número de dígitos deseados (N): ")
            cantidad = validacion_enteros("¿Cuántos números desea generar?: ")
            
            resultados = metodo_parte_central_cuadrado(seed, n_digitos, cantidad)
            
            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")
            
            mostrar_menu_pruebas(resultados)
            print("--------------------------------------------------")

        elif opcion == '2':
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
            print("❌ Opción no válida. Por favor selec2cione una opción del 1 al 6.")
            print("--------------------------------------------------")



if __name__ == "__main__":
    main()