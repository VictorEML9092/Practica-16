def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"\nIntercambio: {arr}")
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Heap construido en índice {i}: {arr}")
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Intercambio de raíz con el elemento en índice {i}: {arr}")
        heapify(arr, i, 0)
        print(f"Heap después del heapify en índice {i}: {arr}")
    return arr