# Step 1: Get user input
user_input = input("Enter a string: ")

# Step 2: Normalize the input
normalized_string = ""
for letter in user_input:  # Loop through each character
    if letter.isalnum():  # Check if the character is alphanumeric
        normalized_string += letter.lower()  # Convert to lowercase and add to normalized_string

# Step 3: Reverse the string
reversed_string = ""
for letter in normalized_string:  # Loop through the normalized string
    reversed_string = letter + reversed_string  # Build the reversed string

# Step 4: Compare original and reversed strings
if normalized_string == reversed_string:
    # Step 5: Display the result
    print(f'"{user_input}" is a palindrome')
else:
    print(f'"{user_input}" is not a palindrome')
