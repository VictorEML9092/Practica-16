def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    paso = 1

    while gap > 0:
        print(f"\nGap actual: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(f"Paso {paso}: {arr}")
            paso += 1
        gap //= 2
    return arr