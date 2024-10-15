import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math
import sqlite3
import os
import random as rn
import matplotlib

#problem 1
#translates a random int into a step along the random walk
#parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
#numpy array y for tracking the forward/backward location at index i
#return: none
def step(x,y,i):
    direction = rn.randint(1,4) #leave this
    if direction == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif direction == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif direction == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

#Do not change -- visualization
def graphit(x,y,n):
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.show() 

#Problem 2
#Abs and pow methods you must complete
class Complex_Number:
    def __init__(self, rpart, ipart):
        self.rpart = rpart
        self.ipart = ipart
        self.cn = [self.rpart, self.ipart]
    
    def get_real(self):
        return self.rpart
    
    def get_imag(self):
        return self.ipart
    
    def __str__(self):
        sign_ = "+" if self.ipart >= 0 else "-"
        if self.rpart != 0:
            return f"({self.rpart}{sign_}{abs(self.ipart)}j)"
        else:
            return f"{abs(self.ipart)}j"

    def __add__(self,ix):
        real_part = self.get_real() + ix.get_real()
        imag_part = self.get_imag() + ix.get_imag()
        iy = Complex_Number(real_part, imag_part)
        return iy
    
    def __mul__(self,other):
        real_part = self.get_real()*other.get_real() - self.get_imag()*other.get_imag()
        imag_part = self.get_real()*other.get_imag() + self.get_imag()*other.get_real()
        iy = Complex_Number(real_part, imag_part)
        return iy

    #calculates the modulus of the self MyComplexNumber
    #parameters: MyComplexNumber self
    #return: the value of the modulus
    def __abs__(self):
        return (self.rpart ** 2 + self.ipart ** 2) ** 0.5
    
    #calculates the powers -- you should use multiplication and return a new instance
    #x**0 = 1, x**1 = x, ...
    def __pow__(self,exponent):
        total = Complex_Number(1, 0)
        for x in range(exponent):
            total = total * self
        return total


def mandelbrot(z,MAX_ITER):
    n = 0
    lz = Complex_Number(0,0)
    c = Complex_Number(-0.1, 0.65)
    while abs(z) <= 10 and n < MAX_ITER:
        z = z**2 + lz + c
        lz = z
        n += 1
    return n/MAX_ITER

#Problem 3
# Complete the query functions
# Uncomment when working on this problem
# os.chdir("/Users/brettdutka/C200-Assignments-bcdutka/Assignment9/")
# connection = sqlite3.connect("mydatabase.db")
# my_cursor = connection.cursor()
# my_cursor.execute('''DROP TABLE Weather''')
# my_cursor.execute(''' CREATE TABLE Weather (City text, State text, High real, Low real)''')

# my_cursor.execute("INSERT INTO Weather Values('Phoenix', 'Arizona', 105, 90)")
# my_cursor.execute("INSERT INTO Weather Values('Tucson', 'Arizona', 101, 92)")
# my_cursor.execute("INSERT INTO Weather Values('Flag Staff', 'Arizona', 105, 90)")
# my_cursor.execute("INSERT INTO Weather Values('San Diego', 'California', 77, 60)")
# my_cursor.execute("INSERT INTO Weather Values('Albuquerque', 'New Mexico', 80, 72)")
# my_cursor.execute("INSERT INTO Weather Values('Nome', 'Alaska', 64 ,-54)")

# data = [
#     ('Phoenix', 'Arizona', 105, 90),('Tucson', 'Arizona', 101, 92),
#     ('Flag Staff', 'Arizona', 105, 90), ('San Diego', 'California', 77, 60),
#     ('Albuquerque', 'New Mexico', 80, 72), ('Nome', 'Alaska', 64 ,-54)
# ]

def query1(db_cursor):
    return db_cursor.execute("SELECT * FROM Weather").fetchall()

def query2(db_cursor):
    return db_cursor.execute("SELECT * FROM Weather WHERE High < 80").fetchall()

def query3(db_cursor):
    l = db_cursor.execute("SELECT Low FROM Weather WHERE City='Albuquerque'").fetchone()[0]
    cities = [i[0] for i in db_cursor.execute(f"SELECT City FROM Weather WHERE Low > {l}")]
    return [[city] for city in cities]

