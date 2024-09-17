position = input("Enter the position of the chess piece: ")
# Check if the position is valid
if len(position) == 2 and position[0].lower() in "abcdefgh" and position[1] in "12345678":
    # If the position is valid, check the color of the square
    if (ord(position[0].lower()) - ord('a') + int(position[1]) - 1) % 2 == 0:
        # If the sum of the ASCII value of the letter and the number is even, the square is black
        print("black|zwart")
    else:
        # If the sum of the ASCII value of the letter and the number is odd, the square is white
        print("white|wit")