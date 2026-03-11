
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice working with strings, loops, conditionals, and user input while managing game state across multiple turns.

## 📝 Tasks

### 🛠️ Build Core Hangman Flow

#### Description
Create the main game loop for Hangman. The game should select one word from a predefined word list, let the player guess one letter at a time, and continue until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of words.
- Prompt the user to enter a single-letter guess each turn.
- Reduce remaining attempts only when the guessed letter is not in the word.
- End the game with a clear win or lose message.


### 🛠️ Display Progress and Validate Input

#### Description
Improve the player experience by showing current word progress and handling common input issues. The displayed word should reveal correctly guessed letters and hide unknown letters.

#### Requirements
Completed program should:

- Display the word progress using placeholders such as `_ _ _ _`.
- Show guessed letters so the player can track previous attempts.
- Reject invalid input (empty input, multiple characters, non-letter characters) with a helpful message.
- Ignore repeated guesses without unfairly reducing attempts.
