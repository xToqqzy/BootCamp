import random


def arithmetic_operation(arithmetic_type, num1, num2):
    if arithmetic_type == 'summation':
        return num1 + num2
    elif arithmetic_type == 'multiplication':
        return num1 * num2
    elif arithmetic_type == 'subtraction':
        return num1 - num2
    else:
        return None


def interactive_arithmetic():
    user_input = input(
        "Enter your choice (summation, multiplication, subtraction): ")
    correct_answers = 0
    incorrect_answers = 0

    operation_symbol = ''
    if user_input == 'summation':
        operation_symbol = '+'
    elif user_input == 'multiplication':
        operation_symbol = '*'
    elif user_input == 'subtraction':
        operation_symbol = '-'
    else:
        print("Invalid operation. Please restart the program and enter a valid choice.")
        return

    for _ in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        correct_result = arithmetic_operation(user_input, num1, num2)

        user_answer = int(input(f"{num1} {operation_symbol} {num2} = "))

        if user_answer == correct_result:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was {correct_result}.")
            incorrect_answers += 1

    print(
        f"\nSummary: Correct answers = {correct_answers}, Incorrect answers = {incorrect_answers}")


if __name__ == "__main__":
    interactive_arithmetic()
