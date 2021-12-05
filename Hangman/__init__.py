from random import randint
from words import words


def secretWord():
    while True:
        word = words[randint(0, len(words) - 1)]
        if '-' in word or ' ' in word or len(word) < 6:
            continue
        return word.upper()


def guessLetter():
    guess = input('Chose a letter: ').upper()

    global count
    if guess.isalpha() and len(guess) == 1:
        if guess in guess_letters:
            print('You already chose that one')
            return guessLetter()
        guess_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if guess == letter:
                    guess_word[i] = guess
            return print(f'Well done! {" ".join(guess_word)}')
        else:
            count += 1
            return print('No luck!')

    print('Please chose one, only one, LETTER')
    return guessLetter()


def wordAttempt():
    attempt = input('What is the secret word ').upper()
    if attempt == word:
        return print('Congratulations!!! You got it!')
    print('Not correct. You lost')


word = secretWord()
print(word)

guess_word = ['_' for x in range(0, len(word))]
guess_letters = []
count = 0
guessLetter()

while True:
    print('\n * New Round *\n')

    action = input('would u like to try the "WORD" or a "LETTER"? ').lower()

    print(f'You already chose {guess_letters} and you miss {count} times \n'
          f'Here is the secret word: {" ".join(guess_word)}')

    if action == 'word':
        wordAttempt()
        break
    elif '_' not in guess_word:
        print('The secret word was found! congratulations!!')
        break
    guessLetter()

    if count > 5:
        print('The guy is dead. You lost')
        break
