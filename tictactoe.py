
class TicTacToe():

    def __init__(self):
        self.board = ['-' for x in range(9)]
        self.log = []
        self.player = 'A'

    def display(self):
        for r in [self.board[x: x + 3] for x in range(0, 9, 3)]:
            for c in r:
                print ' {} '.format(c),
            print

    def move(self, pos):
        if pos < 0 or pos > 8:
            raise Exception('Invalid position')
        if self.board[pos] != '-':
            raise Exception('Position already filled')

        self.log.append(''.join([self.player, str(pos)]))
        self.board[pos] = 'O' if self.player == 'A' else 'X'
        self.player = 'B' if self.player == 'A' else 'A'

        self.display()
        print self.log

    def check(self):
        pass
        # from tictactoe import TicTacToe
t = TicTacToe()
# t.display()
t.move(4)
t.move(5)
t.move(2)
t.move(3)
t.move(7)
t.move(1)
t.display()
