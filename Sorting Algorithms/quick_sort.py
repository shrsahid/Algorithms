def quick_sort(arr,low,high):
    if low<high:

        pivot_index = partition(arr,low,high)

        quick_sort(arr,low, pivot_index -1)

        quick_sort(arr,pivot_index + 1,high)
    
def partition(arr,low,high):

    pivot = arr[high]
    i= low-1
    for j in range (low,high):

        if arr[j] < pivot:
            i += 1

            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high] , arr[i+1]

    return i+1
numbers = []
n=int(input("Enter number of element:"))

for i in range(n):
    value=int(input(f"Enter the value of index {i+1}:- "))
    numbers.append(value)

quick_sort(numbers,0,len(numbers)-1)

print("The sorted array is :- ",numbers)
    