import string
from word_analyzer import has_accent

vowels_with_accents = ["á", "é", "í", "ó", "ú"]

def remove_punctuation(phrase):
    for char in phrase:
        if char in string.punctuation:
            phrase = phrase.replace(char, '')
    return phrase

user_phrase = input("Introduce una frase: ")
phrase_without_punctuation = remove_punctuation(user_phrase)
char_count = len(user_phrase.replace(" ", ""))
tokens = phrase_without_punctuation.split()


print(
    f'Frase introducida: {user_phrase}\n'
    f'Número de caracteres (con espacios): {len(user_phrase)}\n'
    f'Número de caracteres (sin espacios): {len(char_count)}\n'
    f'¿Contiene tilde?: {has_accent(user_phrase)}\n'
    f'Primera palabra: {tokens[0]}\n'
    f'Última palabra: {tokens[-1]}')

