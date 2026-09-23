# Create a csv read and generate row function
import csv
import os
from pathlib import Path

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield row

if __name__ == "__main__":
    current_dir = os.getcwd()
    file_path = Path(current_dir) /"data"/ "swiggy.csv"  # Replace with your CSV file path
    fh = read_csv(file_path)
    # Read only 10 lines
    for i, row in enumerate(fh):
        if i >= 10:
            break
        print(row)