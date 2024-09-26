#je vraagt of je more letters wilt ja betekend dat dit allemaal wordt uitgevoerd wat hier onder staat en no is exit program

#template voor job offer 

#in user input vraag je voor de first name last name job title anual salary starting date
#maar in de input moet je er voor zorgen dat het 1 input is en meerderen vragen 
First_name = input("Whats your first name:")
last_name = input("Whats your last name:")
job_title = input("Whats your job title:")
annual_salary = input("What your annual sallary:")
starting_date = input("Starting date: 'yyyy-mm-dd'")


parts_first_name = first_name.split





parts_starting_date = starting_date.split('-')

# Check if the split resulted in exactly 3 parts_starting_date and if each part is numeric
if len(parts_starting_date) == 3 and all(part.isdigit() for part in parts_starting_date):
    year = int(parts_starting_date[0])
    month = int(parts_starting_date[1])
    day = int(parts_starting_date[2])

    # Check if the year, month, and day are within valid ranges
if (1 <= month <= 12) and (1 <= day <= 31) and (2021 >= year) and (2022 <= year):
        # List of days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

else:    
    print("not correct date should be between 2021 and 2022")
    





#je checkt of de voor en achter naam beide minimaal 2 karakters hebben en max 10 en dat ze alleen letters erin hebben en beide starten met een hoofdletter
#kijk of de formaat van de gegeven informatie klopt funcite is_name_valid
#dat doe je met behulp van of het 2 karakters heeft en of het precies op de goeie manier is geschreven zoals met hoofdletters etc


# job title minimaal 10 karakters zonder nummers
# is_title_valid functie om te kijken of het klopt
#dit check je om je karakters te tellen met behulp van len() en dan ook aan te geven dat het geen nummers mag hebben 

# salary moet een float zijn tuseen de 20 duizend en 80 duizend
# met is_salary_valid
#hier ga ik wat maken dat het len() in dit geval tussen de 20,000.00 en 80,000.00 zit zodat de salary valid is 


# datum mag alleen format hebben van yyyy-mm-dd geen negatieve nummers dagen tuseen de 1-31 maand tussen 1-12 en alleen tuseen 2021 en 2022
# is_date_valid
#hier ga je checken of de eerste 4 cijfers zijn de 2e gedeelte letters en de 3e ook en je haalt dan met behulp van split de - weg 


#en de output wordt dan in een f string gegooid met de bijbehorende tekst en de informatie die is meegegeven 



#template rejection heeft de persoon voor rejection gekozen dan komt die naar de anderen template 
#zelfde verhaal je vraagt zijn naam achter naam job title 
#optie als ja met yes reageert op feedback geven dat die feedback kan geven
#no is dus verder 

#output van rejection ook weer fstring met de meegegevn informatie en dan anderen output for rejection

