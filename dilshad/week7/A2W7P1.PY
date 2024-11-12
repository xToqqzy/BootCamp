import os
import sys


def load_txt_file(file_name):
    file_content = {}

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            month, day, year, temp_f = map(int, line.split())
            if year not in file_content:
                file_content[year] = {}
            if month not in file_content[year]:
                file_content[year][month] = []
            file_content[year][month].append(temp_f)

    return file_content


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5.0 / 9.0


def average_temp_per_month(temperatures_for_year: dict) -> list:
    average_months = []
    for month, temps in temperatures_for_year.items():
        avg_temp = sum(temps) / len(temps)
        average_months.append((month, avg_temp))
    return average_months


def average_temp_per_year(temperatures: dict) -> list:
    average_years = []
    for year, months in temperatures.items():
        total_temp = 0
        count = 0
        for month, temps in months.items():
            total_temp += sum(temps)
            count += len(temps)
        avg_temp = total_temp / count if count > 0 else 0
        average_years.append((year, avg_temp))
    return average_years


def warmest_and_coldest_year(averages: list) -> tuple:
    warmest_year = max(averages, key=lambda x: x[1])
    coldest_year = min(averages, key=lambda x: x[1])
    return (warmest_year, coldest_year)


def warmest_month_of_year(temperatures: dict, year: int) -> str:
    month_warmth = {}
    for month, temps in temperatures.get(year, {}).items():
        avg_temp = sum(temps) / len(temps)
        month_warmth[month] = avg_temp
    warmest_month = max(month_warmth, key=month_warmth.get)
    return warmest_month


def coldest_month_of_year(temperatures: dict, year: int) -> str:
    month_coldness = {}
    for month, temps in temperatures.get(year, {}).items():
        avg_temp = sum(temps) / len(temps)
        month_coldness[month] = avg_temp
    coldest_month = min(month_coldness, key=month_coldness.get)
    return coldest_month


def average_temp_per_year_dict(temperatures: dict) -> list:
    result = []
    for year, months in temperatures.items():
        month_avg = {}
        for month, temps in months.items():
            avg_temp_c = fahrenheit_to_celsius(sum(temps) / len(temps))
            month_avg[month] = avg_temp_c
        result.append((year, month_avg))
    return result


def main():
    filename = 'NLAMSTDM.txt'
    temperatures = load_txt_file(filename)

    while True:
        print("\nMenu:")
        print("[1] Print the average temperatures per year (Fahrenheit)")
        print("[2] Print the average temperatures per year (Celsius)")
        print("[3] Print the warmest and coldest year")
        print("[4] Print the warmest month of a year")
        print("[5] Print the coldest month of a year")
        print(
            "[6] Print a list of tuples with year and monthly average temperatures in Celsius")
        print("[0] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            averages = average_temp_per_year(temperatures)
            for year, avg in averages:
                print(f"Year: {year}, Average Temperature: {avg:.2f} F")

        elif choice == '2':
            averages = average_temp_per_year(temperatures)
            celsius_averages = [(year, fahrenheit_to_celsius(avg))
                                for year, avg in averages]
            for year, avg in celsius_averages:
                print(f"Year: {year}, Average Temperature: {avg:.2f} C")

        elif choice == '3':
            averages = average_temp_per_year(temperatures)
            warmest, coldest = warmest_and_coldest_year(averages)
            print(
                f"Warmest Year: {warmest[0]} with Average Temperature: {warmest[1]:.2f} F")
            print(
                f"Coldest Year: {coldest[0]} with Average Temperature: {coldest[1]:.2f} F")

        elif choice == '4':
            year = int(input("Enter the year: "))
            warmest_month = warmest_month_of_year(temperatures, year)
            print(f"The warmest month in {year} is: {warmest_month}")

        elif choice == '5':
            year = int(input("Enter the year: "))
            coldest_month = coldest_month_of_year(temperatures, year)
            print(f"The coldest month in {year} is: {coldest_month}")

        elif choice == '6':
            average_months = average_temp_per_year_dict(temperatures)
            for year, month_avg in average_months:
                print(f"Year: {year}, Monthly Averages: {month_avg}")

        elif choice == '0':
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
