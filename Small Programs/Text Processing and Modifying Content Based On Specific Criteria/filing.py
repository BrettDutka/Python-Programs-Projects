import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()




def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    someFile = open("Laboratory/Lab7/blank.txt","r")
    contents = someFile.read()
    someFile.close()
    return contents



def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    someFile = open("Laboratory/Lab7/blank.txt","r")
    contents = someFile.readlines()
    someFile.close()
    return contents


def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    stuff = ["a", "b", "c", "d", "e", "f"]
    fileToWrite = open("Laboratory/Lab7/wrong.txt", "w")
    for s in stuff:
        fileToWrite.write(s + "\n")
    fileToWrite.close()


def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    fileToWrite = open("Laboratory/Lab7/wrong.txt", "a")
    for s in range(4):
        fileToWrite.write("more\n")
    fileToWrite.close()



def FileIO_example(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    with open(filePath) as theFile:
        originalContents = theFile.read()
    splitted_lines = originalContents.split("\n")
    count = 0
    goodLines = []
    for line in splitted_lines:
        splitted_vocabs = line.split(" ")
        if len(splitted_vocabs) <= 5:
            count += 1
        else:
            goodLines.append(line.strip())

    with open(newFile, "w") as toWrite:
        for line in goodLines:
            toWrite.write(line)
            toWrite.write("\n")
    return count


def calculation(filePath):
    '''
    Given a file path, we want to open the file, read each line. in each line we have a number
    we want to calculate the summation of numbers in last 2 lines and write the sum at the end of the 
    file we read from it. (eah time that we run this function we add one number of fibonacci series to the file)
    '''
    with open(filePath) as theFile:
        originalContents = theFile.read()
    
    splitted_lines = originalContents.split("\n")

    sum = 0
    size = len(splitted_lines)
    sum = int(splitted_lines[size - 2]) + int(splitted_lines[size - 1])
    with open(filePath, "a") as toWrite:
        toWrite.write("\n")
        toWrite.write(str(sum))
        


if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example("Laboratory/Lab7/testing.data", "Laboratory/Lab7/clean.txt")))

    calculation("Laboratory/Lab7/calculation.txt")