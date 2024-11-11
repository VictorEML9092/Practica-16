def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    print(f"\n[Counting Sort] Ordenando por el dígito en la posición {exp}:")
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    print("Frecuencia de cada dígito:", count)
    for i in range(1, 10):
        count[i] += count[i - 1]
    print("Posiciones finales en la lista de salida:", count)
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    print("Lista después de ordenar por el dígito actual:", output)
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    print("Lista original:", arr)
    while max_num // exp > 0:
        print(f"\n[Radix Sort] Ordenando con exp = {exp}")
        counting_sort(arr, exp)
        print("Lista después de ordenar con exp =", exp, ":", arr)
        exp *= 10
    return arr