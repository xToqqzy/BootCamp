def valid_password(user_input):
    # Directly making the sets for allowed symbols, digits, uppercase, and lowercase letters
    allowed_symbols = {"*", "@", "!", "?"}
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    uppercase = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
    lowercase = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    if len(user_input) < 8 or len(user_input) > 20:
        return False

    has_digit = False
    has_upper = False
    has_lower = False
    has_invalid = False

    for char in user_input:
        if char in digits:
            has_digit = True
        elif char in uppercase:
            has_upper = True
        elif char in lowercase:
            has_lower = True
        elif char not in allowed_symbols:
            has_invalid = True

    if has_digit and has_upper and has_lower and not has_invalid:
        return True
    return False


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
