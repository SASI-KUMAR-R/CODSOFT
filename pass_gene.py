#IMPORTING RANDOM FUNCITON FOR RANDOM PASSWORD GENETOR
import random
#IMPORTING STRING FUNCTION TO USE STRING METHOD EFFIENTILY
import string

# MAIN FUNCTION THIS FUNCTION CONTAINS MAIN CODE OF PASSWORD GENERATOR
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#DETERMINING THE LENGTH FOR PASSWORD
try:
    password_length = int(input("ENTER THE DESIRED PASSWORD LENGTH FOR GENERATOR :"))
    
    if password_length <= 0:
        print("PLEASE CHECK YOUR ENTERED NUMBERS, I CAN'T GENERATE.")
    else:
# GENERATING THE PASSWORD :
        password = generate_password(password_length)
        print(f"GENERATED PASSWORD : {password}")
except ValueError:
    print("INVALID LENGTH..")
