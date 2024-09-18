SCORES_FILE_NAME = "Scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty: int) -> None:
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + POINTS_OF_WINNING(difficulty)

    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    add_score(3)
