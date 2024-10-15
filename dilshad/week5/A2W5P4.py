def is_integer(unchecked: str) -> bool:
    if user_input.isnumeric():
        print("Valid")
        True
    else:
        print("invalid")
        False


def remove_non_integer(unchecked: str) -> str:
    answer_non_int = ""

    for charachters in unchecked:
        if charachters.isdigit():
            answer_non_int += charachters

    return answer_non_int


if __name__ == '__main__':
    user_input = input("Check if number")
    answer = is_integer(user_input)
    print(answer)

    user_input = input("Remove all letters")
    answer = remove_non_integer(user_input)
    print(answer)


# for of while if statement is alpha of isnum
# legen string door alle tekens heen if num voeg toe
# en niet num niet voegen
