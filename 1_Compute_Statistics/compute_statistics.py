"""
This module calculate different statistics value for a file of numbers
Example:
  python compute_statistics.py {file_path}
"""
import os
import argparse
import time

def calculate_mean(numbers):
    """
    Returns mean value of the numbers received.
    
    :param numbers: List of numbers
    """
    total = 0.0
    count = 0.0
    for num in numbers:
        total = total + num
        count = count + 1
    return total / count

def calculate_median(numbers):
    """
    Returns median value of the numbers received.
    
    :param numbers: List of numbers
    """
    # 1. Sort the list
    sorted_list = sorted(numbers)
    # 2. Find the middle index
    n = len(numbers)
    mid = n // 2
    # 3. Get the middle value, if value is pair get the mean of the two middle values
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        median = float(sorted_list[mid])

    return median

def calculate_mode(numbers):
    """
    Returns most repeated value in the list of numbers received.
    
    :param numbers: List of numbers
    """
    counts = {}
    # 1. Count the number of repetitions of the values
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    # 2. Get the most repeated value
    max_freq = 0
    mode_value = None
    for num, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            mode_value = num
    return mode_value

def calculate_variance(numbers):
    """
    Calculates and returns the variance of the list of numbers received
    
    :param numbers: List of numbers
    """
    mean = calculate_mean(numbers)
    n = len(numbers)
    squared_diff_sum = 0
    for num in numbers:
        squared_diff_sum += (num - mean) ** 2
    return squared_diff_sum / n

def calculate_standard_deviation(numbers):
    """
    Calculates and returns the Standard deviation of the list of numbers received
    
    :param numbers: List of numbers
    """
    return calculate_variance(numbers) ** 0.5


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
        mean = calculate_mean(result)
        median = calculate_median(result)
        mode = calculate_mode(result)
        sd = calculate_standard_deviation(result)
        variance = calculate_variance(result)
        execution_time = time.time() - start_time
        output = f"COUNT: {len(result)}\n"
        output += f"MEAN: {mean}\n"
        output += f"MEDIAN: {median}\n"
        output += f"MODE: {mode}\n"
        output += f"SD: {sd}\n"
        output += f"Variance: {variance}\n"
        output += f"Total execution time {execution_time}"
        print(output)
        save_to_file(output, args.path, f'{args.path}.results.txt')
    else:
        print(f"Error: The path '{args.path}' is invalid.")

if __name__ == "__main__":
    main()
