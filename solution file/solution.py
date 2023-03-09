import random

class Game:
    def __init__(self, username):
        self.username = username
        self.user_score = 0
        self.computer_score = 0
        print(f"Hello {self.username}! Welcome to my Dice Rolling Simulator game")

    def roll_dice(self):
        return random.randint(1, 6)

    def get_user_roll(self):
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

    def play_game(self):

        for i in range(5):
            # User's turn
            user_roll = self.get_user_roll()
            if user_roll is None:
                print("Thanks for playing!")
                self.check_winner()
                break
            else: 
                print(f"You rolled a {user_roll}.")
                self.user_score += user_roll

            # Computer's turn
            computer_roll = self.roll_dice()
            print(f"The computer rolled a {computer_roll}.")
            self.computer_score += computer_roll

    def check_winner(self):
        # Determine the winner
        if self.user_score > self.computer_score:
            print(
                f"Hey {self.username}, you win! Your score: {self.user_score}. Computer's score: {self.computer_score}.")
        elif self.user_score < self.computer_score:
            print(
                f"The computer wins! Your score: {self.user_score}. Computer's score: {self.computer_score}.")
        else:
            print(
                f"It's a tie! Your score: {self.user_score}. Computer's score: {self.computer_score}.")


if __name__ == "__main__":
    print("Welcome to dice rolling simultor Game")
    username = input("Please enter your name: ")
    game = Game(username)
    input("Press [Enter] key to continue")
    game.play_game()
