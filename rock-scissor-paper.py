import random

user_wins = 0
computer_wins = 0

options = ["rock","scissor","paper"]


while True:
    user_input = input("The rock/scissor/paper or press 'Q' to exit. ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    #rock: 0, scissor:1, paper: 2
    computer_input = options[random_num]

    print("Computer input is",options[random_num] + ".")

    if user_input == "rock" and computer_input == "paper":
        print("You win")
        user_wins += 1

    elif user_input == "paper" and computer_input == "rock":
        print("You win")
        user_wins += 1    

    elif user_input == "scissor" and computer_input == "paper":
        print("You win")
        user_wins += 1

    else:
        print("You lose !")
        computer_wins += 1    

print("You win",user_wins,"times.")
print("Computer win",computer_wins,"times") 
print("Good Bye")      