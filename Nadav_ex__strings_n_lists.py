"""Practice indexing strings"""

test_list = [5, 10, 15, 20, 25, 30, 35, 40]

print (test_list[5])

# print the first item
# cardinally (by counting places) in the list
print (test_list[0])
print (test_list[0:2])
print (test_list[5:])
print (test_list[:-5])

# print the first three items in the list
#
# print from the third item to the end of the list
# without using the place number of the last item

new_list = []
num = 0
for i in range (0,50):
    new_list.append(i)
print (new_list)
print (new_list[4:22])
print (new_list[4:22:2])
print (new_list[4:22:4])

#("hello" is like a list [h,e,l,l,o]

string = "hello"
for c in string: print (c)


# your assignment
#
# complete each one
#
# make a list with at least 20 items
# print the first item in the list
# print the first five items in the list
# print the last item
# print the 6th item to the 15th item
# print form the beginning to the end
# from the beginning to numer 14
# from number 7 to the end