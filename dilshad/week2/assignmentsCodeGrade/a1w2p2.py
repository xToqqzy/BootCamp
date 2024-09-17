# Ask the user to enter a year and convert the input to an integer
year = int(input("Enter a year: "))

# Check if the year is a leap year
# A leap year is divisible by 4, but not by 100 unless it's also divisible by 400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    # If the year meets the conditions for a leap year, print that it's a leap year
    print(f"{year} is a leap year")
else:
    # If the year doesn't meet the conditions for a leap year, print that it's not a leap year
    print(f"{year} is not a leap year")

