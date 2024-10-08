import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Enter a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("Congratulations! You guessed the correct number.")
            return True
        else:
            print(f"Sorry, the correct number was {self.secret_number}.")
            return False

# Example usage:
if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level: "))
    game = GuessGame(difficulty)
    game.play()
