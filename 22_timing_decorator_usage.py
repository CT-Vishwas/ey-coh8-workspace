from utilities.func_utils import timing

@timing
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    result, elapsed_time = example_function(100)
    print(f"Result: {result}, Elapsed Time: {elapsed_time}")