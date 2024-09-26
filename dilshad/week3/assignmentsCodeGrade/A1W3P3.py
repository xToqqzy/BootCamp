# Function to draw modular rectangle using for loops
def draw_modular_rectangle_for(width, height):
    for row in range(height):
        for col in range(width):
            print((row * width + col) % 10, end=' ')
        print()  # Move to the next line after finishing a row

# Get user input
user_width = int(input("Width: "))
user_height = int(input("Height: "))
draw_modular_rectangle_for(user_width, user_height)
