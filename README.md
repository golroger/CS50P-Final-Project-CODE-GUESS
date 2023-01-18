# Code-Guessing Game

#### Video Demo:  <https://youtu.be/8w6rbHy60po>

A simple code-guessing game where the user tries to guess a randomly generated four-digit code. The code cannot start with 0 and cannot have any repeating digits. The user can choose from three levels of difficulty, each with a different number of tries: Easy (30 tries), Medium (20 tries), and Hard (10 tries).

## Installation and Setup

To install and set up the game, follow these steps:

1. Clone or download the repository.
2. Install the required dependencies: `pandas` and `tabulate`.
3. Run the game by executing the `main()` function in the `project.py` file.

## How to Play

1. Choose the difficulty level (easy, medium, or hard) by typing it when prompted.
2. Make a guess by entering a four-digit number (e.g. 1234).
3. You will receive feedback on your guess, indicating how many digits you guessed correctly and how many are in the right place. For example, "2 B" means that two of the digits are correct but not in the right place, and " 1 M" means that one digit is correct and in the right place.
4. Continue guessing until you either guess the code correctly or run out of tries.

## Examples

Here are some examples of the game in action:

Code = 1536
Choose the level,
type the chosen level 'easy', 'medium' or 'hard' :easy

user guess :1234

0 B 2 M

user guess :4321

2 B 0 M

user guess :1356

2 B 2 M

user guess :1536

0 B 4 M

you WIN !


## Additional Information

- The game keeps track of the user's guesses and their results in a history table, which is printed after each guess.
- The game provides a brief overview and the rules before starting.
- The game checks the validity of the user's guesses and provides an error message if the guess is invalid.




