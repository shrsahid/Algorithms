def insertion_sort(arr):
    n = len(arr)

    for i in range(n):

        key = arr[i]
        j= i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]

            j-=1
        arr[j+1] = key
numbers =[]

n = int(input("Enter Number of element: "))

for i in range(n):
    value= int(input(f"Enter the value of element {i+1}:- "))
    numbers.append(value)

insertion_sort(numbers)

print("The sorted array is : ",numbers)
