import tracemalloc
import time

def measure_memory(func):
    '''Decorator to measure the memory usage of a function.'''
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return result, current, peak
    return wrapper

def timing(func):
    '''Decorator to measure the execution time of a function.'''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    return wrapper