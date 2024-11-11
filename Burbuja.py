"""
Created on Monday 11/11/24

@author: Victor Mendoza
"""

# Método por intercambio para ordenar números
def metodo_burbuja(ListaNum):
    for i in range(len(ListaNum) - 1):
    
        for j in range(len(ListaNum) - 1):
        
            print(ListaNum[j],">",ListaNum[j + 1]) # Se imprime la comparación
        
            if ListaNum[j] > (ListaNum[j + 1]): # Comparamos los números
                ListaNum[j], ListaNum[j + 1] = ListaNum[j + 1], ListaNum[j] # Si el primer número es mayor al segundo, intercambiamos
                print("Si hay cambio")
            else:
                print("No hay cambio")
    
        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(ListaNum,"\n")
    return ListaNum