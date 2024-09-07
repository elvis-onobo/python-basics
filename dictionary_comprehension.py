
dict = { 'a': 'apple', 'b': 'ball', 'c': 'cat' }

keys = {item for item in dict}
print(keys)

values = {item for item in dict} # get the values instead of the keys
print(values)

squares = {x: x**2 for x in range(10)}
print(squares)