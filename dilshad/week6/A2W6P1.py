def unique_chars_dict(input_string):
    char_count = {}

    for char in input_string:
        if char not in char_count:
            char_count[char] = 1

    return len(char_count)


def unique_chars_set(input_string):
    unique_chars = set(input_string)
    return len(unique_chars)


if __name__ == "__main__":
    user_input = input("Enter a string: ")

    unique_count_dict = unique_chars_dict(user_input)
    unique_count_set = unique_chars_set(user_input)

    print(f"Unique characters (using dict): {unique_count_dict}")
    print(f"Unique characters (using set): {unique_count_set}")
