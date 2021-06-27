# Curs 2

# a = 7
# b = 7
# print(a is b, id(a), id(b))
#
# a = [1,2]
# b = [1,2]
# print(a is b, id(a), id(b))
#
# print(ord('3')) # str to ASCII
# print(chr(51)) # ASCII to int
#
# print("linia1linia2 linia 3", sep='\n')

# Strings
# price = 20.00
# name = 'Burger'
# msg = 'Top product: {name} costs only ${price:.2f}.'.format(name=name,price=price)
# print('msg', msg)
# msg2 =f'Top product: {name} costs only ${price:.2f}.'
# print('msg2', msg2)
# msg3 = 'Top product %s costs only $%.2f.' % (name, price)
# print('msg3',msg3)
#
# # Lists
# my_list=[1,2, True, 'abc']
# print(my_list, type(my_list))
# print(2 not in my_list)
#
# # Indexing
# print(my_list[0])
# print(my_list[2])
# print(len(my_list))
# print((my_list[-1]))
#
# # Slicing -> new list [start:stop:step]
# new_list = my_list[::] # the same as my_list[0:len(my_list):1]
# print(new_list)
#
# my_list[2] = False
# print(my_list)
#
# my_list[2] = ['a', [1,2], 'bcd']
# print(my_list[2][1][1])
#
# my_list = my_list[::-1]
# print(my_list)

# Tuples
# my_list = [1,2,3]
# my_list = tuple(my_list)
# print(my_list, type(my_list), id(my_list))
#
# my_tuple = (1,2,3)
# print(my_tuple, type(my_tuple), id(my_tuple))
# my_tuple = list(my_tuple)
# print(my_tuple, type(my_tuple),id(my_tuple))
# my_tuple.append(4)
# print(my_tuple, type(my_tuple), id(my_tuple))

# Dictionaries
# my_dict = {'a': 12, 'b': 'abc', 3:22,
#            'abc':15,
#            (1,2,3):[1,2,3],
#            'dict_in_dict':{'a':1, 'b':2}}
# print(my_dict, type(my_dict))
# print(my_dict['a'])
# print(my_dict['b'])
# print(my_dict[3])
# print(my_dict.get('abc', 'my default value'))
# print('abc' in my_dict and my_dict['abc'] == 22)
# print(my_dict.get('abc', None) == 22)
#
#
# students = [{
#     'name': 'Name 1',
#     'age': 29,
#     'address': {
#         'street':'Str',
#         'city': 'Cluj'
#     }
# }]
# print('students', students)
# print('1st student', students[0], type(students[0]))
#
# print('\nlist of keys', list(students[0].keys()))
# print('values', students[0].values())
# print('items', students[0].items())

# my_dict = {}
# print(my_dict, type(my_dict))
# my_dict['a'] = 2
# print(my_dict, type(my_dict))
# my_dict['b'] = 10
# print(my_dict, type(my_dict))
# my_dict['c'] = 100
# print(my_dict, type(my_dict))
#
# my_dict = dict([('a',dict([('d',400)])), ('b', 200), ('c', 300)])
# print(my_dict, type(my_dict))
#
# empty_list = []
# empty_list_constructor = list()
# list_with_one_element = ['abc']
# list_with_one_element_with_constructor = list((1,))
# print('list_with_one_element_with_constructor', list_with_one_element_with_constructor)
#
# empty_tuple = ()
# tuple_with_one_element = (1,)
# tuple_with_constructor=tuple('abc')
# print('tuple_with_constructor', tuple_with_constructor)
#
# empty_dict= {}
# print('empty_dict', empty_dict)

# Sets
# my_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
# print('my_set', my_set)
# my_set.pop()
# print('my_set', my_set, type(my_set))
# my_set.remove(6)
# print('my_set', my_set, type(my_set))
#
# my_set = set()
# my_set.add(27)
# my_set.add(True)
# my_set.add('abc')
# print(my_set)

# grocery_list = {'mere', 'pere', 'banane', 'kiwi'}
# items = {'mere', 'kiwi', 'piersici'}
# print(items.issubset(grocery_list))
# print(grocery_list.issuperset(items))
# print(grocery_list.union(items))
# print(grocery_list.intersection(items))
# print(grocery_list.difference(items))
# print(items.difference(grocery_list))

