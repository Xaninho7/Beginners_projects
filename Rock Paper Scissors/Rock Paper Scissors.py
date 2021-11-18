import random

options = ['rock', 'paper', 'scissors']
result = 0


def game():
    user = input('Rcok, Paper or Scissors? ').lower()
    comp = random.choice(options)
    global result

    while user not in options:
        print('Invalid choice. Try again.')
        user = input('Rcok, Paper or Scissors? ').lower()

    print(f'You chose {user} while the computer chose {comp}.')

    if user == comp:
        print('Draw.')
    elif user == 'rock':
        if comp == 'paper':
            print('You lost.')
            result -= 1
        else:
            print('You won')
            result += 1
    elif user == 'paper':
        if comp == 'scissors':
            print('You lost.')
            result -= 1
        else:
            print('You won')
            result += 1
    else:
        if comp == 'rock':
            print('You lost.')
            result -= 1
        else:
            print('You won')
            result += 1

    play_again = input('Would you like to play again? [Y]es or [N]o? ').lower()
    while play_again != 'y' and play_again != 'n':
        play_again = input('You must chose between [Y]es and [N]o! ').lower()

    if play_again == 'y':
        game()
    else:
        if result == 0:
            print('Thank you for playing! It was a draw!')
        elif result < 0:
            print('Thank you for playing! You lost against the computer!')
        else:
            print('Thank you for playing! You beat the computer!')


game()
