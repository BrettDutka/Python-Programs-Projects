###########################################################
# factorial
###########################################################

def factorial(n):
    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def tail_factorial(n, a=1):
    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return a
    else:
        return tail_factorial(n-1, a=a*n)

d = {}
def memo_factorial(n):
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n not in d.keys():
        if n <= 1:
            d[n] = 1
        else:
            d[n] = n * memo_factorial(n-1)

    return d[n]

###########################################################
# only_ints
###########################################################

def only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == []:
        return []
    elif type(xlist[0] != int):
        return [] + only_ints(xlist[1:])
    else:
        return [xlist[0]] + only_ints(xlist[1:])            
        
        

def tail_only_ints(xlist, a=[]):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == []:
        return a
    elif type(xlist[0]) != int:
        return tail_only_ints([]+xlist[1:], a = a)
    else:
        return tail_only_ints(xlist[1:], a = [xlist[0]] + a)

d_only = {}
def memo_only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    xtup = tuple(xlist)

    if xtup not in d_only.keys():
        if xlist == []:
            d_only[xtup] = []
        elif type(xlist[0]) != int:
            d_only[xtup] = memo_only_ints(xlist[1:])
        else:
            d_only[xtup] = [xlist[0]] + memo_only_ints(xlist[1:])

    return d_only[xtup]

if __name__ == "__main__":
    # Write your own print statements here
    # to briefly test your code
    
    # Problem 1
    print(factorial(5))

    # Problem 2
    print(tail_factorial(6))

    # Problem 3
    print(memo_factorial(4))
    # Problem 4
    print(only_ints([5,4,3,2,1,6,7,8,9,10]))

    # Problem 5
    print(tail_only_ints([1,5,4,6,8]))

    # Problem 6
    print(memo_only_ints([5,6,3,9,1]))