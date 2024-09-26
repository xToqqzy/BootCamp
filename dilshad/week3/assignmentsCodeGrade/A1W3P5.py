# Function to display the multiplication table
def display_multiplication_table():
    # Print the header row
    print("   ", end='')  # Initial space for row labels
    for col in range(1, 11):
        print(f"{col:2} ", end='')  # Print numbers 1 to 10 with formatting
    print()  # Move to the next line

    # Print each row of the multiplication table
    for row in range(1, 11):
        print(f"{row:2} ", end='')  # Print row label
        for col in range(1, 11):
            print(f"{row * col:2} ", end='')  # Print product with formatting
        print()  # Move to the next line after finishing the row

# Call the function to display the multiplication table
display_multiplication_table()
