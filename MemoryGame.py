import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        print(f"Please enter {self.difficulty} numbers separated by spaces:")
        while True:
            try:
                user_input = input()
                user_list = list(map(int, user_input.split()))
                if len(user_list) == self.difficulty:
                    return user_list
                else:
                    print(f"Please enter exactly {self.difficulty} numbers.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        sequence = self.generate_sequence()
        print("Remember this sequence:")
        print(sequence)
        time.sleep(0.7)
        print("\033c", end="")  # Clear the screen

        user_sequence = self.get_list_from_user()
        if self.is_list_equal(sequence, user_sequence):
            print("Congratulations! You remembered the sequence correctly.")
            return True
        else:
            print(f"Sorry, the correct sequence was {sequence}.")
            return False

# Example usage:
if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level: "))
    game = MemoryGame(difficulty)
    game.play()
