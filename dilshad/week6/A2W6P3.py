def valid_password(user_input):
    allowed_symbols = {"*", "@", "!", "?"}
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    uppercase = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
    lowercase = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    if len(user_input) < 8 or len(user_input) > 20:
        return False

    user_set = set(user_input)

    has_digit = not user_set.intersection(digits).isdisjoint(digits)
    has_upper = not user_set.intersection(uppercase).isdisjoint(uppercase)
    has_lower = not user_set.intersection(lowercase).isdisjoint(lowercase)

    invalid_chars = user_set.copy()
    invalid_chars.difference_update(allowed_symbols)
    invalid_chars.difference_update(digits)
    invalid_chars.difference_update(uppercase)
    invalid_chars.difference_update(lowercase)

    if has_digit and has_upper and has_lower and invalid_chars == set():
        return True
    return False


if __name__ == "__main__":
    attempts = 0

    while attempts < 3:
        password = input("Password: ")
        if valid_password(password):
            print("Password is valid")
            break
        else:
            print("Password is invalid")
            attempts += 1

    if attempts == 3:
        print("You have reached the maximum number of attempts")
