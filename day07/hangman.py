import random
from hangman_ascii import stages
from hangman_word_list import word_list
from normalize import normalization

# Select a random word from the dictionary and generate the initial display placeholders
chosen_word = random.choice(list(word_list.keys()))
placeholder = "_" * len(chosen_word)

print(placeholder)

lives = 6
is_game_over = False
correct_letters = []  # Stores normalized versions of correctly guessed letters

while not is_game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    # Iterate over the original word and its normalized version in parallel
    # letter: original character (with accent) → used for display
    # normalized_letter: accent-stripped character → used for comparison
    for letter, normalized_letter in zip(chosen_word, normalization(chosen_word)):
        if normalized_letter == normalization(guess):
            # Player guessed this letter correctly (with or without accent)
            display += letter
            correct_letters.append(normalized_letter)
        elif normalized_letter in correct_letters:
            # Letter was already guessed in a previous round
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' no forma parte de la palabra; pierdes una vida.")

        if lives == 0:
            is_game_over = True
            print(f"****************************{lives}/6 LIVES LEFT****************************")
            print(f"***********************LA PALABRA ERA {chosen_word.upper()}. PIERDES**********************")
            print(f"Definición: {word_list[chosen_word]}")
            break

    if "_" not in display:
        is_game_over = True
        print("****************************¡GANASTE!****************************")
        print(f"Definición: {word_list[chosen_word]}")
        break

    print(stages[lives])
        




    


