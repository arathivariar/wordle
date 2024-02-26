import gspread
from google.oauth2.service_account import Credentials
import random

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
print(f"Hidden Word is {hidden_word}")


def game_instruction():
    """
    Function to explain the game rules to the user
    """
    print("""WELCOME TO WORDLE \n
    ============================\n
    Wordle is a single player game.\n
    The player has to guess a five letter English word.\n
    You have six attempts.\n
    Your Progress Guide "✔  ➕  ❌"\n
    "  ✔  " indicates that the letter and its position is correct.\n
    "  ➕  " indicates that the letter is there, but in a different position.\n
    "  ❌  " indicates that the letter not there in the word.\n """)


def validate_data_length(guess):
    """
    Function to check whether the user input consists of 5 English letters.
    """
    try:
        if len(guess) != 5:
            raise ValueError(
                f"Exactly 5 letters required, you provided {len(guess)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


def encode_data(guess):
    """
    Function to check whether the user input contains ascii characters only
    """
    try:
        guess = guess.encode('ascii')
    except UnicodeError as e:
        print(f'The word {e.object} has a character at position {e.start} that cannot be encoded in {e.encoding} due to {e.reason}')
    return guess


def validate_data_content(guess):
    """
    Function to check whether the user input contains alphabets only
    """
    if guess.isalpha() == False:
        raise ValueError(
            f"Invalid data: The word should contain English alphabets only. Please enter again\n"
        )


def check_word():
    """
    Function to check the word entered by user with the actual word
    """
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word. Please enter a 5 letter English word: \n"))
        validate_data_length(guess)
        encode_data(guess)
        validate_data_content(guess)
        guess = guess.upper()
        if guess == hidden_word:
            print("You guessed the word correctly! YOU WIN !!!\n")
            break
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempt(s) left ,, \n ")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + " ✔ ", end=" ")
                elif word in hidden_word:
                    print(word + " ➕ ", end=" ")
                else:
                    print(" ❌ ", end=" ")
            if attempt == 0:
                print(" GAME OVER !!! \n")


def main():
    """
    Run all program functions
    """
    game_instruction()
    check_word()


main()
