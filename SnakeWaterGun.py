'''
1- snake
-1 - water
0 - gun
'''

import random

computer = random.choice([1,-1,0])
youstr = input("Enter Your Choice(s,w, or g): ")
youDict = {"s": 1,"w": -1, "g": 0} 
foridentify = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print("You Choose: ",foridentify[you])
print("Computer Choose: ",foridentify[computer])


if(computer == you):
    print("Draw!")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")  
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")   
    else:
        print("Something went wrong!")