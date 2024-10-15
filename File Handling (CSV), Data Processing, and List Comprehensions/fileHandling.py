import math
import random as rn
import numpy as np
# import matplotlib.pyplot as plt
import os 
import csv


print(os.getcwd())

# PROBLEM ONE

data = []
#INPUT path and filename
#OUTPUT list of parent, child pairs
#CONSTRAINT use csv reader
def get_data(path, filename):
    with open(path + filename, "r") as f:
        read = csv.reader(f)
        info = list(read)
        return info


#input parent name
#output children
#constraint using comprehension
def get_child(name):
    return [c for p, c in data if p == name]


#input parent name
#output true if has children
#constraint using comprehension
def has_children(name):
    return bool(get_child(name))

#input child name
#output parent of child
#constraint using comprehension
def get_parent(name):
    p2 = [p for p, c in data if c == name]
    return p2[0] if p2 else None


#input child name1, child name2
#output true if children have same parent
#constraint using comprehension
def siblings(name1,name2):
    return get_parent(name1) == get_parent(name2)
 
 
#input grandparent name1, grandchild name2
#output true if name1 is grandparent to name2
#constraint using comprehension 
def grandparent(name1, name2):
    return name1 == get_parent(get_parent(name2))

#input nothing
#output all names
#constraint list comprehension only
def get_all():
    return [k for k in [i for i, _ in data] + [j for _, j in data]]

#input name1, name2
#output true if name1 and name 2 are cousins, i.e., have the same grandparents
def cousins(name1,name2):
    return siblings(get_parent(name1), get_parent(name2))


# Problem 2
# input n: total space (size), v: tiles and 
# output all possible patterns where the tiles add exactly to the the space (n)
def tiles(n, v, lst):
    tmp = []
    for x in lst:
        total = sum(x)
        if total == n:
            tmp.append(x)
        elif total < n:
            for y in v:
                new = x + [y]
                lst.append(new)
    return tmp



#problem 3
# input: a list of numbers
# output: a pair containing the sum and boolean vector (see PDF for sample output)
def max_adjacent(lst):
    leng = len(lst)
    if leng == 0:
        return [0, []]
    if leng == 1:
        return [lst[0], [1]]
    
    cVal = [0] * leng
    last = [-1] * leng
    cVal[0] = lst[0]
    cVal[1] = max(lst[0], lst[1])

    if lst[0] > lst[1]:
        last[1] = 0
    
    for x in range(0, leng):
        if cVal[x - 2] + lst[x] > cVal[x - 1]:
            cVal[x] = cVal[x - 2] + lst[x]
            last[x] = x - 2
        else:
            cVal[x] = cVal[x - 1]
            last[x] = x - 1
    total = [0] * leng  
    x = leng - 1
    while (x >= 0):
        if last[x] == x - 2:
            total[x] = 1
            x -= 2
        else:
            x -= 1
    return [cVal[-1], total]

# Test case
print(max_adjacent([99, 88, 92]))


########################
# PROBLEM 4
########################


# INPUT path and filename (payrollwins.txt)
# OUTPUT payroll and number of wins as a list
# Ouptut example: [[209,89], [139,74]]
# CONSTRAINT use csv reader
def get_data_1(path, filename):
    with open(path + filename, "r") as f:
        read = csv.reader(f)
        info = list(read)
        return [[int(x), int(y)] for x, y in info]

def std_linear_regression(data):
    length = len(data)
  
    xysum = sum([(x * y) for x, y in data])
    xsum = sum([x for x, _ in data])
    ysum = sum([y for _, y in data])
    xsqrsum = sum([(x ** 2) for x, _ in data])

    m_hat = round((length * xysum - xsum * ysum) / (length * xsqrsum - math.pow(xsum, 2)), 3)
  
    b_hat = round((ysum - m_hat * xsum) / length, 3)

    sst = sum([round(y - (ysum / length), 3) ** 2 for _, y in data])
    sse = sum([round(y - (m_hat * x + b_hat), 3) ** 2 for x, y in data])
  
    R_sq = round(1 - (sse / sst), 3)

    return m_hat, b_hat, R_sq


#### Problem 5

# INPUT path and filename (fish_data.txt)
# OUTPUT two separate lists, first one containing the age and second containing 
# the length as given in the fish_data.txt file 
# Ouptut example: [1,2,3, ...], [4.8, 8.8, 8.0, ...]
# CONSTRAINT use csv reader
# make sure to get rid of the first line that just contains the column names (we don't want that)
def get_fish_data(path, name):
    with open(path + name, "r") as f:
        read = csv.reader(f)
        next(read)
        ages = []
        lengths = []
        for i in read:
            ages.append(int(i[0]))
            lengths.append(float(i[1]))
        return ages, lengths


