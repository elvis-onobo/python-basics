# decorators modify or enhance functions or methods

def my_decorator(func):
    print("before calling function")
    func()
    print("after calling function")


@my_decorator
def say_hello():
    print("hello")