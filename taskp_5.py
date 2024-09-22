import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        computer_choice = random.choice(choices)
        
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
        
        if user_choice == computer_choice:
            print(f"It's a tie! Both chose {user_choice}.")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You win! {user_choice.capitalize()} beats {computer_choice}.")
            user_score += 1
        else:
            print(f"You lose! {computer_choice.capitalize()} beats {user_choice}.")
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Have a great day!")
            break

play_game()
