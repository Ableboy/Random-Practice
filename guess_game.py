from random import randint

answer = randint(1, 10)
def guesses_game(answer, user):
    while True:
        print(answer)
        try:
            user = int(input("Enter number between 1 to 10: "))
            if 0 < user < 11:
                if user == answer:
                    print("You're a special being, keep it up")
                    break
                else:
                    print("Wrong try again dude")
        except ValueError:
            print("Ahh!. Enter a number nut head")

# Another way of guessing game

# Guessing game using random() as correct guess
import random
import sys

# correct_ran = random.randint(1, 10) # To access the correct_ran in loop
while True:
    try:
        # print(correct_ran)
        # get user input for the guess game
        num_given = int(input("guess a num between 1 to 10: "))
        # result for the guess game using sys to print
        correct_ran = random.randint(int(sys.argv[1]), int(sys.argv[10]))
        # check num if it's less than 10 but more than 0
        if 0 < num_given < 11:
            # check random for corresponding
            if num_given == correct_ran:
                print("you're a genius dude!")
                break
            else:
                print("Try again dude")
        else:
            print("hey bozo, i said 1 ~ 10")
    # check if user input number, if not tell to input
    except ValueError:
        print("please enter a number")