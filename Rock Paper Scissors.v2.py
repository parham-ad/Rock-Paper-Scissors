import random
import time
count1 = 0
count2 = 0
while True:
    s = input("Enter the number of game scores: ")
    #----------------Error-handling---------------------------------------------
    try:
        s =int(s)
        break
    except ValueError :
        print("the Value is not correct!")
    #---------------------------------------------------------------------------

            
while True :
    #----------------Error-handling---------------------------------------------
    try:
        b =int(input("choose one of (Rock = 1) , (Paper = 2) , (Scissors = 3): "))
        if b < 1 or b > 3:
            print("the Value is not correct!")
            continue
    except ValueError:
        print("the Value is not correct!")
        continue
    #---------------------------------------------------------------------------
    a =random.randint(1,3)
    print("********************************************************************")
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
    
    #Result of the game
    time.sleep(1)
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
    print("********************************************************************")
    print(f"Your score: {count1}    and    Opponent's score: {count2}")
    print("-------------------------------------------------------------")
    print()
    if count1 >= int(s) :
        print("you win! :)")
        break
    elif count2 >= int(s) :
        print("You lost! :(")
        break
print("parham code")
time.sleep(10)
exit()
