
import random
import array

print("PASSWORD GENERATOR")

max_length = 12

numbers = ["1","2","3","4","5","6","7","8","9"]

lowcase_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

uppercase_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

symbols = ["!","@","#","$","%","*","&"]

combined_characters = numbers + lowcase_alphabets + uppercase_alphabets + symbols

rand_numbers = random.choice(numbers)
rand_lowcase = random.choice(lowcase_alphabets)
rand_uppercase = random.choice(uppercase_alphabets)
rand_symbols = random.choice(symbols)

temp_password = rand_numbers + rand_lowcase + rand_uppercase + rand_symbols

for x in range(max_length - 4):
    temp_password = temp_password + random.choice(combined_characters)

    temp_password_list = array.array("u",temp_password)
    random.shuffle(temp_password_list)

password = " "
for x in temp_password_list:
    password = password + x

print(password)