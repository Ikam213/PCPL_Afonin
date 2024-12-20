from contextlib import contextmanager
import time

class cm_timer_1:

    def __init__(self):
        self.begin_time = time.time()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, exc_val, exc_tb)
        else:
            print('time: ', time.time() - self.begin_time)
    
@contextmanager
def cm_timer_2():
    begin_time = time.time()
    yield 1
    print('time: ', time.time() - begin_time)
