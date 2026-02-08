"""
This module count words on files
Example:
  python word_count.py {file_path}
"""
import os
import argparse
import time

def count_words(text):
    """
    Returns most repeated value in the list of numbers received.
    
    :param numbers: List of numbers
    """
    counts = {}
    # 1. Count the number of repetitions of the values
    for word in text:
        counts[word] = counts.get(word, 0) + 1
    return counts

def read_words_from_file(filepath):
    """Reads text from a file and returns a list of words."""
    words = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    return []

def save_to_file(results, input_path, output_path):
    """Write the results in a text file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"=== Results for: {input_path} ===\n")
            f.write(f"{results}\n")
            f.write("-" * 40 + "\n")
        print("File saved successfully!")
    except IOError as e:
        print(f"Failed to save file: {e}")

def main():
    """
    Starting point of the program.
    """
    start_time = time.time()
    # 1. Initialize the ArgumentParser
    parser = argparse.ArgumentParser(
        description="Read numbers from a file and convert them to a list."
    )
    parser.add_argument("path", help="The path to the text file containing numbers", type=str)

    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Use the path parameter (accessible via args.path)
    if os.path.exists(args.path):
        text = read_words_from_file(args.path)
        word_count = count_words(text)
        output = "  WORD    |  COUNT"
        output += "===================\n"
        for word, count in word_count.items():
            output += f"{word:10} - {count:4}\n"
        print(output)
        save_to_file(output, args.path, f'{args.path}.results.txt')
    else:
        print(f"Error: The path '{args.path}' is invalid.")

if __name__ == "__main__":
    main()
