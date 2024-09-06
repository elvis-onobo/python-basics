
person = {"name": "John", "surname": "Snow", "age": 30, "gender": "male"}
print(person.get('name'))
print(person['surname'])
person["age"] = 31
print(person.get('age'))
print(person)

# remove the item with the key from the dictionary
person.pop('gender')
print(person)

person_copy = person.copy()
print(person_copy)

dict_from_keys = person_copy.fromkeys('name', 'age')
print(dict_from_keys)

items = person.items()
print(f"items: {items}")

keys = person.keys()
print(f"keys: {keys}")

updated = person.update(age=32)
print(f"updated: {person}")

values = person.values()
print(f"values: {values}")

default = person.setdefault('name', 'El')
print(f"person {person}")

person.clear()