def query4(db_cursor):
    city, l = db_cursor.execute("SELECT City, Low FROM Weather ORDER BY Low ASC LIMIT 1").fetchone()
    return [[city, l]]

def query5(db_cursor):
    h = db_cursor.execute("SELECT High FROM Weather ORDER BY High DESC LIMIT 1").fetchone()[0]
    return db_cursor.execute(f"SELECT City, High FROM Weather WHERE High = {h}").fetchall()

def query6(db_cursor):
    avgHigh = db_cursor.execute("SELECT AVG(High) FROM Weather").fetchone()[0] 
    avgLow = db_cursor.execute("SELECT AVG(Low) FROM Weather").fetchone()[0]
    return [(avgHigh, avgLow)]

def query7(db_cursor):
    return db_cursor.execute("SELECT Low, COUNT(Low) FROM Weather GROUP BY Low").fetchall()

#TEST CASES
if __name__ == "__main__":

    #problem 1
    # #PROBLEM 1
    # #number of steps
    # n = 100000   #You should change the number of steps to see
    #             #to see how it affects the plot
    # x = np.zeros(n) 
    # y = np.zeros(n) 

    # #fill array with step values 
    # for i in range(1,n):
    #     step(x,y,i)
    # graphit(x,y,n)


    #problem 2
    # x1 = Complex_Number(1,2)
    # y1 = complex(1,2)
    # print(x1,y1)
    # print(abs(x1),abs(y1))
    # for i in range(6):
    #     print(x1**i,y1**i)
    # MAX_ITER = 300
    # width, height = 500, 500
    # xmin,xmax = -1.5,1.5 # -2.0,.5
    # xwidth = xmax - xmin 
    # ymin, ymax = -1.5, 1.5 # -1.0,2.0
    # yheight = ymax - ymin - 1

    # m_ = np.zeros((width, height))
    # X = list(range(width))
    # for x in range(width):
    #     for y in range(height):
    #         X,Y = (x / width) * xwidth + xmin,  (y / height) * yheight + ymin
    #         z = Complex_Number(X,Y)
    #         v = mandelbrot(z,MAX_ITER)
    #         m_[x,y] = math.log(v)*math.atanh(v)


    # fig, ax = plt.subplots()
    # ax.imshow(m_, aspect='equal', interpolation='nearest', cmap=cm.twilight, )
    # # ax.imshow(m_, cmap="PuOr")
    # plt.axis ('off')
    # plt.show()


    #problem 3
    #  QUERY 1 Select all the tuples
    # print("Query 1")
    # print(query1(my_cursor))
    # print("List Comprehension: ", data)


    # # QUERY 2 
    # # Select All the tuples where the high temperature is less than 80
    # print("\nQuery 2")
    # print(query2(my_cursor))
    # print("List Comprehension: ", [d for d in data if d[2] < 80 ])


    # # QUERY 3 
    # # Select All the cities where the low temperature is greater than the low of Albuquerque 
    # print("\nQuery 3")
    # print(query3(my_cursor))
    # print("List Comprehension: ",[d[0] for d in data if d[3] > [d[3] for d in data if d[0] == 'Albuquerque'][0]])


    # # QUERY 4 
    # # Select the city and temperature with the smallest low temperature 
    # print("\nQuery 4")
    # print(query4(my_cursor))
    # print("List Comprehension: ",[(d[0],d[3]) for d in data if d[3] in (sorted(data, key = lambda x:x[3])[0])])


    # # QUERY 5 
    # # Select the city temperature with the largest high temperature 
    # print("\nQuery 5")
    # print(query5(my_cursor))
    # print("List Comprehension: ",[(d[0],d[2]) for d in data if d[2] in (sorted(data, key = lambda x:x[2],reverse=True)[0])])


    # # QUERY 6 
    # # Display the average High and Low temperatures
    # # You are not allowed to use Avg()
    # print("\nQuery 6")
    # print(query6(my_cursor))
    # print("List Comprehension: ", [(sum([d[2] for d in data])/len(data),sum([d[3] for d in data])/len(data))])


    # # QUERY 7 
    # # Give the counts of cities by their Low temperatures
    # print("\nQuery 7")
    # print(query7(my_cursor))
    # print("List Comprehension: ", [(i,list(map((lambda x: x[3]),data)).count(i)) for i in set(map((lambda x: x[3]),data))])

    # connection.close()
    print()