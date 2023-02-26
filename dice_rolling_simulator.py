import random

username = input("Please enter your name: ")
print(f"Hello {username}! Welcome to my Dice Rolling Simulator game")
input("Press [Enter] key to continue")

# Define a function to simulate rolling a dice


def roll_dice():
    return random.randint(1, 6)


# Defining a function to get the user's roll

def get_user_roll():
    while True:
        user_input = input("Press Y to roll the dice, or N to exit: ").lower()
        if user_input == "n":
            return None
        elif user_input == "y":
            while True:
                try:
                    user_roll = int(input("Enter a value between 1 and 6: "))
                    if 1 <= user_roll <= 6:
                        return user_roll
                    else:
                        print("Invalid input. Please enter a value between 1 and 6.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        else:
            print("Invalid input. Please enter Y or N.")


# Defining a function to play the game

def play_game():
    user_score = 0
    computer_score = 0

    for i in range(5):
        # User's turn
        user_roll = get_user_roll()
        if user_roll is None:
            print("Thanks for playing!")
            return
        print(f"You rolled a {user_roll}.")
        user_score += user_roll

        # Computer's turn
        computer_roll = roll_dice()
        print(f"The computer rolled a {computer_roll}.")
        computer_score += computer_roll

    # Determine the winner
    if user_score > computer_score:
        print(
            f"Hey {username}, you win! Your score: {user_score}. Computer's score: {computer_score}.")
    elif user_score < computer_score:
        print(
            f"The computer wins! Your score: {user_score}. Computer's score: {computer_score}.")
    else:
        print(
            f"It's a tie! Your score: {user_score}. Computer's score: {computer_score}.")


play_game()
