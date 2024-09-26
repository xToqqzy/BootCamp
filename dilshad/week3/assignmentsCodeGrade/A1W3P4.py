# Function to display the temperature conversion table
def display_temperature_conversion_table():
    # Print the table headers
    print("°C\t°F")
    
    # Iterate through Celsius values from 0 to 100 in steps of 10
    for celsius in range(0, 101, 10):
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        # Print the values without decimal point
        print(f"{celsius}\t{int(fahrenheit)}")  # Convert fahrenheit to int to remove the decimal

# Call the function to display the table
display_temperature_conversion_table()
