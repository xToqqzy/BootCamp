# Ask the user for input in the format 'Years: X'
user_input = input("Please enter the number of years in the format 'Years: X': ")

# Split the input string into a list of words zodat letters en cijfers gescheiden worden
words = user_input.split()

# Extract the number of years from the list
years = int(words[1])

# Calculate the number of months and days
months = years * 12
days = years * 365

# Print the result using f-string
print(f"Months: {months}, Days: {days}")