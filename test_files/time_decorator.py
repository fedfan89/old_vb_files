import time

def my_time_decorator(original_function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()
        diff = t2 - t1
        print(diff)
        return result
    return(wrapper)

@my_time_decorator
def counter(number):
    for i in range(number):
        print(i)

counter(10)
