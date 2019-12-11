"""author: Nadav and Dad.
this program will generate a list and identify it as palindromic or non-palindromic"""


"""The following code is Nadav's code for generating a random list and generating a palindromic list"""

# These steps will create a random list

# create an empty list
list = []
# randomize the length:  how many elements will be in the last (let's say keep it under 100)

import random
# random number generator.  rand_num is a variable giving a random number
rand_num_gen = random.randint(1,101)

for x in range (5):
    rand_num_gen = random.randint(1, 101)
    list.append(rand_num_gen)


print (list)

""""The code up until this point gives a list of 5 random numbers between 1 and 100.  Your job is to create a palindromic list of 10 numbers.""""
# create an empty list called palindrome_list
# Then you are going to figure out a way to append the random numbers from [list] into [palindrome_list] two times:
#   Once in the order they were created
#   then again in the reverse of that order.


# This new folder will be the palindromic list.

# For example, create a list that is [3, 5, 4]
#
# create code that will append [3, 5, 4, 4, 5, 3] to a new list

# create a random number generator that will create the elements of the list
# append the random number "rand_num" amount of times to the list

