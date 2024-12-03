import random
import time

your_score = 0
computer_score = 0

print("Let's play the Pig Dice game!")

while True:
    time.sleep(1)
    input("Your turn. Press Enter to roll the die")
    your_turn = random.randint(1,6)
    print("You scored ", your_turn)
    your_score += your_turn
    time.sleep(1)
    print("Your Score: ", your_score)
    print("Computer's Score: ", computer_score)
    if(your_score >= 30):
        print("Congrats! You won.")
        break
    time.sleep(1)
    print("Computer's turn to play!")
    time.sleep(1)
    computer_turn = random.randint(1,6)
    print("Computer scored ", computer_turn)
    computer_score += computer_turn 
    time.sleep(1)
    if(computer_score >= 30):
        print("Oops! Computer won. Better luck next time")
        break
    print("Your Score: ", your_score)
    print("Computer's Score: ", computer_score)
    time.sleep(1)
