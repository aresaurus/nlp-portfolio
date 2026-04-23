alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(functionality, original_text, shift_amount):
    cipher_text = ""

    if functionality == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            letter_index = alphabet.index(letter)
            shifted_index = (letter_index + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_index]

    print(f"Here is the {functionality}d result: {cipher_text}")

stop_caesar = False

while not stop_caesar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, functionality=direction)

    play_again = input("Do you want to try with another message? Type 'yes' or 'no': ").lower()

    if play_again == "no":
        stop_caesar = True