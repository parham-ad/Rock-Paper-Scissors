import random
import time

count1 = 0
count2 = 0
s = int(input("Enter the number of game scores: "))

while True :
    b =int(input("choose one of (Rock = 1) , (Paper = 2) , (Scissors = 3): "))
    a =random.randint(1,3)
    print(a)

    #Show your move
    if b == 1:
        print("your choose is: Rock")
    elif b == 2:
        print("your choose is: Paper")
    elif b == 3:
        print("your choose is: Scissors")
    #Show opponent's move
    if a == 1 :
        print("opponent's choose is: Rock")
    elif a == 2 :
        print("opponent's choose is: Paper")
    elif a == 3 :
        print("opponent's choose is: Scissors")
    
    #Rules of the game

    #if you choose Rock:
    if b == 1 and a == 2 :
        count2 +=1
    elif b == 1 and a == 3 :
        count1 +=1
    #if you choose Paper
    elif b == 2 and a == 1 :
        count1 +=1
    elif b == 2 and a==3 :
        count2 +=1
    #if you choose Scissors
    elif b == 3 and a==1 :
        count2 +=1
    elif b == 3 and a==2 :
        count1 +=1
    #If both choose the same thing
    elif a == b :
        print("nothing")

    print(f"Your score: {count1}              Opponent's score: {count2}")
    print("-------------------------------------------------------------")

    if count1 >= s :
        print("you win!")
        break
    elif count2 >= s :
        print("You lost")
        break

time.sleep(10)
exit()
