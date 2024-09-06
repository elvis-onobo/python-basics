
# sets are an unordered list of unique values
unique_elemets = {1,2,2,3,4,5,5,5}
print(unique_elemets)

unique_elemets.add(6)
print(unique_elemets)

#
union = unique_elemets.union({7, 8, 9})
print(union)

unique_elemets.remove(5)
print(unique_elemets)

# check if an item is in the set
print(6 in unique_elemets)

copy_union = union.copy()



unique_elemets.clear()