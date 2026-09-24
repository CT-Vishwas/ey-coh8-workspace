# Use re module to extract the prices from a file and print them
import re
from pathlib import Path

def extract_prices_from_text(text):
    return re.findall(r'\$\d+(?:\.\d{2})?', text)

def extract_prices_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return extract_prices_from_text(text)

if __name__ == "__main__":
    file_path = Path(input("Enter the filename: "))
    filename = file_path.name
    prices = extract_prices_from_file(file_path)
    print(f"Prices extracted from {filename}: {prices}")