
def recursive_insertion_sort(arr, n):
    if n <= 1:
        return

    recursive_insertion_sort(arr, n - 1)

    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


numbers = [12, 11, 13, 5, 6]

print("Original Array:", numbers)

recursive_insertion_sort(numbers, len(numbers))

print("Sorted Array:", numbers)
