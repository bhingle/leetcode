#Variables create the reference
# numbers = [1,2,3,4,5]
# new_numbers = numbers
# new_numbers[0] = 9
# print("numbers list", numbers)
# print("id of numbers",id(numbers))
# print("numbers list", new_numbers)
# print("id of numbers",id(new_numbers))

# output
# numbers list [9, 2, 3, 4, 5]
# id of numbers 2016434595456
# numbers list [9, 2, 3, 4, 5]
# id of numbers 2016434595456

##########################################################################

#shallow copy
# import copy
# old_list = [[1,2,3], [4,5,6],[7,8,9]]
# new_list = copy.copy(old_list)
# new_list[0] = ['a','b','c']
# print("old list ",old_list)
# print("new list ",new_list)

# output
# old list  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new list  [['a', 'b', 'c'], [4, 5, 6], [7, 8, 9]]

############################################################################

#shallow copy creates a copy of the object but referenes each element of object
# import copy
# old_list = [[1,2,3], [4,5,6],[7,8,9]]
# new_list = copy.copy(old_list)
# new_list[0][2] = 'c'
# print("old list ",old_list)
# print("new list ",new_list)

# output
# old list  [[1, 2, 'c'], [4, 5, 6], [7, 8, 9]]
# new list  [[1, 2, 'c'], [4, 5, 6], [7, 8, 9]]

##############################################################################
#deepcopy creates copy of the object and the elements of the objects
# import copy
# old_list = [[1,2,3], [4,5,6],[7,8,9]]
# new_list = copy.deepcopy(old_list)
# new_list[0][2] = 'c'
# print("old list ",old_list)
# print("new list ",new_list)

# output
# old list  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new list  [[1, 2, 'c'], [4, 5, 6], [7, 8, 9]]