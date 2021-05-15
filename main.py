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

