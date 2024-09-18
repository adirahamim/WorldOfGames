import os
import platform

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner() -> None:
    """
    Clears the terminal screen based on the operating system.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Example usage
if __name__ == "__main__":
    screen_cleaner()
