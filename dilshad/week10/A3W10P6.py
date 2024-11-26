import sys
import os


def readfiles(filenames):
    for file_name in filenames:
        if not os.path.exists(file_name):
            print(f"Error reading file: {file_name} (file not found)")
        else:
            with open(file_name, 'r') as file:
                lines = file.readlines()

                for i in range(len(lines)):
                    if lines[i].strip().startswith('def '):  # Check for function definitions
                        # Check for preceding comment
                        if i == 0 or not lines[i - 1].strip().startswith('#'):
                            function_name = lines[i].split('(')[0][4:].strip()
                            line_number = i + 1
                            print(
                                f"File: {file_name} contains a function [{function_name}()] on line [{line_number}] without a preceding comment.")


def verwerken_files():
    return input('Enter file names separated by commas: ').split(",")


if __name__ == "__main__":
    file_names = verwerken_files()
    # Corrected function call and variable names
    readfiles([name.strip() for name in file_names])
