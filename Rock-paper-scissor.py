import random

def rps_game():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)
    
    if user_choice not in choices:
        return "Invalid choice!"
    
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

print(rps_game())
