import gspread
from google.oauth2.service_account import Credentials
import random
from styles import Styles

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
data_list = words.get_all_values()
random_word_list = random.choice(data_list)
actual_word = ''.join(random_word_list)
print(f"Actual Word is {actual_word}")  # to be removed before submitting


def game_instruction():
    """
    Function to explain the game rules to the user
    """
    print(f"""{Styles.BOLD} WELCOME TO WORDLE \n
    =================================================={Styles.RESET}\n
    Wordle is a single player game.\n
    The player has to guess a five letter English word.\n
    You have six attempts.\n
    Your Progress Guide: \n
    {Styles.GREEN}
    Green indicates that the letter and its position is correct.
    {Styles.RESET}
    {Styles.BLUE}
    Blue indicates that the letter is there, but in a different position.
    {Styles.RESET}
    {Styles.RED}
    Red indicates that the letter not there in the word.
    {Styles.RESET}""")


def validate_data_length(guess):
    """
    Function to check whether the user input consists of 5 letters.
    """
    len_flag = True
    try:
        if len(guess) != 5:
            len_flag = False
            raise ValueError(
                f"Exactly 5 letters required, you provided {len(guess)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    return len_flag


def validate_data_content(guess):
    """
    Function to check whether the user input contains alphabets only
    """
    content_flag = True
    try:
        if not (guess.isalpha()):
            content_flag = False
            raise ValueError(
                f"The word should contain English alphabets only"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    return content_flag


def check_word():
    """
    Function to check the word entered by user with the actual word
    """
    attempt = 6
    while attempt > 0:
        guess = str(input(f"{Styles.RESET}Guess the 5 letter word: \n"))
        if validate_data_length(guess) is False:
            continue
        if validate_data_content(guess) is False:
            continue
        guess = guess.upper()
        if guess == actual_word:
            print(f"{Styles.RESET}{Styles.BOLD}Congratulations, YOU WIN !!!\n")
            break
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempt(s) left \n")
            for char_actual, char_guess in zip(actual_word, guess):
                if char_guess == char_actual:
                    print(f"{Styles.BOLD}{Styles.GREEN}{char_guess}", end=' ')
                elif char_guess in actual_word:
                    print(f"{Styles.BOLD}{Styles.BLUE}{char_guess}", end=' ')
                else:
                    print(f"{Styles.BOLD}{Styles.RED}{char_guess}", end=' ')
            if attempt == 0:
                print(f"{Styles.BOLD} GAME OVER !!! {Styles.RESET}\n")


def main():
    """
    Run all program functions
    """
    game_instruction()
    check_word()


main()
