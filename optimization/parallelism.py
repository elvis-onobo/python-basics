# Allows you to  run multiple processes in parallel. Suitable for CPU bound tasks.

from multiprocessing import Process

def print_hello():
    print("Hello World!")


if __name__ == "__main__":
    process = Process(target=print_hello)
    process.start()
    process.join()
    print(process.is_alive())
    

