def is_name_valid(name):
    return 2 <= len(name) <= 10

def is_title_valid(title):
    return 10 <= len(title) <= 50

def is_salary_valid(salary):
    return 20000 <= salary <= 80000

def is_date_valid(starting_date):
    parts_starting_date = starting_date.split('-')
    
    if len(parts_starting_date) == 3 and all(part.isdigit() for part in parts_starting_date):
        year = int(parts_starting_date[0])
        month = int(parts_starting_date[1])
        day = int(parts_starting_date[2])

        if (1 <= month <= 12) and (1 <= day <= 31) and (2021 <= year <= 2022):
            return True  # Date is valid
    return False  # Date is not valid

def generate_offer_letter(first_name, last_name, job_title, salary, start_date):
    formatted_salary = f"{salary:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return (
        f"Dear {first_name} {last_name},\n"
        f"After careful evaluation of your application for the position of {job_title},\n"
        f"we are glad to offer you the job. Your salary will be {formatted_salary} euro annually.\n"
        f"Your start date will be on {start_date}. Please do not hesitate to contact us with any questions.\n"
        f"Sincerely,\nHR Department of XYZ"
    )


def generate_rejection_letter(first_name, last_name, job_title, feedback=None):
    letter = (
        f"Dear {first_name} {last_name},\n"
        f"After careful evaluation of your application for the position of {job_title},\n"
        f"at this moment we have decided to proceed with another candidate.\n"
    )
    if feedback:
        letter += f"Here we would like to provide you our feedback about the interview.\n{feedback}\n"
    letter += (
        "We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.\n"
        "Sincerely,\nHR Department of XYZ"
    )
    return letter

while True:
    more_letters = input("More letters yes or no: ").strip().lower()
    if more_letters != 'yes':
        break

    job_or_rej = input("Job offer or rejection letters: ").strip().lower()
    if job_or_rej not in ['job offer', 'rejection']:
        print("Invalid option. Please enter 'job offer' or 'rejection'.")
        continue

    first_name = input("What's your first name: ").strip()
    if not is_name_valid(first_name):
        print("Input error")
        continue

    last_name = input("What's your last name: ").strip()
    if not is_name_valid(last_name):
        print("Input error")
        continue

    job_title = input("What's your job title: ").strip()
    if not is_title_valid(job_title):
        print("Input error")
        continue

    if job_or_rej == 'job offer':
        salary = input("What is your annual salary: ").strip().replace('.', '').replace(',', '.')
        try:
            salary = float(salary)
        except ValueError:
            print("Input error")
            continue
        if not is_salary_valid(salary):
            print("Input error")
            continue

        start_date = input("Starting date 'yyyy-mm-dd': ").strip()
        if not is_date_valid(start_date):
            print("Input error")
            continue

        # Generate and print the offer letter
        letter = generate_offer_letter(first_name, last_name, job_title, salary, start_date)
        print("\nHere is the final letter to send:\n")
        print(letter)

    else:  # job_or_rej == 'rejection'
        feedback = input("Do you want to provide feedback? (yes or no): ").strip().lower()
        if feedback == 'yes':
            feedback_text = input("Please enter the feedback: ").strip()
            letter = generate_rejection_letter(first_name, last_name, job_title, feedback_text)
        else:
            letter = generate_rejection_letter(first_name, last_name, job_title)

        print("\nHere is the final letter to send:\n")
        print(letter)




