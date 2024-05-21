import random
import time

class RockPaperScissors:
    def __init__(self):
        self.count1 = 0
        self.count2 = 0

    def get_user_input(self):
        while True:
            try:
                s = int(input("Enter the number of game scores: "))
                break
            except ValueError:
                print("The value is not correct!")

        return s

    def play_game(self):
        while True:
            try:
                b = int(input("Choose one of (Rock = 1), (Paper = 2), (Scissors = 3): "))
                if b < 1 or b > 3:
                    print("The value is not correct!")
                    continue
            except ValueError:
                print("The value is not correct!")
                continue

            a = random.randint(1, 3)
            print("********************************************************************")
            # Show user's move
            moves = ["Rock", "Paper", "Scissors"]
            print(f"Your choice is: {moves[b - 1]}")
            print(f"Opponent's choice is: {moves[a - 1]}")

            # Calculate game result
            time.sleep(1)
            if b == 1 and a == 2 :
                self.count2 +=1
            elif b == 1 and a == 3 :
                self.count1 +=1
            #if you choose Paper
            elif b == 2 and a == 1 :
                self.count1 +=1
            elif b == 2 and a==3 :
                self.count2 +=1
            #if you choose Scissors
            elif b == 3 and a==1 :
                self.count2 +=1
            elif b == 3 and a==2 :
                self.count1 +=1
            #If both choose the same thing
            elif a == b :
                print("nothing")

            print("********************************************************************")
            print(f"Your score: {self.count1}    and    Opponent's score: {self.count2}")
            print("-------------------------------------------------------------")
            print()

            if self.count1 >= s:
                print("You win! :)")
                break
            elif self.count2 >= s:
                print("You lost! :(")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    s = game.get_user_input()
    game.play_game()
    print("parham code")
    time.sleep(10)
    exit()
