# Dictionary with ten elements
my_dict = {'apple': 2, 'banana': 5, 'orange': 3, 'grape': 1, 'peach': 3, 'pear': 6, 'kiwi': 2, 'mango': 5, 'pineapple': 3, 'watermelon': 1}

# List with ten elements
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# Tuple with ten elements
my_tuple = ('red', 'green', 'blue', 'yellow', 'purple', 'pink', 'orange', 'black', 'white', 'gray')

print(next(filter(lambda x: x % 2 == 0, my_list)))

key, value = next(filter(lambda item: item[1] == 3, my_dict.items()))
print(key, value)

val = next(filter(lambda x: len(x) == 4, my_tuple))
print(val, my_tuple.index(val))
