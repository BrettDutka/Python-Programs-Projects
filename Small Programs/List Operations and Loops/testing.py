
from Lab3 import *


manual_TestCases = [
    [['123','1','132',234], 1],
    [['345','124',124,42], 3],
    [[123,[],'222'], 1]
]



cmp_listTests = [
    [[1,1,1,1,3,2],[1,1,1,1,3,2]],
    [[2522,222,1234,5],[234,222,53221,3]],
    [[111,222,333],["111","222","333"]]
]

factorialTests = [5,23,40]


solutions = {
    manual_append:[
                    ['123', '1', '132', 234, 1],
                    ['345', '124', 124, 42, 3],
                    [123, [], '222', 1],
                    ],
   
   
    manual_remove:[
                    ['123', '132', 234],
                    ['345', '124', 124],
                    [123, '222'],
                  ],
    compare_lists:[
                    [],
                    [234,53221,3],
                    ["111","222","333"],
                  ],
    factorial:[
                   120,
                   25852016738884976640000,
                   815915283247897734345611269596115894272000000000,
    ],
}

studentResults = {
    manual_append:[manual_append(*x) for x in manual_TestCases],
    manual_remove:[manual_remove(*x) for x in manual_TestCases],
    compare_lists:[compare_lists(*x) for x in cmp_listTests],
    factorial:[factorial(x) for x in factorialTests]
}

for function,results in studentResults.items():
    if results == solutions[function]:
        print(f"{function.__name__} works!!")
    else:
        print("Results: " + str(results))
        print("Solution: " + str(solutions[function]))
        print(f"{function.__name__} doesn't work :(")
    
