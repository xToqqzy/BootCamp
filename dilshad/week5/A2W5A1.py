# funtions aanmaken voor de datasets dus student number etc if and else
# tupils maken waar je de student informatie opslaat
# een loop maken misschien om alle tupils in beeld te krijgen zodat er wanneer er nieuwe worden aaan gemaakt
# die ook in het beeld komen
#
import os
import sys


def student_check(student_number):
    if student_number.isdigit() and len(student_number) == 7 and student_number[0] == '0' and student_number[1] in ('9', '8'):
        return True
    else:
        return False


def name_check(first_name, last_name):
    if first_name.isalpha() and last_name.isalpha():
        return True
    else:
        return False


def date_of_birth_check(date_of_birth):
    days = range(1, 32)
    months = range(1, 13)
    years = range(1960, 2005)

    year, month, day = map(int, date_of_birth.split('-'))
    if year in range(1960, 2005) and month in range(1, 13) and day in range(1, 32):
        return True
    else:
        return False


def study_program_check(study_program):
    if study_program in ['INF', 'TINF', 'CMD', 'AI']:
        return True
    return False


def validate_data(dataset):
    valid_students = []
    corrupt_entries = []

    for student in dataset:
        student_number, first_name, last_name, dob, study_program = student

        invalid_data = []

        if student_check(student_number) == False:
            invalid_data.append(student_number)

        if name_check(first_name, last_name) == False:
            if first_name.isalpha() == False:
                invalid_data.append(first_name)
            if last_name.isalpha() == False:
                invalid_data.append(last_name)

        if date_of_birth_check(dob) == False:
            invalid_data.append(dob)

        if study_program_check(study_program) == False:
            invalid_data.append(study_program)

        if invalid_data != []:
            corrupt_entries.append(','.join(student) +
                                   " => INVALID DATA: " + str(invalid_data))
        else:
            valid_students.append(
                (student_number, first_name, last_name, dob, study_program))

    return valid_students, corrupt_entries


if __name__ == "__main__":
    csv_file = 'students.csv'
    dataset = []

    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        next(csv_file)
        for line in csv_file:
            student_data = line.strip().split(",")
            dataset.append(tuple(student_data))

    valid_students, corrupt_entries = validate_data(dataset)

    print("### VALID LINES ###")
    for student in valid_students:
        print(','.join(student))  # Join with a comma for output

    print("\n### CORRUPT LINES ###")
    for entry in corrupt_entries:
        print(entry)  # Print each corrupt entry directly
