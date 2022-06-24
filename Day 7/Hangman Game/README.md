
# Make a [Hangman Game](https://en.wikipedia.org/wiki/Hangman_(game)). 

Hangman is a guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses. Originally a Paper-and-pencil game, there are now electronic versions. 
* First you should go [""HERE""](https://hangmanwordgame.com/?fca=1&success=0#/) and Play the game.

## Flow Chart of Hangman Game
* Break a complex problem into FLow chart to get better understanding
    * By Clicking [""HERE""](https://ibb.co/ZLyqmbh) ** You can go to the flow chart of Hangman Game.

## Steps You should follow.
1. Import the logo from hangman_art.py and print it at the start of the game.

2. Randomly choose a word from the word_list (use the 'word_list' from hangman_words.py) and assign it to a variable called chosen_word.

3.  Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if the chosen_word was "apple",display should be ["_", "_", "_", "_","_"] with 5 "_" representing each letter to guess.

4.  Create a variable called 'lives' to keep track of the number of lives left. 

5. Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

6.  Loop through each position in the chosen_word; 
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

7.  Check if the letter the user guessed (guess) is one of the letters in the chosen_word

**Hint** Use a while loop to let the user guess again.

8. If the user has entered a letter they've already guessed, print the letter and let them know.

9.  If the letter is not in the chosen_word, print out the letter and let them know it's not in the word

10. If guess is not a letter in the chosen_word, #Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."



11. Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

12. import "stages" from hangman_art and print the ASCII art that corresponds to the current number of 'lives' the user has remaining.

