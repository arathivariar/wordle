def game_instruction():
    """
    Function to explain the game rules to the user
    """
    print("""Wordle is a single player game\n
    A player has to guess a five letter hidden word\n
    You have six attempts.\n
    Your Progress Guide "✔❌❌✔➕"\n
    "✔" Indicates that the letter at that position was guessed correctly\n
    "➕" indicates that the letter at that position is in the hidden word, but in a different position\n
    "❌" indicates that the letter at that position is wrong, and isn't in the hidden word\n   """)

def check_word():
    """
    Function to check the word entered by user with the actual word
    """
    hidden_word = "snail"
    attempt = 6
    while attempt > 0:
     guess = str(input("Guess the word: \n"))
     if guess == hidden_word:
          print("You guessed the words correctly! YOU WIN\n")
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
             print(" Game over !!!! \n")


game_instruction()
check_word()
