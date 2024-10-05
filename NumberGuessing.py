import random

print("Welcome to the game\nThis game is a number guessing game.\nYou got 7 chances to guess the number.\nlet's start the game.\n")

lowerBound = int(input("Enter Starting Point: "))
upperBound = int(input("Enter Ending Point: "))

computer = random.randrange(lowerBound, upperBound)
# print("Computer : ",computer)

chances = 7
gCounter = 0
while chances>gCounter:
    gCounter += 1
    print("Attempt No. ",gCounter)
    currentGuess = int(input("Enter your number: "))

    if computer == currentGuess:
        print("Congratulations! you found it right !! in the ",gCounter," attempt.")
        break
    elif currentGuess > computer:
        print("Oops! the number is greater than expected.")
    elif currentGuess < computer:
        print("Oops! the number is smaller than expected.")
print("Oops! The number is ",computer,". Better luck next time.")