
# Lab 4
# 
# In a caffeine-induced all-nighter, your coworker Charlie Blockhead Brown has pushed the
# following code to your company's github.  This code is crucial to maintaining Important
# City System, and said system has been down all night.  Charlie never took C200, and so it
# is up to you, StudentNameHere, to save the city by putting your knowledge of errors
# to the task.

def flatten(deep_list):
    """
    Takes a "deep" list of lists representing strings and converts it
    into a "flattened" string.
    
    e.g.
    flatten([['I'],
             ['l', 'o', 'v', 'e'],
             ['C', '2', '0', '0']]) 
    returns 
    "I love C200"
    
    Parameters: A list of lists containing single character strings
    Returns: A list of strings
    """
    flattened = []
    for i in range(len(deep_list)):
        for x in deep_list[i]:
            flattened += deep_list[i]

    return flattened


# I tested the code here after downing seven energy drinks.
# It works on one test, therefore it always works.
#                                - Charlie Blockhead Brown
print(flatten([['I'],['l', 'o', 'v', 'e'],
               ['C', '2', '0', '0']]))


