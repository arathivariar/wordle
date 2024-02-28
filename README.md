
# Wordle    

Wordle is a word puzzle game that challenges its players to guess a five-letter  English word in six attempts. I have created a version of Wordle with a few minor variations using Python.

 ![Wordle](assets/screenshots/wordle.png)   


# Table of Contents:

- [Design](#design)
- [Features](#features)

	- [Existing Features](#existing-features) 

        -    [Language Used](#language-used)

        -    [Game Instructions](#game-instructions)    

        -    [Google Sheets](#google-sheets)    

        -    [Data Validations](#data-validations)  

        -    [Check Word](#check-word)  

   - [Future Features](#future-features)
- [Testing](#testing)   
     -    [Validator Testing](#validator-testing)  
     -    [Bugs](#bugs)

-    [Libraries and Programs Used](#libraries-and-programs-used)
- [Credits for Content and Media](#credits)  
- [Deployment](#deployment)
   



# Design:   

The flowchart for the application is as shown below:  

![Flowchart](assets/screenshots/flowchart.jpg)  



# Features

# Existing Features:
+ Game Instructions    
+ Google Sheets   
+ Data Validations
+ Check Word 
+ Display Messages    


# Language Used:
+ Python

# Game Instructions     

Wordle is a single player game. A player must guess a five letter English word in six attempts.
Your Progress Guide "✔➕❌"  
"✔" Indicates that the letter at that position was guessed correctly. 
"➕" indicates that the letter at that position is in the hidden word, but in a different position. 
"❌" indicates that the letter at that position is wrong and isn't in the hidden word.    
   
![Game Instructions](assets/screenshots/game_instructions.png)  


# Data Validations

Data validations are done with the help of various functions checking the length of the input string, whether it has valid ASCII characters, whether the input string contains English alphabets only etc.    

![Data Validations](assets/screenshots/data_validations.png)  

# Check Word

Check word function compares the user input with the actual word and displays the relevant message to the user so that the game can be played. If the user guesses the word correctly, a message is displayed accordingly. In case the guess was partially correct, it will inform the same to the user. This function has a loop which gives the user six attempts to guess the hidden word.    

![Check Word]( assets/screenshots/check_word.png)    

# Display Messages

Display messages functionality ensures proper message is displayed throughout the game so that the player understands the game progress. The player is prompted to enter a new guess each time a wrong guess is entered. Also, the number of attempts left is displayed. Similarly, even if the word entered is wrong, but one or more letters are correct, that is displayed. A different message is displayed in case the letter and its position in the word is correct. The player can understand the progress and make an informed decision for the next guess. When the player guess the hidden word correctly, a success message is displayed.    
 
![Display Messages]( assets/screenshots/display_messages.png)

# Future Features:  

+ Include validation to check whether the user input is a valid English word. If not, display an error message telling “Not a word”.
+ Include more words in the Google Sheets for better gaming experience.    
+ Improve the UI experience by including more colours and styles to indicate whether the user input is right or wrong.    

# Testing:  

The application is tested thoroughly by entering all sorts of valid and invalid user inputs and ensuring the application can handle it all without breaking the code.
I have tested the website on both Google Chrome (used for the development) and Microsoft Edge to ensure that the website worked on different browsers.

# Validator Testing:  

# Pep8ci:    

![python_validator](assets/screenshots/python_validator.png)    
 

# Bugs:  

During the development phase, there were a few minor bugs which were fixed with the help of various tutorials available on Google.
There are no unfixed bugs existing in this website as per my knowledge.

# Libraries and Programs Used:  

* Code Repository: [GitHub](https://github.com/)
* Development IDE: [Gitpod](https://www.gitpod.io/)
* [Google Cloud]( https://console.cloud.google.com/)
* [Google Sheets API](https://console.cloud.google.com/apis/api/sheets.googleapis.com)
* [Google Drive API]( https://console.cloud.google.com/apis/api/drive.googleapis.com/)
* [Colorama](https://pypi.org/project/colorama/)
* Validating Python: [PEP8]( https://pep8ci.herokuapp.com/)


# Credits for Content and Media:
* Flowchart: Powerpoint
* Basic game structure: [Free Code Camp]( https://www.freecodecamp.org/news/building-a-wordle-game/)
* Words used in Wordle: [Rock Paper Shotgun]( https://www.rockpapershotgun.com/wordle-past-answers)
* Print Colors in Python terminal: [GeeksForGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)
* Love Sandwiches project
* My Mentor Martina for her guidance and the Slack Community for their support.

# Deployment:

This project is deployed using Code Institute's mock terminal for Heroku.

Steps for Deployment:

* Fork or clone the repository
* Set up Google Sheets and Google Drive APIs
* Download the Key json file from Google, upload it to the project. Change the name to creds.json
* Create a new Google Sheet named 'words'
* Add label one worksheet 'words' and add the desired content to the sheet.
* Create new Heroku app
* Set the buildpacks to python and node.js (in the same order mentioned)
* Link the Heroku app to the repository
* Click Deploy    

_Note:_ The live website link: https://wordle-python-ec6f7a74fed2.herokuapp.com/
