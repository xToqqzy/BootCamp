
# Ask the user to input their age in human years and convert it to an integer
Human_Years = int(input("Enter your age to convert to dog years: "))

# Check if the input is less than 0
if Human_Years < 0:
    # If it is, print an error message
    print("Only positive numbers are allowed")
else:
    # If the input is not less than 0, proceed to calculate the age in dog years
    if Human_Years <= 2:
        # If the human age is less than or equal to 2, each human year is equivalent to 10.5 dog years
        Dog_Years = Human_Years * 10.5
    else:
        # If the human age is more than 2, the first 2 years are calculated as 10.5 dog years each
        # and each additional year is calculated as 4 dog years
        Dog_Years = 2 * 10.5 + (Human_Years - 2) * 4
    # Print the age in dog years
    print(f"Dog years: {Dog_Years}")