import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        # Replace 'your_api_key' with your actual API key
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data['rates']['ILS']

    def get_money_interval(self, amount):
        interval = 5 - self.difficulty
        lower_bound = amount * self.exchange_rate - interval
        upper_bound = amount * self.exchange_rate + interval
        return lower_bound, upper_bound

    def get_guess_from_user(self, amount):
        while True:
            try:
                guess = float(input(f"Guess the value of {amount} USD in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        amount = random.randint(1, 100)
        lower_bound, upper_bound = self.get_money_interval(amount)
        guess = self.get_guess_from_user(amount)
        if lower_bound <= guess <= upper_bound:
            print("Congratulations! Your guess is within the correct interval.")
            return True
        else:
            print(f"Sorry, the correct value was between {lower_bound:.2f} and {upper_bound:.2f}.")
            return False



# Example usage:
if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level (1-5): "))
    game = CurrencyRouletteGame(difficulty)
    game.play()