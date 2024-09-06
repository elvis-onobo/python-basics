
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} is making a sound"

    def walk(self):
        return f"{self.name} is walking"
    

if __name__ == '__main__':
    cat = Animal("Bullet")
    print(cat.make_sound())
    print(cat.name)
    print(cat.walk())



