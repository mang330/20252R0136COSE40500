def bubble_sort(arr):
    a = arr[:]  # do not mutate input
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))
