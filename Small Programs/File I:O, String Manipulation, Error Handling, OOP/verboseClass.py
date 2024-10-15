

class Example: # A class

    # This is the constructor. When you create an instance, this is the first function called. 
    def __init__(self, p1, p2, p3): # parameters passed in
        """
        Doc Comment
        """
        self.ip1 = p1 # Assigning parameters to instance variables
        # Instance variable names don't have to line up with 
        self.ip2 = p2
        if p3 == 0:
            self.tomato = "alpha"
        elif p3 == 1:
            self.tomato = "beta"
        else:
            self.tomato = "charlie"
        
    def __eq__(self, o1):
        """
        Known as a magic function that handles comparing 2 instances of classes

        Example:
        ```
        e1 = Example(1, 2, 3)
        e2 = Example(2, 2, 2)
        print(e1 == e2) # Will give back false
        ```
        """
        return self.ip1 == o1.ip1 and self.ip2 == o1.ip2 and self.tomato == o1.tomato
    
    def __str__(self):
        """
        String representation of the class

        Something displayed for a human. 

        This function **must** return a string. 

        It does **not** print
        """
        return "Example class with {} {} {}".format(self.ip1, self.ip2, self.tomato)
    
    def aFunction(self, someValue):
        """
        This is an instance function. A function that works off of the information in the instance
        """
        # You can do more than one line, the examples are just tiny
        if someValue == self.ip1 + self.ip2:
            self.tomato = "hotel"
         
        # These functions don't always have to return but they can

    def updateIp2(self, value):
        """
        Another instance function 

        In programming, you normally see getters and setters.

        Python allows you to modify instance variables outside of the class 
        (example will be shown below outside of this function)
        """
        self.ip2 = value
    
    def getID(self):
        """
        This function here is to demonstrate `self`. 

        This will return the "memory id" of the self variable, showing it is the same as the instance that 
        called this function
        """
        return id(self)




anInstance1 = Example(1, 2, 3) # This is an instance of the class Example. 
anInstance2 = Example(2, 2, 2)

print("Example1: " + str(anInstance1)) 
# Should get: 
# > Example1: Example class with 1 2 charlie
# 
# If you comment out the __str__ function, you will get something harder to decipher. 
#   When you make your own class, python will not have a clue on how to display it as a string. 
#   So you might get something like this
# > Example1: <__main__.Example object at 0x0183E700>
#   NOTE: the numbers after at will be different

print("Example2: " + str(anInstance2))

# This does comparison
print("Are they the same: {}".format(anInstance1 == anInstance2))

# Here, you can show that self is specific to an instance
print("Memory ID showing instances:", id(anInstance1), anInstance1.getID(), id(anInstance1) == anInstance1.getID())

# You can update the values 2 ways
# With a setter
print()
print()
print("Updating values")
print(anInstance1)
anInstance1.updateIp2(4)
print(anInstance1)
anInstance1.ip2 = 5
print(anInstance1)

print()
print()
print("Updating values with another function")
print(anInstance2)
anInstance2.aFunction(4)
print(anInstance2)