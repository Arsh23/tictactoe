import random
from copy import deepcopy

from tictactoe import TicTacToe
game = TicTacToe()


def minimax(game, player):
    scores = []
    possible_pos = [x for x in range(9) if game.board[x] == '-']

    for pos in possible_pos:
        next_game = deepcopy(game)
        next_game.move(pos)

        if next_game.status == 'won':
            if next_game.winner == player:
                if player == 'A':
                    scores.append((pos, 20 - len(next_game.log)))
                if player == 'B':
                    scores.append((pos, -20 + len(next_game.log)))

        elif next_game.status == 'draw':
            scores.append((pos, 0))
        else:
            next_player = 'B' if player == 'A' else 'A'
            scores.append((pos, minimax(next_game, next_player)[1]))

    if player == 'A':
        scores.sort(key=lambda x: x[1], reverse=True)
    if player == 'B':
        scores.sort(key=lambda x: x[1])
    scores = filter(lambda x: x[1] == scores[0][1], scores)
    return random.choice(scores)


while game.status == None:
    game.display()
    print

    if game.player == 'A':
        # pos = int(raw_input('Enter your move : '))
        pos = int(minimax(deepcopy(game), 'A')[0])
    else:
        # pos = int(raw_input('Enter your move : '))
        pos = int(minimax(deepcopy(game), 'B')[0])

    game.move(pos)
    if game.status == 'draw':
        game.display()
        print 'Draw !!'
    if game.status == 'won':
        game.display()
        print game.winner, 'Won !!'
