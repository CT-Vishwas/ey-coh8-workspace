# define a function to read a csvfile and return its contents
import csv
import tracemalloc

def measure_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return result, current, peak
    return wrapper

@measure_memory
def read_csv_file(file_path):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.

    :param file_path: Path to the CSV file
    :return: List of dictionaries representing the rows in the CSV file
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# define a function to read a csvfile and return its contents as a generator
@measure_memory
def read_csv_file_generator(file_path):
    """
    Reads a CSV file and yields its contents as dictionaries.

    :param file_path: Path to the CSV file
    :yield: Dictionary representing a row in the CSV file
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

# test the functions
if __name__ == "__main__":
    file_path = "data\\swiggy.csv"  # Replace with your CSV file path

    # Test read_csv_file function
    csv_data, current, peak = read_csv_file(file_path)
    print("Contents of the CSV file (as list):")
    for row in csv_data:
        # print(row)
        pass
    print(f"Memory usage: current={current}, peak={peak}")

    # Test read_csv_file_generator function
    print("\nContents of the CSV file (as generator):")
    csv_data_gen, current_gen, peak_gen = read_csv_file_generator(file_path)
    for row in csv_data_gen:
        # print(row)
        pass
    print(f"Memory usage: current={current_gen}, peak={peak_gen}")