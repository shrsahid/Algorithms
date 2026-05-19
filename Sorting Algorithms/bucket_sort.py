def bucket_sort(arr):

    max_value = max(arr)

    bucket_count = len(arr)
    buckets = []

    for i in range(bucket_count):
        buckets.append([])

    for num in arr:

        index = int((num / (max_value + 1)) * bucket_count)

        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    k = 0

    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

print("\nOriginal Array:")
print(numbers)

# Call bucket sort
bucket_sort(numbers)

print("\nSorted Array:")
print(numbers)