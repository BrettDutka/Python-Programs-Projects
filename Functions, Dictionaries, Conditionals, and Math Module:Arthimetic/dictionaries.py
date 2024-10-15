import math
# import matplotlib.pyplot as plt



###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    return dlst[2] - ((14 - dlst[1]) / 12)

def a2(dlst):
    return a(dlst) + ((a(dlst) / 4)) - ((a(dlst) / 100)) + ((a(dlst) / 400))

def b(dlst):
    return math.floor(a2(dlst))

def c(dlst):
    return dlst[1] + (12 * ((14 - dlst[1]) / 12)) - 2

def day(dlst):
    d = (dlst[0] + b(dlst) + (31 * (c(dlst) / 12))) % 7
    d = round(d)
    return week[d]
##########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    a, b, c = t
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        pos = (-b + math.sqrt(discriminant)) / (2 * a)
        neg = (-b - math.sqrt(discriminant)) / (2 * a)
        return (round(neg, 2), round(pos, 2))
    else:
        realNum = -b / (2 * a)
        imaginaryNum = math.sqrt(-discriminant) / (2 * a)
        return (complex(round(realNum, 2), round(imaginaryNum, 2)), complex(round(realNum, 2), round(-imaginaryNum, 2)))
    
###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
# You'll be comparing the smallest degree of difference between each sublist representing each person.
# RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)
def inner_prod(v0,v1):
    t = 0
    for x in range(len(v0)):
        t += v0[x] * v1[x]
    return round(t, 2)

def mag(v):
    return math.sqrt(inner_prod(v, v))


def angle(v0,v1):
    n = inner_prod(v0, v1)
    x = mag(v0) * mag(v1)
    theta = math.acos(n / x) * 180 / math.pi
    return round(theta, 2)


def match(people):
    scores = []
    for x in range(len(people)):
        for y in range(x + 1, len(people)):
            v0 = people[x]
            v1 = people[y]
            theta = angle(v0, v1)
            scores.append([v0, v1, theta])
    return scores

def best_match(scores):
    best = float("inf")
    pair = []
    for x in scores:
        theta = round(x[2], 2)
        if theta < best:
            best = theta
            pair = x
    return pair




###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT tuple of quadratic (ax^2 + bx + c)
#RETURN tuple (m,n) cofficients for real solutions a(x+m)^2 + n = 0
#CONSTRAINT round to 2 places
def c_s(coefficients):
    a, b, c = coefficients
    m = b / (2 * a)
    n = c - (b ** 2) / (4 * a)
    return round(m, 2), round(n, 2)

#INPUT coefficients for quadratic ax^2 + bx + c 
#RETURN return real roots uses c_s
def q_(coefficients):
    m, n = c_s(coefficients)
    r1 = -m - (math.sqrt(-n))
    r2 = -m + (math.sqrt(-n))
    return round(r1, 2), round(r2, 2)


###########################################################################
# Functions for Problem 5
###########################################################################
# INPUT List of numbers
# RETURN Various means
def mean(lst):
    t = 0
    for x in lst:
        t += x
    return round(t / len(lst), 2)

def var(lst):
    m = mean(lst)
    t = 0
    for x in lst:
        t += (x - m) ** 2
    return round(t / len(lst), 2)

def std(lst):
    v = var(lst)
    return round(v ** 0.5, 2)

def mean_centered(lst):
    m = mean(lst)
    c = []
    for x in lst:
        c.append(x-m)
    return c



###########################################################################
# Functions for Problem 6
###########################################################################
# INPUT supply and demand coefficients
# RETURN solution of quadratic equations
def equi(s,d):
    s1, s2, s3 = s
    d1, d2, d3 = d

    a = s1 - d1
    b = s2 - d2
    c = s3 - d3

    roots = q((a, b, c))

    equilibrium = []

    for root in roots:
        if type(root) == float:
            equilibrium.append(round(root, 2))

    if equilibrium:
        return tuple(equilibrium)
    else:
        return "No equilibrium point found."

##########################################################################
# Functions for Problem 7
###########################################################################
#INPUT parameters to LV model
#OUTPUT two lists history_rabbit, history_fox of populations
def rabbit_fox(br,dr,df,bf,rabbit,fox,time_limit):
    temp = 0
    rabbitHistory = []
    foxHistory = []

    while temp < time_limit:
        rabbitHistory.append(rabbit)
        foxHistory.append(fox)

        new_rabbit = rabbit + rabbit * br - rabbit * fox * dr
        new_fox = fox + bf * dr * rabbit * fox - fox * df

        rabbit = math.ceil(new_rabbit)
        fox = math.ceil(new_fox)
        temp += 1

    return rabbitHistory, foxHistory




