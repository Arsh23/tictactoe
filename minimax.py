from tictactoe import TicTacToe
from copy import deepcopy
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

    final_pos = None
    if player == 'A':
        final_score = -1000
    if player == 'B':
        final_score = 1000

    for pos, score in scores:
        if player == 'A' and score > final_score:
            final_score = score
            final_pos = pos
        if player == 'B' and score < final_score:
            final_score = score
            final_pos = pos

    return (final_pos, final_score)


game.move(0)
game.move(1)
game.move(5)
game.move(4)
game.move(7)
game.move(6)
game.display()
print minimax(deepcopy(game), 'A')
