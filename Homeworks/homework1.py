# Given list
given_list = [7,8,9,2,3,1,4,10,5,6]

# List sorted ascending
print(sorted(given_list))

# List sorted descending
print(sorted(given_list, reverse=True))

# Even numbers from the input list
even_numbers = given_list[1:4:2] + given_list[6:8] + given_list[-1:]
print(even_numbers)

# Odd numbers from the input list
odd_numbers = given_list[0:5:2] + given_list[5::3]
print(odd_numbers)

# Multiples of 3
multiples = given_list[2:5:2] + given_list[-1:]
print(multiples)

