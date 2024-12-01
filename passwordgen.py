import string
import random

password = ''
password += string.ascii_letters
password += string.digits
password += string.punctuation

# print(password)

chair = list(password)

digits = int(input("How many characters do you want in a password? "))

print("Your wanted password is:",end=" ")

for i in range (digits):
    randomizer = random.choice(chair)
    print(randomizer, end="")