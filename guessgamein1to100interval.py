import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("You have to guess the number, and I'll tell you if it's higher or lower.")

myInterval = range(1, 101)
computerChoice = random.choice(myInterval)

def guessingGame():
    while True:
        numberGuessed = int(input("Enter your number... "))
        
        if numberGuessed < computerChoice:
            print("Higher...")
        elif numberGuessed > computerChoice:
            print("Lower...")
        else:
            print("You won!")
            break

guessingGame()
