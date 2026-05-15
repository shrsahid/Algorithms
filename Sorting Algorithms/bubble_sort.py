def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if not swapped:
            break

numbers = []
n = int (input("Enter the number of elements: "))

for i in range(n):
    value = int(input(f"Enter the Elements {i+1}:- "))
    numbers.append(value)

print("\nOriginal array")
print(numbers)

bubble_sort(numbers)

print("\nSorted Array:")
print(numbers)