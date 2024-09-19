# Ask the user to enter the sides of the triangle in the format "a=X,b=Y,c=Z"
input_string = input("Enter the sides of the triangle in the format 'a=X,b=Y,c=Z': ")

# Split the input string into a list of words
words = input_string.split(',')

# Extract the numbers from the list and convert them to integers
a = int(words[0].split('=')[1])
b = int(words[1].split('=')[1])
c = int(words[2].split('=')[1])

# Check if the inputs form a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Check if all sides are equal
    if a == b == c:
        print("Equilateral triangle")
    # Check if at least two sides are equal
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    # Check if all sides are different
    else:
        print("Scalene triangle")
else:
    # Print a more descriptive error message
    print("The input numbers do not form a valid trianglscalene")