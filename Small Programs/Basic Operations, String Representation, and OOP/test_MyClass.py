from MyClass import MySet
from MyClass import MyFraction


def test_equality():
    passes1 = mySet1.compare_with_pyset(pySet1)
    passes2 = mySet2.compare_with_pyset(pySet2)
    passes3 = mySet3.compare_with_pyset(pySet3)
    return (passes1,passes2,passes3)

def test_results(operation):
    result = test_equality()
    if all(result):
        print(f"{operation} operation works!!\n\n")
    else:
        if not result[0]:
            print("mySet 1 is not working!")
        if not result[1]:
            print("mySet2 is not working!")
        if not result[2]:
            print("mySet3 is not working!")


if __name__ == "__main__":
    mySet1 = MySet()
    mySet2 = MySet()
    mySet3 = MySet()
    pySet1 = set()
    pySet2 = set()
    pySet3 = set()
    # add operations
    mySet1.add(1)
    mySet1.add(2)
    mySet1.add(3)

    pySet1.add(1)
    pySet1.add(2)
    pySet1.add(3)

    mySet2.add("ll")
    mySet2.add('sd')

    pySet2.add('ll')
    pySet2.add('sd')

    mySet3.add( (1,2) )
    mySet3.add( (2,3) )

    pySet3.add( (1,2) )
    pySet3.add( (2,3) )

    
    print("~~~~TESTING ADD OPERATION~~~~~")
    test_results("add")

    # remove operations
    mySet1.remove(2)
    pySet1.remove(2)
    mySet2.remove('ll')
    pySet2.remove('ll')
    mySet3.remove( (2,3) )
    pySet3.remove( (2,3) )

    print("~~~~TESTING REMOVE OPERATION~~~")
    test_results("remove")

    
    print("~~~TESTING COUNT OPERATION~~~")
    test_results("count")

    print("~~~OUTPUT for __str__~~~")
    print(mySet1)
    print(mySet2)
    print(mySet3)

    

    
    # Fraction 
    f1 = MyFraction(1, 2)
    f2 = MyFraction(3, 10)
    f3 = MyFraction(7, 12)
    f4 = MyFraction(2,20)

    # testing evaluate
    print()
    print("~~~TESTING EVALUATE~~~")
    print("Proper  | Your Solution")
    print("------------------------")
    print(f"{1/2:.4f}  | {f1.evaluate():.4f} ")
    print(f"{3/10:.4f}  | {f2.evaluate():.4f} ")
    print(f"{7/12:.4f}  | {f3.evaluate():.4f} ")
    print(f"{2/20:.4f}  | {f4.evaluate():.4f} ")

    # testing add
    print()
    print("~~~TESTING ADD~~~")
    print("Proper | Your Solution")
    print(f"16/20 | {f1 + f2}")
    print(f"164/240 | {f3 + f4}")

    # testing sub
    print()
    print("~~~TESTING SUB~~~")
    print("Proper    | Your Solution")
    print(f"16/40     | {f1 - f4}")
    print(f"-34 / 120 | {f2 - f3}")


