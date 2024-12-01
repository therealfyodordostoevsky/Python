import random

minValue = 1
maxValue = 6
rollAgain = "yes"

while rollAgain.lower() in ["yes", "y"]:
    print("Rolling the dices...")
    diceValues = [random.randint(minValue, maxValue) for _ in range(10)]
    print(f"The values are: {diceValues}")
    
    rollAgain = input("Press 'y' or 'yes' to roll the dices again: ").strip().lower()

print("Have a good day.")
