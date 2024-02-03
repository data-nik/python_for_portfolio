import random

# List of words for the game
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)

# Initialize variables
word_length = len(chosen_word)
display = ["_"] * word_length
lives = 6

# ASCII art representation of hangman stages
stages = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]


# Function to display the current state of the game
def display_game():
  print(stages[lives])
  print(' '.join(display))


# Main game loop
while lives > 0 and "_" in display:
  # Ask the user to guess a letter and convert it to lowercase
  guess = input("Guess a letter: ").lower()

  # Input validation
  if not guess.isalpha() or len(guess) != 1:
    print("Invalid input. Please enter a single letter.")
    continue

  # Check if the guessed letter is in the chosen word
  if guess in chosen_word:
    for position in range(word_length):
      if chosen_word[position] == guess:
        display[position] = guess
  else:
    lives -= 1

  # Display the current state of the game
  display_game()

# Check if the game is won or lost
if "_" not in display:
  print("Congratulations! You win!")
else:
  print(f"Sorry, you lose. The correct word was '{chosen_word}'.")
