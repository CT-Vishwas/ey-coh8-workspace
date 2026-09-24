# Write functions to take input and calculate number of lines,words, characters, punctuation marks, digits
import string
from pathlib import Path

SUMMARY_LOG = "summary_log.txt"
def summarize_text(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)
    num_punctuations = sum(1 for char in text if char in string.punctuation)
    num_digits = sum(1 for char in text if char.isdigit())
    return {
        "lines": num_lines,
        "words": num_words,
        "characters": num_chars,
        "punctuation_marks": num_punctuations,
        "digits": num_digits
    }

# def a function to append the summary to a file
def append_summary_to_file(filename, summary):
    with open(filename, 'a') as file:
        file.write("\nSummary:"+ filename +"\n")
        file.write(f"Lines: {summary['lines']}\n")
        file.write(f"Words: {summary['words']}\n")
        file.write(f"Characters: {summary['characters']}\n")
        file.write(f"Punctuation Marks: {summary['punctuation_marks']}\n")
        file.write(f"Digits: {summary['digits']}\n")
        file.write("\n")
        file.write("="*40 + "\n")


if __name__ == "__main__":
    # Take filename as input and read the content
    file_path = Path(input("Enter the filename: "))
    filename = file_path.name
    with open(file_path, 'r') as file:
        text = file.read()
    summary = summarize_text(text)
    print("\nSummary:")
    print(f"Lines: {summary['lines']}")
    print(f"Words: {summary['words']}")
    print(f"Characters: {summary['characters']}")
    print(f"Punctuation Marks: {summary['punctuation_marks']}")
    print(f"Digits: {summary['digits']}")
    # Append the summary to the file
    append_summary_to_file(SUMMARY_LOG, summary)