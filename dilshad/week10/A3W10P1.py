import sys


def main():
    if len(sys.argv) != 2:
        print(f"Error reading file: \"{' '.join(sys.argv[1:])}\"")
        sys.exit()

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            for i in range(10):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f'Error reading file: "{file_name}"')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
