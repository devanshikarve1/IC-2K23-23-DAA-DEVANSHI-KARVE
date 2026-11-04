
def recursive_bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    recursive_bubble_sort(arr, n - 1)


numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", numbers)

recursive_bubble_sort(numbers, len(numbers))

print("Sorted Array:", numbers)
