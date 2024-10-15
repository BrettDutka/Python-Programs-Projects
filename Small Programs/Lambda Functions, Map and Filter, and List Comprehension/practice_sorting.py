def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [3,4,5,6,7,8,9]
x = 4

result = binary_search(arr, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not Found")


def binarySearch(arr, x, low, high):
    if high >+ low:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
    
        elif arr[mid] > x:
            return binarySearch(arr, x, low, mid-1)
    
        else:
            return binarySearch(arr, x, mid + 1, high)
    else:
        return -1
    
arr = [3,4,5,6,7,8,9]
x = 4
result = binarySearch(arr, x, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not Found")
    
