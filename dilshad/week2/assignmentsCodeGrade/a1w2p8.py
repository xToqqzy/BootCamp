import re

license_input = input("Enter the license plate number: ")

# Define the valid license plate patterns
valid_patterns = [
    r'^([A-Z]{2}-\d{2}-\d{2})$',  # Pattern 1 #the a z is the range of the letters that can be entered the {2} indicates that there should be 2 letters /d (0-9) is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the last /d is the same as the one before it 
    r'^(\d{2}-\d{2}-[A-Z]{2})$',  # Pattern 2 #the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the last /d is the same as the one before it and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters
    r'^(\d{2}-[A-Z]{2}-\d{2})$',  # Pattern 3 #the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters and the last /d is the same as the one before it
    r'^([A-Z]{2}-\d{2}-[A-Z]{2})$',  # Pattern 4 #the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters and the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters
    r'^([A-Z]{2}-[A-Z]{2}-\d{2})$',  # Pattern 5 #the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters and the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers
    r'^(\d{2}-[A-Z]{2}-[A-Z]{2})$',  # Pattern 6 #the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters
    r'^(\d{2}-[A-Z]{3}-\d)$',  # Pattern 7 #the \d is the range of the numbers that can be entered the 0/9 {2} indicates that there should be 2 numbers and the [A-Z] is the range of the letters that can be entered the {3} indicates that there should be 3 letters and the \d is the range of the numbers that can be entered
    r'^(\d-[A-Z]{3}-\d{2})$',  # Pattern 8 #the \d is the range of the numbers that can be entered and the [A-Z] is the range of the letters that can be entered the {3} indicates that there should be 3 letters and the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers
    r'^([A-Z]{3}-\d{2}-[A-Z])$',  # Pattern 9 #the [A-Z] is the range of the letters that can be entered the {3} indicates that there should be 3 letters and the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the [A-Z] is the range of the letters that can be entered
    r'^(\d-[A-Z]{3}-\d{2})$',  # Pattern 10 #the \d is the range of the numbers that can be entered and the [A-Z] is the range of the letters that can be entered the {3} indicates that there should be 3 letters and the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers
    r'^([A-Z]{3}-\d{2}-[A-Z])$',  # Pattern 11 #the [A-Z] is the range of the letters that can be entered the {3} indicates that there should be 3 letters and the \d is the range of the numbers that can be entered the {2} indicates that there should be 2 numbers and the [A-Z] is the range of the letters that can be entered
    r'^(^[A-Z]-\d{3}-[A-Z]{2})$',  # Pattern 12 #the [A-Z] is the range of the letters that can be entered the {3} indicates that there should be 3 letters and the \d is the range of the numbers that can be entered the {3} indicates that there should be 3 numbers and the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters
    r'^([A-Z]{2}-\d{3}-[A-Z])$'  # Pattern 13 #the [A-Z] is the range of the letters that can be entered the {2} indicates that there should be 2 letters and the \d is the range of the numbers that can be entered the {3} indicates that there should be 3 numbers and the [A-Z] is the range of the letters that can be entered
     
]

# Check if the input matches any of the valid patterns for loop is used to check if the input matches any of the valid patterns
for pattern in valid_patterns:
    if re.match(pattern, license_input):
        print("Valid")
        break
else:
    print("Invalid")
