# Threading allows multiple threads to run concurrently. This is useful for I/O inbound tasks

import threading

def print_numbers():
    for i in range(5):
        print(i)


thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
print(thread.is_alive())