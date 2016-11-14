import random
from copy import deepcopy

from tictactoe import TicTacToe
game = TicTacToe()


def minimax_with_alphabeta(game, player, alpha, beta):
    possible_pos = [x for x in range(9) if game.board[x] == '-']

    score = float('-inf') if player == 'A' else float('inf')
    best_pos = None

    for pos in possible_pos:
        next_game = deepcopy(game)
        next_game.move(pos)
        n = None

        if next_game.status == 'won':
            if next_game.winner == player:
                if player == 'A':
                    n = 20 - len(next_game.log)
                if player == 'B':
                    n = -20 + len(next_game.log)

        elif next_game.status == 'draw':
            n = 0
        else:
            next_player = 'B' if player == 'A' else 'A'
            n = minimax_with_alphabeta(next_game, next_player, alpha, beta)[1]

        if player == 'A':
            if n > score:
                score = n
                best_pos = pos
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        if player == 'B':
            if n < score:
                score = n
                best_pos = pos
            beta = min(beta, score)
            if beta <= alpha:
                break

    best_pos = random.choice(range(9)) if len(possible_pos) == 9 else best_pos
    return (best_pos, score)

if __name__ == '__main__':
    main()


def main():
    while game.status == None:
        game.display()
        print

        if game.player == 'A':
            # pos = int(raw_input('Enter your move : '))
            pos = int(minimax_with_alphabeta(
                deepcopy(game), 'A', float('-inf'), float('inf'))[0])
        else:
            # pos = int(raw_input('Enter your move : '))
            pos = int(minimax_with_alphabeta(
                deepcopy(game), 'B', float('-inf'), float('inf'))[0])

        game.move(pos)
        if game.status == 'draw':
            game.display()
            print 'Draw !!'
        if game.status == 'won':
            game.display()
            print game.winner, 'Won !!'
