# We want to use re module and extract Numbers from a file
# make use of pathlib to handle file paths
# make it modular
import re
from pathlib import Path


def extract_numbers_from_text(text):
    return re.findall(r'\d+', text)

def extract_numbers_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return extract_numbers_from_text(text)

if __name__ == "__main__":
    file_path = Path(input("Enter the filename: "))
    filename = file_path.name
    numbers = extract_numbers_from_file(file_path)
    print(f"Numbers extracted from {filename}: {numbers}")