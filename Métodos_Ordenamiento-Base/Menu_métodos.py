import m_todos_de_ordenamiento

def menu():
    Lista = []

    while True:
        print("\n1. Ingresar los números a ordenar")
        print("2. Ordenar por el método Shellsort")
        print("3. Ordenar por el método Quicksort")
        print("4. Ordenar por el método Heapsort")
        print("5. Ordenar por el método Radix")
        print("6. Ordenar por el método de intercambio")
        print("7. Ordenar por el método de inserción")
        print("8. Ordenar por el método de Selección")
        print("9. Salir")

        opcion = input("\nIngrese la opción que desea usar: ")

        if opcion == "1":
            elementos = int(input("\nIngrese la cantidad de números a ingresar: "))
            Lista = []
            for i in range(elementos):
                numeros = int(input("Ingrese un número: "))
                Lista.append(numeros)
            print(f"Lista actual: {Lista}")

        elif opcion == "2":
            shell_sorted = m_todos_de_ordenamiento.shell_sort(Lista[:])
            print(f"\nLista ordenada con Shellsort: {shell_sorted}")

        elif opcion == "3":
            quick_sorted = m_todos_de_ordenamiento.quicksort(Lista[:])
            print(f"\nLista ordenada con Quicksort: {quick_sorted}")

        elif opcion == "4":
            heap_sorted = m_todos_de_ordenamiento.heapsort(Lista[:])
            print(f"\nLista ordenada con Heapsort: {heap_sorted}")

        elif opcion == "5":
            radix_sorted = m_todos_de_ordenamiento.radix_sort(Lista[:])
            print(f"\nLista ordenada con Radix: {radix_sorted}")
        
        elif opcion == "6":
            bubble_sorted = m_todos_de_ordenamiento.metodo_burbuja(Lista[:])
            print(f"\nLista ordenada con Intercambio: {bubble_sorted}")
        
        elif opcion == "7":
            deck_sorted = m_todos_de_ordenamiento.metodo_baraja(Lista[:])
            print(f"\nLista ordenada con Inserción: {deck_sorted}")

        elif opcion == "8":
            selection_sorted = m_todos_de_ordenamiento.metodo_seleccion(Lista[:])
            print(f"\nLista ordenada con Selección: {selection_sorted}")

        elif opcion == "9":
            print("\nSaliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()