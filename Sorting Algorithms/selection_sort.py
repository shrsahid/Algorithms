def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range( i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i],arr[min_idx] = arr[min_idx],arr[i]

numbers =[ ]

n=int(input("Enter number of elements: "))

for i in range(n):
    value= int(input(f"Enter the elements{i+1}:- "))
    numbers.append(value)

selection_sort(numbers)
print("The sorted Array:- ",numbers)