""" curs 2"""
# print('start of program')
# my_age = input('How old are you?: ')
# my_age = int(my_age)
#
# if my_age < 18:
#     print('Persoana minora')
#     if my_age < 14:
#         print("Persoana nu are buletin")
# elif my_age < 26:
#     print("Persoana este student.")
# else:
#     print("Persoana nu este student")
#     if my_age >= 65:
#         print('Persoana este la pensie')
#
# print('end of program')

# my_list = [10, 23, 30, 45, 50]
# for item in my_list:
#     if item % 2 == 0:
#         print('Number %s is even.' % item)
#         # continue #pass control to the next iteration
#         break # pass control to the next instruction in the loop
#     else:
#         print("Number %s is odd."  % item)
#     print('end of program')

# list_index = 0
# while list_index < len(my_list): # list_index = [0,4]
#     item = my_list[list_index]
#     list_index += 1
#     if item % 2 ==0:
#         print('Number %s is even.' % item)
#         continue #pass control to the next iteration
#         #break # pass control to the next instruction in the loop
#     else:
#         print('Number %s is odd.' % item)

    # print('end of while loop', item)

# n = int(input('n: '))
# for i in range(1,n+1):
#     print('Python is awesome!', i)

# my_list = [3, 5, 8, 10,5]
#
# for index, item in list(enumerate(my_list)):
#     if item % 2 == 0:
#         print('Even element on index = %s' % index)
#     else:
#         print('odd element on index = %s' % index)
#
# my_list1 = [[1,2,3], [4,5,6],[7,8,9]]
# for main_index, list_ in enumerate(my_list1):
#     for index, element in enumerate(list_):
#         print(main_index, index, element)

# d = {
#     'name':'A',
#     'email': 'B',
#     'age': 20
# }
#
# for key in d.keys():
#     print(key, d[key])
# print('\n')
# for a in d.values():
#     print('dict value: ', a)
# print('\n')
# for k, v in d.items():
#     print(k, v)
# print('\n')
# for key in d:
#     print(key, d[key])

# d = {
#     'Jan': 10,
#     'Feb': 15,
#     'Jun': 8
# } # points = 10 + 15 + 8 = 33
# m = {'Jan', 'Jul', 'Sep', 'Oct'} # x2 => 20+15+8 => 43
# my_months = set(d.keys())
# print('my months', my_months)
# extra_points = m.intersection(my_months)
# print('extra points', extra_points)

# Functii
# def my_function(a, b | c=5):
# def my_function(a, b, *args, c=5, **kwargs):
#     print(args, kwargs)
#     return a+b+c
#
# function_result = my_function(10,20,30,40,50, c=60,d = 70, e=80, f=90)
# print('function result', function_result)

# in python parametrii sunt trimisi prin referinta
# import copy
# def my_function(l):
#     l = copy.deepcopy(l)
#     # l = l.copy()
#     print('---> l', l)
#     l[1].append(6)
#     print('----> l', l)
#
# my_list =[1,[2,3,4],5]
# my_function(my_list)

# def my_function(l):
#     def inner_function(item):
#         print(item ** 2)

#     def inner_function2(item):
#         print(item*2)

#     for i in l:
#         if i % 2 == 0:
#             inner_function(i)
#         else:
#             inner_function2(i)


# def my_function(a, b):
#     return a+b
#
#
# my_sum = my_function(5,7)
# print(my_sum)

# Namespace-uri
# print(dir(__builtins__))
# def my_function(a, b):
#     def inner_func():
#         my_sum = 20
#         print('---+---> my_sum', my_sum)
#     my_sum = a + b
#     print('my sum', my_sum)
#     inner_func()
#     return my_sum
#
# my_sum = my_function(5,7) *2
# print(my_sum)

# Tratarea exceptiilor
# my_age = input()
#
# print(my_age)
#
# print('my_age', my_age, type(my_age))
# try:
#     my_age = int(my_age)
#     print('d', d)
# except (ValueError, NameError) as e:
#     print('e--->', e)
# else:
#     print('else branch was executed')
# finally:
#     print('finally branch was executed')

# print(__name__)

