from threading import Thread
import time
from tqdm import tqdm


global storage
store = {}

def threaded_function(arg):


if __name__ == "__main__":
    global thread
    old = time.time()

    t = []
    for i in range(10):
        thread = Thread(target = threaded_function, args = (100000,), i*chunk_size)
        t.append(thread)
        thread.start()

    for thread in t:
        thread.join()

    now = time.time()
    print(now-old)
