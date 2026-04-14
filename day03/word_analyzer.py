vowels_with_accents = ["á", "é", "í", "ó", "ú"]

    
def has_accent(word):
    counter = 0
    for letter in word:
        if letter in vowels_with_accents:
            counter += 1
    if counter >= 1:
        return "Sí"
    else:
        return "No"


user_word = input("Introduce una palabra: ")


print(
    f'Palabra introducida: {user_word}\n'
    f'Número de letras: {len(user_word)}\n'
    f'En mayúsculas: {user_word.upper()}\n'
    f'¿Contiene tilde?: {has_accent(user_word)}\n'
    f'Primera letra: {user_word[0]}\n'
    f'Última letra: {user_word[-1]}')

