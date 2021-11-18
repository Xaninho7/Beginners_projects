import random

options = ['rock', 'paper', 'scissors']
player_result = 0
comp_result = 0


while True:
    user = input('Rcok, Paper or Scissors? ').lower()
    comp = random.choice(options)

    while user not in options:
        print('Invalid choice. Try again.')
        user = input('Rcok, Paper or Scissors? ').lower()

    print(f'You chose {user.upper()} while the computer chose {comp.upper()}.')

    if user == comp:
        print('Draw.')
    elif user == 'rock':
        if comp == 'paper':
            print('You lost.')
            comp_result += 1
        else:
            print('You won')
            player_result += 1
    elif user == 'paper':
        if comp == 'scissors':
            print('You lost.')
            comp_result += 1
        else:
            print('You won')
            player_result += 1
    else:
        if comp == 'rock':
            print('You lost.')
            comp_result += 1
        else:
            print('You won')
            player_result += 1

    play_again = input('Would you like to play again? [Y]es or [N]o? ').lower()
    while play_again != 'y' and play_again != 'n':
        play_again = input('You must chose between [Y]es and [N]o! ').lower()

    if play_again == 'y':
        continue
    else:
        if comp_result == player_result:
            print(f'Thank you for playing! {comp_result} - {player_result} It was a draw!')
            break
        elif comp_result - player_result > 0:
            print(f'Thank you for playing! {player_result} - {comp_result} You lost against the computer!')
            break
        else:
            print(f'Thank you for playing! {player_result} - {comp_result} You beat the computer!')
            break

