def counting_sort(arr):
    max_value = max(arr)

    count = [0]*(max_value +1)
    for num in arr:
        count[num] +=1

    index= 0

    for i in range(len(count)):

        while count[i]>0:
            arr[index]=i
            index +=1
            count[i] -=1
numbers = []
n=int(input("Enter the number of element: "))

for i in range(n):
    value= int(input(f"Enter the value {i+1}:- "))
    numbers.append(value)

counting_sort(numbers)

print("The sorted array is :- ",numbers)