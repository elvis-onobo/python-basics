from classes import Animal

class Dog(Animal): #inherits from Animal
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking!"
    

bingo = Dog("Bingo", 3)
print(bingo.name)
print(bingo.age)
print(bingo.make_sound())
print(bingo.walk())
print(bingo.bark())