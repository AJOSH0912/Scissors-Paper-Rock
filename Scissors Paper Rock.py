import random

def get_computer_choice():
    """Return a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter your choice (rock, paper, or scissors). To exit the game, type 'exit'.")
    
    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "exit":
            print("Thanks for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()