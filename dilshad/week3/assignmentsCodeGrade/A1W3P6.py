# Step 1: Read input from the user
binary_str = input("Enter a binary number: ")

# Step 2: Initialize the decimal variable
decimal_value = 0

# Step 3: Process each digit in the binary string
for digit in binary_str:
    # Check if the digit is valid (0 or 1)
    if digit not in '01':
        print("Invalid binary number. Please enter only 0s and 1s.")
        break
    # Convert the character to an integer (0 or 1)
    decimal_value = decimal_value * 2 + int(digit)

# Step 4: Display the result if input is valid
else:
    print(f"The decimal equivalent of binary {binary_str} is {decimal_value}.")
