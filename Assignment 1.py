def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

try:
    user_input = input("Enter a list of integers separated by spaces: ")
    unsorted_list = list(map(int, user_input.split()))
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
    exit()

bubble_sort(unsorted_list)

print("Sorted array:", unsorted_list)