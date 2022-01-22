import random
from random import randint


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        print(f'Dice: {die1} and {die2}')
        self.position += die2 + die1

        print(f'{self.name} is on position {self.position}')
        if self.position > 100:

            self.position -= (self.position - 100) * 2

        if self.position in snakes_ladders:
            self.position = snakes_ladders[self.position]
            print(f'{self.name} sent to position {self.position}')

        if die1 == die2 and self.position != 100:
            # print('Press any key to roll again')
            self.move()


game_over = False
snakes_ladders = {2: 38,
                  7: 14,
                  15: 26,
                  21: 42,
                  28: 84,
                  36: 44,
                  49: 11,
                  46: 25,
                  51: 67,
                  62: 19,
                  64: 60,
                  71: 91,
                  74: 54,
                  78: 98,
                  87: 94,
                  92: 88,
                  95: 75,
                  99: 80}


list_players = []

while True:
    num_players = int(input('Chose the number of players, from 1 to 4: '))
    if num_players <= 4:
        break

i = 0
while i < num_players:
    player = Player(input(f'What is the name of Player {i+1} '))
    i += 1
    list_players.append(player)

if num_players == 1:
    player = Player('Computer')
    list_players.append(player)


random.shuffle(list_players)
print(f'{list_players[0].name} is the first to play and {list_players[1].name} is the second')

while not game_over:
    for player in list_players:
        print(input(f'{player.name} turn. Press any key to roll! '))
        player.move()

        if player.position == 100:
            print(f'Player  {player.name} win')
            game_over = True
            break
