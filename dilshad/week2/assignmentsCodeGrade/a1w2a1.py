np_date = input("Enter date in the required format 'YYYY-MM-DD': ")

# Split the input date into components
words = np_date.split("-")

# Check if the split resulted in exactly 3 parts (YYYY, MM, DD)
if len(words) == 3:
    # Check if the year part has 4 digits and is numeric
    if len(words[0]) == 4 and words[0].isnumeric():
        # Check if the month part has 2 digits and is numeric
        if len(words[1]) == 2 and words[1].isnumeric():
            # Check if the day part has 2 digits and is numeric
            if len(words[2]) == 2 and words[2].isnumeric():
                # Get the year, month, and day from the input date
                year = int(words[0])
                month = int(words[1])
                day = int(words[2])

                # Check if the day is the last day of the month
                if day == 28:
                    # Check if it's the last day of February
                    if month == 2:
                        # Change the month to March and reset the day to 1
                        month = 3
                        day = 1
                    else:
                        # Change the day to 1 and increment the month
                        day = 1
                        month += 1
                else:
                    # Increment the day
                    day += 1

                # Check if the month is December
                if month == 12:
                    # Change the month to January and increment the year
                    month = 1
                    year += 1

                # Print the next date
                print(f"Next Date: {year:04d}-{month:02d}-{day:02d}")
            else:  
                print("Bijna (dag is niet correct)")
        else:
            print("Bijna (maand is niet correct)")
    else:
        print("Bijna (jaar is niet correct)")
else:
    print("Bijna (formaat is niet correct)")
