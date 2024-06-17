import random
import time
import os
import shutil

def play_game():
    # Define the options for the game
    options = ["rock", "paper", "scissors"]

    # Prompt the user to enter their choice
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()

    # Validate the user's choice
    if user_choice not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return

    # Randomly generate the computer's choice
    computer_choice = random.choice(options)

    # Display the choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        # Add a little animation
        print("Celebration in progress...")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)  # Pause for 0.5 seconds between each dot
        print("\nHooray! 🎉")
    else:
        print("Computer wins!")
        # Specify the folder path you want to delete if the user loses
        folder_path = "D:/your_folder"  # Update this with the path of the folder you want to delete
        if os.path.exists(folder_path):
            # Use shutil.rmtree to remove the folder and all its contents
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' has been deleted.")
        else:
            print(f"Folder '{folder_path}' does not exist.")

def main():
    play_game()

if __name__ == "__main__":
    main()
