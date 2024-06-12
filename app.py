# Write a code about the minigame rock, sicssors, paper
import random

# The user will choose between rock, scissors or paper

print("Welcome to the Rock, Paper, Scissors game!")
print("You will play against the computer. Good luck!")

def game():
    player_score = 0
    computer_score = 0
    
    # The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
    # The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

    while True:
        player_choice = input("Choose between rock, paper, or scissors: ").lower()
        # The computer will choose randomly between rock, scissors or paper
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # The user will play against the computer. Good luck!
        # At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please choose between rock, paper, or scissors.")
            continue
        # The user will be informed if they won, lost or tied with the opponent
        elif player_choice == computer_choice:
            # Display the player's score at the end of the game.
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "paper":
                # Display the player's score at the end of the game.
                print("You lose!")
                computer_score += 1
            else:
                # Display the player's score at the end of the game.
                print("You win!")
                player_score += 1
        elif player_choice == "paper":
            if computer_choice == "scissors":
                # Display the player's score at the end of the game.
                print("You lose!")
                computer_score += 1
            else:
                # Display the player's score at the end of the game.
                print("You win!")
                player_score += 1
        elif player_choice == "scissors":
            if computer_choice == "rock":
                # Display the player's score at the end of the game.
                print("You lose!")
                computer_score += 1
            else:
                # Display the player's score at the end of the game.
                print("You win!")
                player_score += 1
        
        # By the end of each round, the player can choose whether to play again. If the player chooses to play again, the game will restart. 
        # If the player chooses not to play again, the game will end and the player will be able to see the results of the game.
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again != "yes":
            # The user will be able to see the results of the game
            print(f"Player: {player_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

    

game()



    