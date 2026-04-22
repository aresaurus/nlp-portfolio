import random
from hangman_ascii import stages
from hangman_word_list import word_list
from normalize import normalization

# Select a random word and its normalized form
chosen_word = random.choice(list(word_list.keys()))
normalized_word = normalization(chosen_word)

# Initial hidden display
placeholder = "_" * len(chosen_word)
print("Palabra que debes adivinar:", placeholder)

lives = 6
is_game_over = False
correct_letters = []
wrong_letters = []

while not is_game_over:
    if lives == 1:
        print(f"****************************{lives}/6 VIDA RESTANTE****************************")
    else:
        print(f"****************************{lives}/6 VIDAS RESTANTES****************************")

    guess = input("Introduce una letra: ").lower()
    normalized_guess = normalization(guess)

    # Prevent repeated guesses
    if normalized_guess in correct_letters or normalized_guess in wrong_letters:
        print(f"Ya has dicho '{guess}'.")
        continue
    
    # Check whether the guess is in the normalized word
    if normalized_guess in normalized_word:
        correct_letters.append(normalized_guess)
    else:
        wrong_letters.append(normalized_guess)
        lives -= 1
        print(f"'{guess}' no forma parte de la palabra; pierdes una vida.")

    # Build display using original letters, but compare normalized ones
    display = ""

    for letter, normalized_letter in zip(chosen_word, normalized_word):
        if normalized_letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Palabra que debes adivinar:", display)

    if wrong_letters:
        print("Letras incorrectas:", ", ".join(wrong_letters))

    print(stages[lives])

    # Lose condition
    if lives == 0:
        is_game_over = True
        print(f"***********************LA PALABRA ERA {chosen_word.upper()}. PIERDES**********************")
        print(f"Definición: {word_list[chosen_word]}")
        break

    if "_" not in display:
        is_game_over = True
        print("****************************¡GANASTE!****************************")
        print(f"Definición: {word_list[chosen_word]}")
        break




    


