
fruits = ["apple", "orange", "banana"]
print(fruits[1])

# adding an item to the list
fruits.append("banana")
print(fruits)

# remove the first item from the list if calld without a value. If called with a value, removes that value.
fruits.remove("orange")
print(fruits)

# count the number of occurences of a value
number_of_items_in_list = fruits.count("banana")
print(f"There are {number_of_items_in_list} fruits in the list.")

# returns a copy of the list
copy_list = fruits.copy()
print(f"copy of the list is {copy_list}")

# join another list to a current list
fruits.extend(["grape", "mango"])
print(fruits)

# insert an item at a specific index
fruits.insert(1, "kiwi")
print(fruits)

# get the index of a specified item
index_of_banana = fruits.index("banana")
print(f"Banana is at index {index_of_banana}")

# reverse the order of the list
fruits.reverse()
print(fruits)

# sort the list in ascending order
fruits.sort()
print(fruits)

# sort the list in descending order
fruits.sort(reverse=True)
print(fruits)

# remove the last item from the list
fruits.pop()
print(fruits)

# remove a range of items from the list
fruits.pop(0)
print(fruits)

# remove duplicates from the list
fruits = list(set(fruits))
print(fruits)

# check if an item is in the list
print("banana" in fruits)
print("mango" in fruits)

# create a new list from a slice of another list
new_list = fruits[1:3]
print(new_list)

# remove all items from a specific range in the list
fruits = ["apple", "banana", "orange", "kiwi", "grape"]
fruits[1:3] = []
print(fruits)

# remove all items from the list
fruits.clear()