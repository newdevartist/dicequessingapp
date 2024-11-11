import random

def dice_guessing_game():
    print("Welcome to the Dice Guessing Game!")
    print("You will guess the outcome of a dice roll (1-6).")
    
    # Generate a random number between 1 and 6
    dice_roll = random.randint(1, 6)
    
    # Get the player's guess
    try:
        guess = int(input("Enter your guess (1-6): "))
        
        # Check if the guess is valid
        if guess < 1 or guess > 6:
            print("Invalid input! Please enter a number between 1 and 6.")
            return
        
        # Display the result
        print(f"The dice rolled: {dice_roll}")
        
        if guess == dice_roll:
            print("Congratulations! You guessed correctly!")
        else:
            print("Sorry, you guessed wrong. Better luck next time!")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    while True:
        dice_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break