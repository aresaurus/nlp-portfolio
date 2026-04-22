# Day 7 - Linguistic Hangman in Spanish (100 Days of Code)

Base project from Angela Yu's 100 Days of Code course, extended with:

This project is an adaptation of the classic Hangman exercise from the *100 Days of Code* course.

Instead of using a generic word list, this version uses Spanish linguistic terms. Each word is linked to a short definition, so the game works both as a Python practice exercise and as a small vocabulary game related to linguistics and translation.

## Main adaptation

The main linguistic feature of this project is **text normalization**:

- the player can guess accented letters without typing the accent explicitly
- the program compares normalized characters internally
- the original form of the word is preserved for display
- `ñ` is protected so it is not reduced to `n`

For example, a player can type `o` and still reveal `ó` correctly.

## What I practiced

- loops
- conditionals
- lists
- dictionaries
- imports from custom Python modules
- basic text normalization with `unicodedata`

## Why I adapted it

I’m using early Python exercises to connect programming practice with my transition from translation and localization to computational linguistics.