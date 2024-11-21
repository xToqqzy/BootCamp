import sys


def tail(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()[-10:]
            for line in lines:
                print(line.strip())
    except Exception as e:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tail.py <filename>")
    else:
        tail(sys.argv[1])
