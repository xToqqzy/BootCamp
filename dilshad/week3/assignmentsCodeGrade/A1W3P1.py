user_input = input("Write your word: ")

is_palindrome = True  


for i in range(len(user_input) // 2):
    if user_input[i] != user_input[-i-1]:
        is_palindrome = False
        

if is_palindrome:
    print(f"'{user_input}' is a palindrome")
else:
    print(f"'{user_input}' is not a palindrome")
