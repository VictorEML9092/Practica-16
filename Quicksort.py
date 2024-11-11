def quicksort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
        print("\n  " * depth + f"División en profundidad {depth}: Pivote = {pivot}")
        print("  " * depth + f"Izquierda: {left}")
        print("  " * depth + f"Derecha: {right}")
        
        # Recursión y combinación
        sorted_left = quicksort(left, depth + 1)
        sorted_right = quicksort(right, depth + 1)
        
        result = sorted_left + [pivot] + sorted_right
        print("  " * depth + f"Combinación en profundidad {depth}: {result}")
        
        return result