"""author: Nadav and Dad.
this program will generate a list and identify it as palindromic or non-palindromic"""


"""The following code is Nadav's code for generating a random list and generating a palindromic list"""

# These steps will create a random list

# create an empty list
list = []
# randomize the length:  how many elements will be in the last (let's say keep it under 100)

import random
# random number generator.  rand_num is a variable giving a random number
rand_num = random.randint(1,101)

for x in range (rand_num):
    rand_num = random.randint(1, 101)
    list.append(rand_num)

print (list)

#your job is to create a random but palindromic list that is between one and 100 elements long.
#make a new random number generator that makes number sets between 1 and 50 elements.
# create an empty list called palindrome_list
# Then you are going to figure out a way to put those numbers into a new list two times:
#   Once in the order they were created
#   then again in the reverse of that order.


# This new folder will be the palindromic list.

# For example, create a list that is [3, 5, 4]
#
# create code that will append [3, 5, 4, 4, 5, 3] to a new list

# create a random number generator that will create the elements of the list
# append the random number "rand_num" amount of times to the list

