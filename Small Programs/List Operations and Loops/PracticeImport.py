if __name__ == '__main__':
    print()
    print("Running file: {}".format(__file__))
    print()


def exampleFunction():
    print("Running function in PracticeImport")


# Will run everything in 
print("\t IMPORTING `Practice.py`")
print()
import Practice
print()
print("\t Finished IMPORTING `Practice.py`")

print("\t Calling a function in `Practice.py`")

Practice.practiceFunction()
