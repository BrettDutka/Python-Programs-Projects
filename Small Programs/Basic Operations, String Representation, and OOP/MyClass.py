class MySet:
    """
    This class is to practice making a data structure. 

    For easy practice, we are going to replicating Python's `set`.

    Please note: this is not going to perform as efficiently as Python's 
    `set` but will hopefully give a picture of making a class.
    """

    def __init__(self, data=None):
        """
        The constructor for making a class

        This will set-up the "behind the scenes" structure that will hold our data. 

        Assuming `data` is provided a `list`, we can add existing data to the set.
        """
        self.structure = []
        if data != None:
            # TODO: Add data
            for x in data:
                if x not in self.structure:
                    self.structure.append(x)

    def add(self, item):
        """
        Given a single item, add this to the set. 

        The item given could or could not already exist in the set.
        
        Returns:
        - True: if the item can be added to the set
        - False: if the item cannot be added to the set
        """
        if item in self.structure:
            return False
        else:
            self.structure.append(item)
            return True

    def remove(self, item):
        """
        Given a single item, remove that item from the set. 

        If the item does not exist in the set, return None

        Return:
        - item: The item to be removed
        - None: return None to provide a value back to signal the item was not removed
        """
        if item in self.structure:
            self.structure.remove(item)
            return item
        else:
            return None


    def count(self):
        """
        Return the number of unique values in the set
        """
        return len(self.structure)

    
    def __len__(self):
        """
        Return the number of unique values in the set
        """
        return self.count()
    
    
    def __str__(self):
        """
        Return the string representation of the set. 
        """
        myString = "{"
        for i in range(len(self.structure[:-1])):
            item = self.structure[i]
            myString = myString + str(item) + ", "
        
        myString += str(self.structure[-1]) + "}"
        return myString

    def __repr__(self):
        """
        Return the string representation of the set
        """
        return str(self) # Provided
    
    def __eq__(self, other):
        """
        Challenge: 

        In your free time (not required), think of a way to determine if 
        """
        return False # TODO: Independently

    def compare_with_pyset(self, pySet):
        """
        Provided method:

        This method is to show the values added to our set have similar results as adding to a set.

        """
        return sorted(list(self.structure)) == sorted(list(pySet)) # Provided



class MyFraction:
    """
    This class allows for the representation of fractions.
    """

    def __init__(self, numerator, denominator):
        """
        This class will make a fraction:

               numerator 
        ---------------------------
              denominator
        """
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self):
        """
        This function will return the fraction evaluated into a decimal
        """
        return self.numerator / self.denominator


    def __add__(self, other):
        """
        Adds 2 fractions together. 

        Handles addition by making the denominators the same by multiplying them together
        """
        if self.denominator != other.denominator:
            denom1, denom2 = self.denominator, other.denominator
            numer1, numer2 = self.numerator, other.numerator
            mult1_by, mult2_by = denom2, denom1
            numer1 *= mult1_by
            denom1 *= mult1_by
            numer2 *= mult2_by
            denom2 *= mult2_by
        
        return MyFraction(numer1 + numer2, denom1)

    def __sub__(self, other):
        """
        Subtracts 2 fractions. 

        Handles subtraction by making the denominators the same by multiplying them together
        """
        if self.denominator != other.denominator:
            denom1, denom2 = self.denominator, other.denominator
            numer1, numer2 = self.numerator, other.numerator
            mult1_by, mult2_by = denom2, denom1
            numer1 *= mult1_by
            denom1 *= mult1_by
            numer2 *= mult2_by
            denom2 *= mult2_by
        
        return MyFraction(numer1 - numer2, denom1)

    def __str__(self):
        """
        Makes a fraction representation

        Example:
        f = 4 / 5
        """
        return f"f = {self.numerator} / {self.denominator}"