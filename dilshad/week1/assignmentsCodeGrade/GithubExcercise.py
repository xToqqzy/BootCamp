getal = 12
print("Hallo, Wereld!", getal) #comment

x = 66 #int - integer
k = "kevin" #string
u = 5.5 #float

print(x,k,u)


#variabel
email_address = "1098696@hr.nl"

#splitter zodat je de studentnummer kan krijgen
student_number = email_address.split("@")[0]

#print de studentnummer
print(student_number)

alpahabet = "abcdefghijklmnopqrstuvwxyz"

#splitter zodat je de eerste 13 letters van het alpahabet krijgt
first_13 = alpahabet[0:13]
second_13 = alpahabet[13:26]

#zet de alfabet in verkeerde orde
wrong_order_alphabet = second_13 + first_13

#printing the results
print(wrong_order_alphabet)

#2 variabelen
num1= 5
num2= 10

#optellen van de 2 variabelen
print (num1 + num2)

#vermenigvuldigen van de 2 variabelen 
print (num1 * num2)

#substractie van de 2 variabelen
print (num1 - num2)

#delen van de 2 variabelen
print (num1 / num2)

#vul eigen input in de variable en bij print print de variable 
my_str = input("Enter your number")
print(my_str)

# hij geeft aan divided bij zero fout melding 
#num = 0
#num2 = 0
#print (num/num2)

text = "Hallo, Wereld!"
text2 = "Hallo, Roffa!"

helezin = f"Dit is een {text} , dit is twee {text2}"

print(helezin)

#PEMDAS stands for Parenthesis, Exponentiation, Multiplication, Division, Addition, and Subtraction. However, Multiplication and division can have the same precedence but are differentiated by their orders from left to right. Addition and Subtraction also behave in the same way

#to use parenthesis you have to use double parenthesis to give it priority these symbols ((5*4  )) are used to give priority to the operation inside them
result = ((5 * 3) - (12 * 2)) - ((8 - 4) * (3 - 1)) - (7 - 5)
print(result)


#things to do python book 3.1

# Number of seconds in a minute
seconds_per_minute = 60

# Number of minutes in an hour
minutes_per_hour = 60

# Calculate the total number of seconds in an hour
seconds_per_hour = seconds_per_minute * minutes_per_hour

# Print the result
print(seconds_per_hour)


#things to do python book 3.2

seconds_per_hour = 3600
hours_per_day = 24

#things to do python book 3.3

second_per_day = seconds_per_hour * hours_per_day

print(second_per_day)

#things to do python book 3.4

seconds_per_day = second_per_day
print(seconds_per_day)

#things to do python book 3.5

dividing =seconds_per_day / seconds_per_hour
print(dividing)

#things to do python book 3.6

#using // to get the integer division
dividing =seconds_per_day // seconds_per_hour
print(dividing)







