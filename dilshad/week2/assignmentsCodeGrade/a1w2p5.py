input_string = input("Date: ")

# Check if the input is in the correct format
if "Month:" in input_string and "Day:" in input_string:
    words = input_string.split(',')
    month = int(words[0].split(':')[1].strip())
    day = int(words[1].split(':')[1].strip())

    if month == 1 and day == 1:
        print("Nieuwjaarsdag")
    elif month == 4 and day == 27:
        print("Koningsdag")
    elif month == 4 and day == 30:
        print("Koninginnedag")
    elif month == 5 and day == 4:
        print("Dodenherdenking")
    elif month == 5 and day == 5:
        print("Bevrijdingsdag")
    elif month == 12 and day == 25:
        print("Eerste Kerstdag")
    elif month == 12 and day == 26:
        print("Tweede Kerstdag")
    elif month == 12 and day == 5: 
        print("Sinterklaas")
    else:
        print("No holiday found on given input")
else:
    print("Invalid input format. Please enter the date in the format 'Month: X, Day: Y'")