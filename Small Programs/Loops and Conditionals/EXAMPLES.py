
"""
This takes an starting height in feet and increments until you have an height that can ride rollercoasters.

Args: Takes a height that is required for the rollercoaster

Returns: Should print the height and whether you are able to ride the roller coaster.
    
"""
def rollerCoaster(height):
    for i in range(8):
        while i < height:
            print("You are " + str(i) + " feet tall, you cannot ride the coaster.") 
            break
        else: 
            print("You are " + str(i) + " feet tall. You are tall enough.")

"""
Counts up to a number non-inclusive. Each time the loop runs, you count higher by one number. 
eg: 1, 12, 123, 1234, etc

Args:
    (int) count: number you want to count up to non-inclusive

Returns:
    prints out numbers from 0 to count-1, each time with one number higher
"""
def countingUp(count):
    for i in range(count):
        counter = 0
        while counter != i:
            counter += 1
            print(counter, end=" ")
        print()

"""
Prints each name in the list five times in a row

Args: 
    (list) nameList: list of names

Returns:
    Prints names five times a row
"""


def names(nameList):
    for i in nameList:
        count = 0
        while count < 5:
            print(i, end=" ")
            count = count + 1
        print()

"""
Your parents have implemented a limit on how much you can use your phone.
This function takes a hour limit and locks the phone once you've reached a hour limit.

Args: 
    (int) limit: How many hours you can use your phone

Returns:
    While you are using your phone, it will print how many hours you've used it for.
    Once your hour limit is reached, you will print a string saying that the phone is locked
"""

def phoneUsageLimiter(limit):
    hours = 0
    while hours < limit:
        for i in range(limit):
            hours += 1
            print("You've used your phone for " + str(hours) + " hours.")
    print("Your phone is locked")

    
if __name__ == "__main__":
    namesList = ['Parichit', 'Dr Dalkilic', 'Proj Hmeljak']
    names(namesList)
    countingUp(10)
    rollerCoaster(3)
    phoneUsageLimiter(3)
"""
This takes an starting height in feet and increments until you have an height that can ride rollercoasters.

Args: Takes a height that is required for the rollercoaster

Returns: Should print the height and whether you are able to ride the roller coaster.
    
"""
def rollerCoaster(height):
    for i in range(8):
        while i < height:
            print("You are " + str(i) + " feet tall, you cannot ride the coaster.") 
            break
        else: 
            print("You are " + str(i) + " feet tall. You are tall enough.")

"""
Counts up to a number non-inclusive. Each time the loop runs, you count higher by one number. 
eg: 1, 12, 123, 1234, etc

Args:
    (int) count: number you want to count up to non-inclusive

Returns:
    prints out numbers from 0 to count-1, each time with one number higher
"""
def countingUp(count):
    for i in range(count):
        counter = 0
        while counter != i:
            counter += 1
            print(counter, end=" ")
        print()

"""
Prints each name in the list five times in a row

Args: 
    (list) nameList: list of names

Returns:
    Prints names five times a row
"""


def names(nameList):
    for i in nameList:
        count = 0
        while count < 5:
            print(i, end=" ")
            count = count + 1
        print()

"""
Your parents have implemented a limit on how much you can use your phone.
This function takes a hour limit and locks the phone once you've reached a hour limit.

Args: 
    (int) limit: How many hours you can use your phone

Returns:
    While you are using your phone, it will print how many hours you've used it for.
    Once your hour limit is reached, you will print a string saying that the phone is locked
"""

def phoneUsageLimiter(limit):
    hours = 0
    while hours < limit:
        for i in range(limit):
            hours += 1
            print("You've used your phone for " + str(hours) + " hours.")
    print("Your phone is locked")

    
if __name__ == "__main__":
    namesList = ['Parichit', 'Dr Dalkilic', 'Proj Hmeljak']
    names(namesList)
    countingUp(10)
    rollerCoaster(3)
    phoneUsageLimiter(3)
