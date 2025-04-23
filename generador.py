from lehmer import metodo_lehmer
from pruebaFrecuencia import prueba_frecuencia
from pruebaPromedios import prueba_promedios
from pruebaCorrida import prueba_corrida
from pruebaSerie import prueba_serie
from pruebaKS import prueba_ks
from parteCentralCuadrado import metodo_parte_central_cuadrado

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
            while True:
                entrada = input("Ingrese el valor de z_alpha: ")
                try:
                    z_alpha = float(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número flotante válido.")
                    continue                        
                if z_alpha <= 0.0:                      
                    print("❌ El número debe ser un flotante positivo.")
                    continue                        
                break 
            prueba_promedios(resultados, z_alpha)
            print("--------------------------------------------------")

        elif opcion == '2':
            print("\nPrueba de la Frecuencia:")
            print("--------------------------------------------------")
            while True:
                entrada = input("Ingrese el número de intervalos: ")
                try:
                    nro_intervalos = int(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue                        
                if nro_intervalos <= 0:                      
                    print("❌ El número debe ser un entero positivo.")
                    continue                        
                break     

            while True:
                entrada = input("Ingrese el valor del estadístico: ")
                try:
                    z_alpha = float(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número flotante válido.")
                    continue                        
                if z_alpha <= 0.0:                      
                    print("❌ El número debe ser un flotante positivo.")
                    continue                        
                break 

            prueba_frecuencia(resultados, nro_intervalos, z_alpha)
            print("--------------------------------------------------")

        elif opcion == '3':
            print("\nPrueba de la Serie")
            print("--------------------------------------------------")
            while True:
                entrada = input("Ingrese el valor del estadístico: ")
                try:
                    estadistico = float(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número flotante válido.")
                    continue                        
                if estadistico <= 0.0:                      
                    print("❌ El número debe ser un flotante positivo.")
                    continue                        
                break 
            while True:
                entrada = input("Ingrese el valor de x: ")
                try:
                    x = int(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número flotante válido.")
                    continue                        
                if x <= 0:                      
                    print("❌ El número debe ser un flotante positivo.")
                    continue                        
                break 
            prueba_serie(resultados, estadistico, x)
            print("--------------------------------------------------")


        elif opcion == '4':
            print("\nPrueba de K-S")
            print("--------------------------------------------------")
            while True:
                entrada = input("Ingrese el valor del estadístico: ")
                try:
                    d = float(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número flotante válido.")
                    continue                        
                if d <= 0.0:                      
                    print("❌ El número debe ser un flotante positivo.")
                    continue                        
                break 
            prueba_ks(resultados, d)
            print("--------------------------------------------------")

        elif opcion == '5':
            print("\nPrueba de Corrida Abajo y Arriba de la Media")
            print("--------------------------------------------------")
            while True:
                entrada = input("Ingrese el valor del estadístico: ")
                try:
                    estadistico = float(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número flotante válido.")
                    continue                        
                if estadistico <= 0.0:                      
                    print("❌ El número debe ser un flotante positivo.")
                    continue                        
                break 
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

            while True:
                entrada = input("Ingrese la semilla (M): ")
                try:
                    seed = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if seed <= 0:
                    print("❌ El número debe ser un entero positivo.")
                    continue
                break

            while True:
                entrada = input("Ingrese el número de dígitos deseados (N): ")
                try:
                    n_digitos = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue
                if n_digitos <= 0:
                    print("❌ El número debe ser un entero positivo.")
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
                    print("❌ El número debe ser un entero positivo.")
                    continue
                break

            resultados = metodo_parte_central_cuadrado(seed, n_digitos, cantidad)
            print("\nNúmeros pseudoaleatorios generados:")
            for i, r in enumerate(resultados):
                print(f"{i + 1}: {r:.5f}")
            mostrar_menu_pruebas(resultados)
            print("--------------------------------------------------")

        elif opcion == '2':
            print("Generador Pseudoaleatorio - Método de Lehmer")
            while True:
                entrada = input("Ingrese la semilla (n₀): ")
                try:
                    seed = int(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue                        

                if seed <= 0:                      
                    print("❌ El número debe ser un entero positivo.")
                    continue                        
                break     

            while True:
                entrada = input("Ingrese el valor de t: ")
                try:
                    t = int(entrada)               
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue                        

                if t <= 0:                      
                    print("❌ El número debe ser un entero positivo.")
                    continue                        
                break                          
            k = len(str(t))
            while True:
                entrada = input("¿Cuántos números desea generar?: ")
                try:
                    cantidad = int(entrada)
                except ValueError:
                    print("❌ Error: La entrada no es un número entero válido.")
                    continue    
                if cantidad <= 0:
                    print("❌ El número debe ser un entero positivo.")
                    continue
                break

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