"""
This module transform decimal numbers to binary and hexadecimal
Example:
  python conver_numbers.py {file_path}
"""
import os
import argparse
import time

def decimal_to_binary(n):
    """Converts a decimal integer to a binary string."""
    if n == 0:
        return "0"
    binary = ""
    number = n
    if number < 0:
        number = number * -1
    while number > 0:
        remainder = int(number) % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary

def decimal_to_hexadecimal(n):
    """Converts a decimal integer to a hexadecimal string."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    number = n
    if number < 0:
        number = number * -1
    while number > 0:
        remainder = int(number) % 16
        hex_result = hex_chars[remainder] + hex_result
        number = number // 16
    return hex_result

def read_numbers_from_file(filepath):
    """Reads numbers from a file and returns a list of integers."""
    number_list = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue

                try:
                    # Intento de transformación
                    number = float(clean_line)
                    number_list.append(number)
                except ValueError:
                    # Si falla, informamos y continuamos con la siguiente línea
                    print(f"Line {line_num} skipped: '{clean_line}' is not a valid number.")
        return number_list
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
        result = read_numbers_from_file(args.path)
        output = ""
        for line_num, value in enumerate(result, 1):
            bin_value = decimal_to_binary(value)
            hex_value = decimal_to_hexadecimal(value)
            output += f"{line_num:5} {value} | {bin_value} | {hex_value}\n"
        execution_time = time.time() - start_time
        output += f"Total execution time {execution_time}"
        print(output)
        save_to_file(output, args.path, f'{args.path}.results.txt')
    else:
        print(f"Error: The path '{args.path}' is invalid.")

if __name__ == "__main__":
    main()
