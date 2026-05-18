# Bucket Sort in Python

def bucket_sort(arr):

    # Find maximum value
    max_value = max(arr)

    # Create empty buckets
    bucket_count = len(arr)
    buckets = []

    for i in range(bucket_count):
        buckets.append([])

    # Put array elements into buckets
    for num in arr:

        # Calculate bucket index
        index = int((num / (max_value + 1)) * bucket_count)

        buckets[index].append(num)

    # Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Merge buckets into original array
    k = 0

    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1


# Main Program
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