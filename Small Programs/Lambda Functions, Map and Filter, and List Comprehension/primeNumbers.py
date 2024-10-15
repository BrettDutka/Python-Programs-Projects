import types  # This is used to determine if you have function type


# Task 1
def add_list_elements(list1, list2):
    """
    Using a lambda function, add the lists together utilizing map
    Another stipulation is you have to add 1000 to each of them. You must accomplish this with a list comprehension.
    Returns a map object.
    You can't assume which list will be the max length between the two.
    Example:
    add_list_elements([1, 2, 3, 4], [5, 6, 7, 8, 9]) -> map object
    printing above map object as a list in testing -> [1006, 1008, 1010, 1012]
    """
    thousand = [1000 for x in range(max(len(list1), len(list2)))]
    return map(lambda x, y, z: x + y + z, list1, list2, thousand)


# Task 2
def is_a_prime(n):
    """
    Given a list of numbers, return a list of only the prime numbers.
    Example:
    get_only_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]) -> [2, 3, 5, 7]

    You must use a filter function.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
        
    if n % 2 == 0 or n % 3 ==0:
        return False
        
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
def get_only_primes(lst):
    return list(filter(is_a_prime, lst))


    


# Task 3
def quicksort(arr):
    """
    Given a list of numbers, return a sorted list of those numbers using Quick Sort.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)



if __name__ == "__main__":
    print("Task 1")
    if isinstance(add_list_elements([1], [1]), type(map(lambda x: x, [1]))):
        LISTS1 = [[1, 2, 3, 4], [-1, -1, -1, -1, -1, -1, -1], [200, -2045, 10, 8, 2]]
        LISTS2 = [[5, 6, 7, 8, 9], [-2, -3, -4, -5, -6, -7, -8], [12, 4]]
        for i in range(len(LISTS1)):
            print(list(add_list_elements(LISTS1[i], LISTS2[i])))
    else:
        print("Task 1 is not return a map object")
        if isinstance(add_list_elements([1], [1]), list):
            print("You should not convert it to a list before returning")
        else:
            print("You are returning: " + str(type(add_list_elements([1], [1]))))

    print("\nTask 2")
    assert get_only_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7]
    assert get_only_primes([1, 4, 6, 8, 9]) == []
    print(get_only_primes([11, 13, 15, 17, 27, 151]))

    print("\nTask 3")
    assert quicksort([10, 7, 2, 6, 8, 9, 1, 5, 3, 4]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quicksort([20, 19, 18, 17, 16, 15, 14, 13, 21, 11]) == [
        11,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
    ]
    print(quicksort([143, 254, 5, -2, 0, 26, 51, 3773, 99, -84]))
