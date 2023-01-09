import random

user_score = 0
computer_score = 0
user_computer_draws = 0
options = ["rock", "paper", "scissors"]


print("We're going to play a classic game.")
print()
print()

while True:
    user_input = input("Please type one of the following: Rock, Paper, Scissors or Q to quit: ").lower()
    if user_input == "q":
        print()
        break

    if user_input not in options:
        print()
        print("Please enter valid response")
        print()
        continue

    random_number = random.randint(0, 2)
    #0 is rock, 1 is paper, 2 is scissors

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

#user win conditions
    if user_input == "rock" and computer_pick == "scissors":
        user_score += 1
        print("You won! XD")
        print()


    elif user_input == "paper" and computer_pick == "rock":
        user_score += 1
        print("You won! :D")
        print()


    elif user_input == "scissors" and computer_pick == "paper":
        user_score += 1
        print("You won! :)")
        print()

    elif user_input == computer_pick:
        user_computer_draws +=1
        print("Its a draw, no points given.")
        print()

    else:
        computer_score += 1
        print("You lost! :(")
        print()

print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
print("You drew", user_computer_draws, "times.")
print()
print("Please play again! ^_^")