#INPUT lists X values, Y values of data and degree of the polynomial
#RETURN a polynomial of degree three
def make_function(X,Y,degree): # PASSED
    coef = np.polyfit(X, Y, degree)
    return np.poly1d(coef)



#### Problem 6
#input string and positive integer n
#output a list of the longest string that have no more than n distinct symbols

def max_n(str, n): # PASSED
    def longest(lst):
        def length(lst, empty = [""]):
            if lst:
                varX, lst, varY = lst[0], lst[1:], empty[0]
                if len(varX) > len(varY):
                    return length(lst, [varX])
                elif len(varX) == len(varY):
                    return length(lst, empty + [varX])
                else:
                    return length(lst, empty)
            else:
                return empty
        return length(lst)
    def difference(lst, tmp = [], count = 0):
        if lst:
            x, lst = lst[0], lst[1:]
            if not x in tmp:
                count, tmp = count + 1, tmp + [x]
            return difference(lst, tmp, count)
        else:
            return count
        
    count = []

    def subStrings(str, count, num):
        for i in range(len(str)):
            for x in range(i + 1, len(str) + 1):
                xII = str[i:x]
                count += [xII] if not xII in count and difference(xII) == num else []
        return count
    return longest(subStrings(str, count, n))




#problem 7

#input a tuple of model parameters, second parameter is the number of trials
#output the percent success rounded to two decimal places
def simulation(model_parameters, num_trials): # PASSED
    b, p, m = model_parameters
    passedAttempts = 0
    for _ in range(num_trials):
        total = b
        while total > 0 and total < m:
            result = np.random.binomial(1, p)
            if result == 1:
                total += 1
            else:
                total -= 1
        if total >= m:
            passedAttempts += 1
    win = passedAttempts / num_trials
    return round(win, 2)



if __name__ == '__main__':
    
    # uncomment to test
    # Before sbmitting to the Autograder: 
    # Make sure to comment the code for plotting graph in P4 and also the import of matplotlib on the top of this file
    # You can use that code to make the graph on your system and test but comment it before the submission

    # problem 1
    # data = get_data("Assignment6", "family.txt")
    # print(data)
    # print(has_children('0')) #true
    # print(has_children('7')) #false
    # print(get_child('6'))
    # print(get_parent('g'))
    # print(siblings('7','A')) #true
    # print(siblings('2','7')) #false
    # print(grandparent('0','3')) #true
    # print(grandparent('0','7')) #false
    # print(get_all())
    # print(cousins('3','6')) #true
    # print(cousins('3','5')) #false


    #problem 2
    # n = 6
    # v = [1,2,3]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")
    # n = 4
    # v = [1,2]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")    

    # problem 3
    # data = [[5,1,4,1,5],[5,6,2,4],[4,5,1,1],[1,5,10,4,1],[1,1,1,1,1], [4,2,3,6], [99,88,92]]
    # for d in data:
    #     print(max_adjacent(d))

    # problem 4

    # data6 = get_data_1("Assignment6", "payrollwins.txt")
    # m_hat, b_hat, R_sq  = std_linear_regression(data6)
    # print(m_hat,b_hat,R_sq)
    
    # Comment the code for plotting (and the import of matplotlib up top) before you submit to the Autograder.
    # You can test as much as you want on your system but before the submission - please comment the code for
    # plotting.
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # plt.plot([x for x,_ in data6],[m_hat*x + b_hat for x,_ in data6],'b')
    # plt.xlabel("$M Payroll")
    # plt.ylabel("Season Wins")
    # plt.title(f"Least Squares: m = {m_hat}, b = {b_hat}, R^2 = {R_sq} ")
    # plt.ylabel("Y")
    # plt.show()

    # #problem 5
    # name = "fish_data.txt"
    # X,Y = get_fish_data("Assignment6", name)
    # data5 = [[i,j] for i,j in zip(X,Y)]
    # print(data5)
      
    # plt.plot(X,Y,'ro')
    # xp = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X,Y,degree)
    # plt.plot(xp,p3(xp),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()

    #problem 6
    # data = ["aaaba", "abcba", "abbcde","aaabbbaaaaaac","abcdeffg"]
    # for d in data:
    #     for i in range(1,7):
    #         print(f"{d} with {i} max is\n {max_n(d,i)}")
    
    
    #problem 7
    # model_parameters = (2,.6,4) #starting amount, probablity of win, goal
    # print(simulation(model_parameters,100000))
    
    print()