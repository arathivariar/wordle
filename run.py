import gspread
from google.oauth2.service_account import Credentials

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
print(data)

def game_instruction():
    """
    Function to explain the game rules to the user
    """
    print("""WELCOME TO WORDLE. \n
    "============================"\n
    Wordle is a single player game.\n
    The player has to guess a five letter English word.\n
    You have six attempts.\n
    Your Progress Guide "✔  ➕  ❌"\n
    "  ✔  " indicates that the letter at that position was guessed correctly.\n
    "  ➕  " indicates that the letter at that position is in the hidden word, but in a different position.\n
    "  ❌  " indicates that the letter at that position is wrong, and is not in the hidden word.\n   """)

def check_word():
    """
    Function to check the word entered by user with the actual word
    """
    hidden_word = "snail"
    attempt = 6
    while attempt > 0:
     guess = str(input("Guess the word. Please enter a 5 letter English word: \n"))
     validate_data(guess)
     if guess == hidden_word:
          print("You guessed the word correctly! YOU WIN !!!\n")
          break
     else:
          attempt = attempt - 1
          print(f"you have {attempt} attempt(s) ,, \n ")
          for char, word in zip(hidden_word, guess):
               if word in hidden_word and word in char:
                    print(word + " ✔ ")

               elif word in hidden_word:
                    print(word + " ➕ ")
               else:
                    print(" ❌ ")
          if attempt == 0:
             print(" GAME OVER !!! \n")

def validate_data(guess):
    """
    Inside the try, check whether the user input consists of 5 English letters.
    Raises ValueError if the input is not valid
    or if there aren't exactly 5 letters.
    """
    try:
        if len(guess) != 5:
            raise ValueError(
                f"Exactly 5 letters required, you provided {len(guess)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


game_instruction()
check_word()
