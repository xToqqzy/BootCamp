np_date = input("Enter date in the required format 'YYYY-MM-DD': ")

# Split the input date into components
parts = np_date.split('-')

# Check if the split resulted in exactly 3 parts and if each part is numeric
if len(parts) == 3 and all(part.isdigit() for part in parts):
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])

    # Check if the year, month, and day are within valid ranges
    if (1 <= month <= 12) and (1 <= day <= 31):
        # List of days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Increment the day
        day += 1

        # Check if the day exceeds the number of days in the current month
        if day > days_in_month[month - 1]:
            day = 1
            month += 1

            # Check if the month exceeds 12
            if month > 12:
                month = 1
                year += 1

        # Print the next date
        print(f"Next Date: {year:04d}-{month:02d}-{day:02d}")
    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
