import sys


def find_longest_words(filename):
    try:
        with open(filename, "r") as file:
            words = file.read().split()

        if not words:
            print("The file is empty.")
            return

        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]

        print(f"Length of longest word(s) is [{max_length}] chars")
        print("These are all the words of that length:")
        print(", ".join(longest_words))

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 longest_words.py <filename>")
    else:
        find_longest_words(sys.argv[1])
