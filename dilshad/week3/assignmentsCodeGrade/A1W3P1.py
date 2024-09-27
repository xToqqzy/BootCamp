while True:
    first_name = input("What's your first name: ")
    last_name = input("What's your last name: ")
    job_title = input("What's your job title: ")
    annual_salary = input("What is your annual salary: ")
    starting_date = input("Starting date: 'yyyy-mm-dd': ")

    # Check if the first name is valid
    is_valid_name = first_name[0].isupper() and first_name.isalpha() and last_name[0].isupper() and last_name.isalpha()
    
    if not is_valid_name:
        print("Both names must start with a capital letter and contain only letters. Please try again.")
        continue  # Go back to the beginning of the loop

    # Check the length of first and last name
    if len(first_name) < 2 or len(first_name) > 10 or len(last_name) < 2 or len(last_name) > 10:
        print("First and last names must be between 2 and 10 characters. Please try again.")
        continue  # Go back to the beginning of the loop

    # Check if the job title is valid
    if len(job_title) < 10 or any(char.isdigit() for char in job_title):
        print("Job title must be at least 10 characters long and cannot contain numbers. Please try again.")
        continue  # Go back to the beginning of the loop

    # Check if the annual salary is valid
    try:
        annual_salary = float(annual_salary)
        if not (20000 <= annual_salary <= 80000):
            print("Annual salary must be between 20,000 and 80,000. Please try again.")
            continue  # Go back to the beginning of the loop
    except ValueError:
        print("Please enter a valid number for annual salary.")
        continue  # Go back to the beginning of the loop

    # Check the starting date format
    parts_starting_date = starting_date.split('-')
    if len(parts_starting_date) != 3 or not all(part.isdigit() for part in parts_starting_date):
        print("Starting date must be in the format 'yyyy-mm-dd' and contain only numbers. Please try again.")
        continue  # Go back to the beginning of the loop

    year = int(parts_starting_date[0])
    month = int(parts_starting_date[1])
    day = int(parts_starting_date[2])

    if not (1 <= month <= 12) or not (1 <= day <= 31) or not (2021 <= year <= 2022):
        print("The date must be valid and within the years 2021 and 2022. Please try again.")
        continue  # Go back to the beginning of the loop

    # If all checks pass, break out of the loop
    print("All inputs are valid!")
    break  # Exit the loop

# Proceed with the rest of your code after the loop
