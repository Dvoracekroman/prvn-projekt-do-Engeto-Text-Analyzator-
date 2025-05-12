"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Roman Dvořáček
email: dvoracekroman@gmail.com
"""
TEXTS = [
   '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
     a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# uzivatele  bob, ann, mike, liz - jmena uzivatelu 
# heslo 123, pass123, password123, pass123 - hesla uzivatelu

# hesla jsou uložena jako slovník, kde klíčem je uživatelské jméno s hodnotou hesla
uzivatele = {
    "bob" : "123", 
    "ann" : "pass123", 
    "mike" : "password123", 
    "liz" : "pass123"
    }
# oddelovaci znak - pro prehlednost
carka = "-" * 40

# kontrola jmena
while True:
    username = input("Enter your username: ")
    if not username:
        print(f"Empty input. Try again...")
    else:
        break
# kontrola hesla
while True:
    password = input("Enter your password: ")
    if not password:
        # heslo nesmí být prázdné
        # pokud je heslo prázdné, tak se program ukončí
        # a uživatel je vyzván k zadání hesla znovu
        print(f"Empty input. Try again...")
    else:
        break
    # carka "-" * 40
print(carka)

# kontrola uživatelského jména a hesla
# pokud je uživatelské jméno a heslo správné, tak se program spustí

if password == str(uzivatele.get(username)):
    print(f"Welcome to the app, {username.title()}")
    # v případě, že uživatel zadá špatné heslo, tak se program ukončí
else:
    print(f"unregistered user, {username.title()}. terminating the program..")
    exit()
    # pokud je uživatelské jméno a heslo správné, tak se program spustí
print(f"We have {len(TEXTS)} text to be analyzed.")
# craka = "-" * 40
print(carka)

# vypsání textů k analýze
choosen_text = 0
while True:
    choice = input("Enter a number btw. 1 and 3 to select: ")
    if not choice:
        print(f"Empty input. Try again...")
    else:
        break
if choice.isnumeric():
    choice = int(choice)
    # pokud uživatel zadá číslo mimo 1 ay 3, tak se program ukončí
    # a uživatel je vyzván k zadání čísla znovu

    # pokud uživatel zadá hodnotu mezi 1 a 3, tak se program spustí
    if choice < 1 or choice > 3:
        print(f"{choice} is not btw numbers 1-3 Ending app...")
        exit()
    else:
        choosen_text = TEXTS[choice - 1]
elif '-' in choice:
    choice = choice.replace('-','')
    if choice.isnumeric():
        choice = int(choice)
        choice *= -1
        # pokud uživatel zadá záporné číslo, tak se program ukončí
        print(f"{choice} is a negative number. Ending app...")
        exit()
else:
    # pokud uživatel zadá něco jiného než číslo, tak se program ukončí
    print(f"{choice} is not a number. Ending app...")
    exit()
    
# pokud uživatel zada hodnotu mezi 1 a 3, tak se program spustí 
splited_text = choosen_text.split()

# rozdělení textu na jednotlivá slova
splited_text_clear = [word.strip(',.?!') for word in splited_text]

# odstranění interpunkce z jednotlivých slov
numbers_of_length = [len(word) for word in splited_text_clear]

# vytvoření seznamu s počtem znaků jednotlivých slov
title_case = [word for word in splited_text_clear if word.istitle() and word.isalpha()]

# počet slov začínajících velkým písmenem
upper_case = [word for word in splited_text_clear if word.isupper() and word.isalpha()]

# počet slov psaných velkými písmeny
lower_case = [word for word in splited_text_clear if word.islower() and word.isalpha()]

# počet slov psaných malými písmeny
numeric = [word for word in splited_text_clear if word.isnumeric()]

# počet čísel (ne cifer)
numeric_int = [int(number) for number in numeric]

# carka = "-" * 40
print(carka)

# výpis počtu slov 
print(f"There are {len(splited_text)} words in the selected text.")

# počet slov začínajících velkým písmenem
print(f"There are {len(title_case)} titlecase words.")

# počet počet  slov psaných velkými písmeny
print(f"There are {len(upper_case)} uppercase words.")

# počet slov psaných malými písmeny
print(f"There are {len(lower_case)} lowercase words.")

# počet čísel (ne cifer)
print(f"There are {len(numeric)} numeric strings.")

# součet všech  čísel (ne cifer)
print(f"The sum of all the numbers {sum(numeric_int)}.")

# carka = "-" * 40
print(carka)

print(f"LEN | OCCURENCES | NR.")
# carka = "-" * 40
print(carka)

# hvezda = '*'
# mezera = ' '
hvezda = '*'
mezera = ' '
# vytvoření seznamu s počtem znaků jednotlivých slov
set_of_numbers = set(numbers_of_length)

frequency_numbers = []
# vytvoření seznamu s četností jednotlivých čísel
for cislo in set_of_numbers:

    frequency_numbers.append(numbers_of_length.count(cislo))

highest_number = max(frequency_numbers)

for num in set_of_numbers:
    count_of_spaces = highest_number - numbers_of_length.count(num)
    print(f"  {num} | {hvezda * numbers_of_length.count(num)} {mezera * count_of_spaces} | {numbers_of_length.count(num)}")
