import gspread
from google.oauth2.service_account import Credentials
import random
import Styles

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')

words = SHEET.worksheet('words')
data = words.get_all_values()
# get a random word from the data list each time
hidden_word = random.choice(data)
print(f"Hidden Word is {hidden_word}")  # to be removed before submitting
styles = Styles()


def game_instruction():
    """
    Function to explain the game rules to the user
    """
    print(f"""{styles.BOLD} WELCOME TO WORDLE \n
    ==================================================\n
    Wordle is a single player game.\n
    The player has to guess a five letter English word.\n
    You have six attempts.\n
    Your Progress Guide: \n
    Green indicates that the letter and its position is correct.\n
    Yellow indicates that the letter is there, but in a different position.\n
    Red indicates that the letter not there in the word. {styles.RESET}\n """)


def validate_data_length(guess):
    """
    Function to check whether the user input consists of 5 letters.
    """
    try:
        if len(guess) != 5:
            raise ValueError(
                f"Exactly 5 letters required, you provided {len(guess)}"
            )
            # break
        else:
            print("Inside Else Block")
            # break
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    return


def validate_data_content(guess):
    """
    Function to check whether the user input contains alphabets only
    """
    try:
        if not (guess.isalpha()):
            raise ValueError(
                f"The word should contain English alphabets only"
            )
            # break
        else:
            print("Inside Else Block")
            # break
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    return


def validate_data_value(guess):
    """
    Function to check whether the user input contains ascii characters only
    """
    try:
        for char in guess:
            converted = ord(char)
            # check whether the ascii values are between 65 and 90 (A to Z)
            if converted not in range(65, 91):
                raise ValueError(
                    f"The word should contain English alphabets only")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    return


def check_word():
    """
    Function to check the word entered by user with the actual word
    """
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word. Please enter a 5 letter word: \n"))
        validate_data_length(guess)
        validate_data_content(guess)
        guess = guess.upper()
        validate_data_value(guess)
        if guess == hidden_word:
            print(f"{styles.BOLD}Congratulations, YOU WIN !!!{styles.RESET}\n")
            break
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempt(s) left \n")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(f"{styles.GREEN} {word} {styles.RESET}, end=" "")
                elif word in hidden_word:
                    print(f"{styles.YELLOW} {word} {styles.RESET}, end=" "")
                else:
                    print(f"{styles.RED} {word} {styles.RESET}, end=" "")
            if attempt == 0:
                print(f"{styles.BOLD} GAME OVER !!! {styles.RESET}\n")


def main():
    """
    Run all program functions
    """
    game_instruction()
    check_word()


main()
