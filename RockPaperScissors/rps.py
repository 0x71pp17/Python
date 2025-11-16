import random

def main():
    choices = ["rock", "paper", "scissors"]
    # Define what each choice beats
    wins_over = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    player_score = 0
    computer_score = 0

    print("Let's play rock, paper, or scissors!")
    print("Enter 'quit' to exit the game.")

    while True:
        # Get and validate player input
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice == "quit":
            break
        if player_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Computer makes a choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if wins_over[player_choice] == computer_choice:
            print("You won!")
            player_score += 1
        elif player_choice == computer_choice:
            print("It's a tie!")
        else:
            print("Computer won!")
            computer_score += 1

        # Display current score
        print(f"Score - Player: {player_score}, Computer: {computer_score}\n")

    # Display final results
    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations, you won the game!")
    elif computer_score > player_score:
        print("The computer won the game!")
    else:
        print("The game ended in a tie!")

if __name__ == "__main__":
    main()   
