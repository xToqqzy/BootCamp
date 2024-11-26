import os


def filelezen(filename):
    if not os.path.exists(filename):
        print("File name not found")
        return

    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


def line_check(lines):
    lines_apart = []

    for line in lines:
        if line.strip().startswith('#'):  # Check for lines starting with '#'
            line = line.split('#')[0]
        lines_apart.append(line)

    return lines_apart


def new_save(lines, file_name):
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line)


def main():
    file_name = input("File name: ")
    lines = filelezen(file_name)  # Corrected function name call
    if lines:
        clean_lines = line_check(lines)
        save_name = input("Save name: ")
        new_save(clean_lines, save_name)
        print(f"File saved as {save_name}")


if __name__ == "__main__":  # Corrected condition
    main()
