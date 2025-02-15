# Hangman Game

## Description

The Hangman Game is a Python-based text game where the user tries to guess a hidden word by suggesting letters, one at a time. If a user guesses a wrong letter, they lose a life. The game continues until the user guesses the word or loses all their lives.

## Features

- The game randomly selects a word from a predefined list.
- The player can guess one letter at a time.
- The player has 6 lives, with a life being lost for each incorrect guess.
- The game shows the current state of the word with correctly guessed letters.
- ASCII art is used to display the Hangman stages and the game logo.

## Technologies Used

- Python 3.x
- Random module for selecting words

## Files

1. **hangman.py** - The main script that runs the game logic.
2. **hangmanwords.py** - Contains the list of words that can be guessed in the game.
3. **hangmanart.py** - Contains the ASCII art for the stages of the game and the logo.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hangman-game.git
    ```
2. Navigate to the project folder:
    ```bash
    cd hangman-game
    ```
3. Run the `hangman.py` file:
    ```bash
    python hangman.py
    ```

## Game Rules

1. A word is randomly chosen from the list.
2. You need to guess the letters in the word.
3. Each incorrect guess costs you one life. You have 6 lives in total.
4. The game ends when you either guess the word correctly or lose all your lives.
5. You can only guess one letter at a time.
6. If you guess a letter you've already guessed, the game will notify you.

