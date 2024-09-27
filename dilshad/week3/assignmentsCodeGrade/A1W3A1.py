while True: #<---- van chat gpt whist niet dat dit hier moest 
    more_letters = input("More letters yes or no:")
    if more_letters.lower() != "yes":
        print("Exiting program.")
        break

    job_or_rej = input("job offer or rejection letters: ")
    
    if job_or_rej.lower() == "job offer": #<---- via chat gpt wist niet hoe je kon switchen van(template)
        first_name = input("What's your first name: ")
        last_name = input("What's your last name: ")
        job_title = input("What's your job title: ")
        annual_salary = input("What is your annual salary: ")
        starting_date = input("Starting date: 'yyyy-mm-dd': ")

        is_valid_name = first_name[0].isupper() and first_name.isalpha() and last_name[0].isupper() and last_name.isalpha()
        is_title_valid = job_title

        if not is_valid_name:
            print("Both your first and last name dont have a capital letter in it")

        if len(first_name) <= 2 or len(first_name) >= 10:
            print("First name has to have more then 2 and less then 10 characters")

        if len(last_name) <= 2 or len(last_name) >= 10:
            print("Last name has to have more then 2 and less then 10 characters")

        if len(job_title) < 10 or any(char.isdigit() for char in job_title):
            print("Job title has to have minimum of 10 characters and cant have any numbers in it")

        annual_salary = float(annual_salary)
        if not (20000 <= annual_salary <= 80000):
            print("annual range should be between 20.000 to 80.000")

        parts_starting_date = starting_date.split('-')

        if len(parts_starting_date) == 3 and all(part.isdigit() for part in parts_starting_date):
            year = int(parts_starting_date[0])
            month = int(parts_starting_date[1])
            day = int(parts_starting_date[2])

            if (1 <= month <= 12) and (1 <= day <= 31) and (2021 <= year <= 2022):
                days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:    
                print("not correct date should be between 2021 and 2022")

        print(f"Dear {first_name} {last_name},\n"
              f"After careful evaluation of your application for the position of {job_title},\n"
              f"we are glad to offer you the job. Your salary will be {annual_salary:.3f} euros annually.\n"
              f"Your start date will be on {starting_date}. Please do not hesitate to contact us with any questions.\n"
              f"Sincerely,\n"
              f"HR Department of XYZ")
    
    elif job_or_rej.lower() == "rejection": #<----- zelfde verhaal wist niet dat je op deze manier kon switchen van temaplate dus chatgpt 
        first_name = input("What's your first name: ")
        last_name = input("What's your last name: ")
        job_title = input("What's your job title: ")

        feedback = input("Would you like to provide feedback? (yes or no): ")
        if feedback.lower() == "yes":
            feedback_text = input("Please provide your feedback: ")
            print(f"Thank you for your feedback: {feedback_text}")

        print(f"Dear {first_name} {last_name},\n"
              f"Thank you for your interest in the position of {job_title}. We appreciate the time you took to apply.\n"
              f"Unfortunately, we have decided to move forward with other candidates. We wish you all the best in your job search.\n"
              f"Sincerely,\n"
              f"HR Department of XYZ")
    else:
        print("Invalid option. Please select either 'job offer' or 'rejection letters'.")
