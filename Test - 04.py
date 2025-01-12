import random

Player1 = input("Enter your name for player 1: ")
Player2 = input("Enter your name for player 2: ")

Results = []

print("starting the rolls for", Player1)
Dice1 = 0
Dice2 = 0
Number_of_Rolls = 0

while Dice1+Dice2 != 12:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    Number_of_Rolls = Number_of_Rolls + 1
    print("Roll", Number_of_Rolls, ":", Dice1, Dice2)

Results.append(Number_of_Rolls)

print("starting the rolls for", Player2)
Number_of_Rolls = 0
Dice1 = 0
Dice2 = 0

while Dice1+Dice2 != 12:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    Number_of_Rolls = Number_of_Rolls + 1
    print("Roll", Number_of_Rolls, ":", Dice1, Dice2)

Results.append(Number_of_Rolls)

print("It took", Player1, Results[0], "rolls to double sixes")
print("It took", Player2, Results[1], "rolls to double sixes")

if Results[0] < Results[1]:
    print(Player1, "won with the fewest rolls:", Results[0])
elif Results[1] < Results[0]:
    print(Player2, "won with the fewest rolls:", Results[1])
else:
    print("It's a tie! Both players took the same number of rolls:", Results[0])

