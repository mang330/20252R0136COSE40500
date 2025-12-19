def binary_search(sorted_arr, target):
    lo, hi = 0, len(sorted_arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] == target:
            return mid
        if sorted_arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 4, 7, 9, 12]
    print(binary_search(arr, 7))
    print(binary_search(arr, 2))
