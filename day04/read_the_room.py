import random

situations = [
    'You\'re in the middle of a job interview...',
    'Remember your aunt? No? Too bad, because it\'s her birthday and it\'s your turn to send a message on the family group chat...',
    'Discord calling! Your friend needs you to plan an attack on the rival players...'
]

responses = {
    (0, 'formal'):   'The interviewer seems to be pleased. Good job!',
    (0, 'informal'): 'What did you just call the interviewer??',
    (0, 'jargon'):   'Congratulations! You\'ve just embarrassed yourself!',
    (1, 'formal'):   'Your aunt replies with three question marks...',
    (1, 'informal'): 'There\'s nothing like a simple message paired with a couple of random emojis :)',
    (1, 'jargon'):   'For some reason, only your little cousins react so... well done?',
    (2, 'formal'):   'Your friend stares at the screen. "Comrade... are you okay?"',
    (2, 'informal'): 'Close enough, but your friend keeps asking why you type like someone\'s watching.',
    (2, 'jargon'):   'LETS GO!! Your friend hypes you up and the raid begins. No cap.',
}

situation_index = random.randrange(0, len(situations))
user_choice = input(f'{situations[situation_index]}\nWhat register do you choose?: Formal, Informal or Jargon ').lower()

print(responses.get((situation_index, user_choice), 'Invalid choice. Formal, Informal or Jargon only!'))