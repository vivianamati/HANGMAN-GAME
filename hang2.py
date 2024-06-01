import random

print("WELCOME TO HANGMAN!!!")
print("-----------------------------------")

word_dictionary = ["jacket", "house", "car", "bag", "coat", "cabinet", "bottle", "girl", "boy"]

# Choose a random word
random_word = random.choice(word_dictionary)
guessed_word = "_" * len(random_word)
guessed_letters = []

def print_hangman(wrong):
    hangman_stages = [
        """
        +---+
            |
            |
            |
           ===
        """,
        """
        +---+
        O   |
            |
            |
           ===
        """,
        """
        +---+
        O   |
        |   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
       /    |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
       / \\  |
           ===
        """
    ]
    print(hangman_stages[wrong])

def print_word(guessed_word):
    for char in guessed_word:
        print(char, end=" ")
    print()

def print_lines():
    print("\u203e " * len(random_word))

wrong_attempts = 0

while wrong_attempts < 6 and "_" in guessed_word:
    print("\nLetters guessed so far:", ", ".join(guessed_letters))
    print_hangman(wrong_attempts)
    print_word(guessed_word)
    print_lines()

    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
    else:
        wrong_attempts += 1

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", random_word)
else:
    print("Sorry, you've run out of attempts. The word was:", random_word)
