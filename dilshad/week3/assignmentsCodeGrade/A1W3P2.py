user_input = input("Write your sentence: ")

is_palindrome = True  

#haal alles dingen eruit
normaal_input = user_input.replace(" ", "")

for i in range(len(normaal_input) // 2):
    if normaal_input[i] != normaal_input[-i-1]:
        is_palindrome = False
        

if is_palindrome:
    print(f"'{normaal_input}' is a palindrome")
else:
    print(f"'{normaal_input}' is not a palindrome")
