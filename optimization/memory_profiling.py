# this helps you understand and optimize the memory usage in your application

from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(10000)]
    return a

my_function()