import random
import string


#Description of program
print("Welcome to the password generator!")
print("This program will generate a random password for you, based on your preferences.")
print("It will ask you for the length (in characters) you would like your password to be.")
print("You will be able to choose the length, the number of letters and numbers you want and the remaining will be symbols.")
print("The letters include both lower and capital cases.")
print("And remember, no spaces in passwords.\n")

while True:
    try:
        #Ask the user for how long they would like their password to be in length (in terms of character count)
        pass_length = int(input("How long would you like your password to be? "))
        break
    except Exception as e:
        print("Try entering a number")
        continue
while True:
    try:
        #Ask the user for how many numbers they would like in their password
        nums_length = int(input("How many numbers would you like in your password? "))
        break
    except Exception as e:
        print("Try entering a number")
        continue

while True:
    try:
        #Ask the user how many letters they would like in their password
        letters_length = int(input("How many letters would you like in your password? "))
        break
    except Exception as e:
        print("Try entering a number")
        continue

print("\nNow generating a passwork with...")
print("Total Length of:", str(pass_length))
print("Number of numbers:",str(nums_length))
print("Number of letters:",str(letters_length))
print("Number of symbols:",str(pass_length - nums_length - letters_length))

numbers_list = []
letters_list = []
symbols_list = []

for letter in string.ascii_letters:
    letters_list.append(letter)

for number in string.digits:
    numbers_list.append(number)

for symbol in '~`!@#$%^&*()_-+={[}]|\:;<,>.?':
    symbols_list.append(symbol)

password = ""

for i in range(1, pass_length + 1):
    if nums_length > 0:
        random_num = random.randrange(len(numbers_list))
        password += numbers_list[random_num]
        nums_length -= 1
    elif letters_length > 0:
        random_num = random.randrange(len(letters_list))
        password += letters_list[random_num]
        letters_length -= 1
    else:
        random_num = random.randrange(len(symbols_list))
        password += symbols_list[random_num]
        
randomized_password = "".join(random.sample(password, len(password)))
print("\nYour randomized password is:", randomized_password)