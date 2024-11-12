import re

license_input = input("Enter the license plate number: ")


# Define the valid license plate patterns
valid_patterns = [
    license_input[0:1].isalpha() and license_input[2:3].isnumeric(
    ) and license_input[4:5].isnumeric(),
    license_input[0:1].isdigit() and license_input[1:2].isdigit() and license_input[2:3] == '-' and license_input[3:4].isdigit(
    ) and license_input[4:5].isdigit() and license_input[5:6] == '-' and license_input[6:7].isalpha() and license_input[7:8].isalpha(),
    license_input[0:1].isdigit() and license_input[1:2].isdigit() and license_input[2:3] == '-' and license_input[3:4].isalpha(
    ) and license_input[4:5].isalpha() and license_input[5:6] == '-' and license_input[6:7].isdigit() and license_input[7:8].isdigit(),
    license_input[0:1].isalpha() and license_input[1:2].isalpha() and license_input[2:3] == '-' and license_input[3:4].isdigit(
    ) and license_input[4:5].isdigit() and license_input[5:6] == '-' and license_input[6:7].isalpha() and license_input[7:8].isalpha(),
    license_input[0:1].isalpha() and license_input[1:2].isalpha() and license_input[2:3] == '-' and license_input[3:4].isalpha(
    ) and license_input[4:5].isalpha() and license_input[5:6] == '-' and license_input[6:7].isdigit() and license_input[7:8].isdigit(),
    license_input[0:1].isdigit() and license_input[1:2].isdigit() and license_input[2:3] == '-' and license_input[3:4].isalpha(
    ) and license_input[4:5].isalpha() and license_input[5:6] == '-' and license_input[6:7].isalpha() and license_input[7:8].isalpha(),
    license_input[0:1].isdigit() and license_input[1:2].isdigit() and license_input[2:3] == '-' and license_input[3:4].isalpha(
    ) and license_input[4:5].isalpha() and license_input[5:6].isalpha() and license_input[6:7] == '-' and license_input[7:8].isdigit(),
    license_input[0:1].isdigit() and license_input[1:2] == '-' and license_input[2:3].isalpha() and license_input[3:4].isalpha(
    ) and license_input[4:5].isalpha() and license_input[5:6] == '-' and license_input[6:7].isdigit() and license_input[7:8].isdigit(),
    license_input[0:1].isalpha() and license_input[1:2].isalpha() and license_input[2:3].isalpha(
    ) and license_input[3:4] == '-' and license_input[4:5].isdigit() and license_input[5:6].isdigit() and license_input[6:7] == '-' and license_input[7:8].isalpha(),
    license_input[0:1].isdigit() and license_input[1:2] == '-' and license_input[2:3].isalpha() and license_input[3:4].isalpha(
    ) and license_input[4:5].isalpha() and license_input[5:6] == '-' and license_input[6:7].isdigit() and license_input[7:8].isdigit(),
    license_input[0:1].isalpha() and license_input[1:2].isalpha() and license_input[2:3].isalpha(
    ) and license_input[3:4] == '-' and license_input[4:5].isdigit() and license_input[5:6].isdigit() and license_input[6:7] == '-' and license_input[7:8].isalpha(),
    license_input[0:1].isalpha() and license_input[1:2] == '-' and license_input[2:3].isdigit() and license_input[3:4].isdigit(
    ) and license_input[4:5].isdigit() and license_input[5:6] == '-' and license_input[6:7].isalpha() and license_input[7:8].isalpha(),
    license_input[0:1].isalpha() and license_input[1:2].isalpha() and license_input[2:3] == '-' and license_input[3:4].isdigit(
    ) and license_input[4:5].isdigit() and license_input[5:6].isdigit() and license_input[6:7] == '-' and license_input[7:8].isalpha()
]


# Check if the input matches any of the valid patterns for loop is used to check if the input matches any of the valid patterns
for pattern in valid_patterns:
    if re.match(pattern, license_input):
        print("Valid")
        break
else:
    print("Invalid")
