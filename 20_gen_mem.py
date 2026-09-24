from utilities.func_utils import measure_memory
m = 100
# simple function to run a loop and return the total

@measure_memory
def calculate_total(n):
    total = 0
    for i in range(n):
        total += i
    return total

@measure_memory
def list_version(n):
    return sum([i for i in range(n)])

@measure_memory
def generator_version(n):
    return sum(i for i in range(n))


if __name__ == "__main__":
    # n = int(input("Enter a number: "))
    n = 100_00_000
    total, current, peak = calculate_total(n)
    print(f"Total using loop: {total}, Current memory: {current}, Peak memory: {peak}")

    total, current, peak = list_version(n)
    print(f"Total using list comprehension: {total}, Current memory: {current}, Peak memory: {peak}")

    total, current, peak = generator_version(n)
    print(f"Total using generator expression: {total}, Current memory: {current}, Peak memory: {peak}")