##########################################################################
# Functions for Problem 8
###########################################################################
# INPUT container, sample size n
# OUTPUT random selection of size n in any order
# CONSTRAINT uses random 
# This is with replacement
def sub_strings(str,cnt):
    for x in range(1, len(str) + 1):
        for y in range(len(str) - x + 1):
            subString = str[y:y+x]
            if subString in cnt:
                cnt[subString] += 1
            else:
                cnt[subString] = 1

    return cnt




###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
def deposit(S,i,n):
    R = S * (i / (math.pow(1+i, n) - 1))
    return round(R, 2)


#INPUT sinking fund values except deposit
#OUTPUT a list of period, deposit, interest, accrued total fund
def sinking_fund(final_amt, r, m, y):
    i = r / m
    n = m * y
    R = deposit(final_amt, i, n)

    schedule = []
    total = 0
    for x in range(n):
        interest = round(total * i, 2)
        total += R + interest
        roundedTotal = round(total, 2)
        schedule.append([x, R, interest, roundedTotal])
    return schedule



###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT list of numbers
#OUTPUT Boolean if geometric series
def is_geometric_sequence(lst):
    if len(lst) < 3:
        return False
    r = lst[1] / lst[0]

    for x in range(2, len(lst)):
        if lst[x] != lst[x-1] * r:
            return False
        
    return True



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT portfolio of stock price, shares, market
#OUTPUT current total value
def value(portfolio, market):
    original = 0
    current = 0

    stocks = portfolio['stock']

    opx, nsx = stocks['x']
    original += opx * nsx
    cpx = market['x']  

    current += cpx * nsx
    opy, nsy = stocks['y']
    original += opy * nsy

    y_current_price = market['y']
    current += y_current_price * nsy
    change = current - original
    pc = change / original * 100

    return round(pc)



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    # #problem 1
    # print(day([14,2,2000])) # Mon
    # print(day([14,2,1963])) # Thu
    # print(day([14,2,1972])) # Mon
    # print(day([12,6,2010])) # Sat
    # print(day([1,3,1972])) # Fri

    # #problem 2
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    # #problem 3
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    # #output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122.83

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #70.53


    # #problem 4 pairs should be identical
    print(q((1,-4,-8)), q_((1,-4,-8)))
    print(q((1,3,-4)),q_((1,3,-4)))
    print(q((1, -4, 1)) , q((1, -4, 1)))
    print(q((12,-24,11)) , q((12,-24,11)))
    print(q((3,-16,1)), q((3,16,1)))

    print(c_s((1, 2, 6)), c_s((1, 2, 6)))
    print(c_s((-10,20,21)), c_s((-10, 20, 21)))
    
    # #problem 5
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(var(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    # #problem 6
    # s = (-.025,-.5,60)
    # d = (0.02,.6,20)
    # print(equi(s,d))
    
    # s = (5,7,-350)
    # d = (4,-8,1000)

    # print(equi(s,d))

    #problem 7
    # br = 0.03
    # dr = 0.0004
    # df = 0.25
    # bf = 0.11
    # rabbit = 3000  #initial population size
    # fox = 200  #initial population size
    # time_limit = 2000
    # history_rabbit, history_fox = rabbit_fox(br,dr,df,bf,rabbit,fox, time_limit)

    # # #uncomment to see time, rabbit, fox populations
    # for j in range(0,2000,200):
    #     print(j, history_rabbit[j], history_fox[j])


    # plt.plot(list(range(0,time_limit)),history_rabbit)
    # plt.plot(list(range(0,time_limit)),history_fox)
    # plt.xlabel("Time")
    # plt.ylabel("Population Size")
    # plt.legend(["Rabbit","Fox"])
    # plt.title("Lotka-Volterra Model for Rabbit & Fox")
    # plt.show()

    
    # #problem 8
    # data = ["abcabc","ccccc",""]
    # for d in data:
    #     cnt = {}
    #     sub_strings(d,cnt)
    #     print(cnt)

    # #problem 9
    # S = 30000
    # m = 4
    # r = 10/100
    # y = 2
    # for i in sinking_fund(S,r,m,y):
    #     print(i)


    #problem 10
    # data = [[1,2,4,6],[2,4,8,16],[10,30,90,270,810,2430]]
    # for d in data:
    #     print(is_geometric_sequence(d))


    #problem 11
    # portfolios =  {'A':{'stock':{'x':(41.45,45),'y':(22.20,1000)}},
    # 'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
    # market = {'x':43.00, 'y':22.50}


    # for name, portfolio in portfolios.items():
    #     print(f"{name} {value(portfolio,market)}")
