
class TicTacToe():

    def __init__(self):
        self.board = ['-' for x in range(9)]
        self.log = []
        self.player = 'A'
        self.end = False

    def display(self):
        for r in [self.board[x: x + 3] for x in range(0, 9, 3)]:
            for c in r:
                print ' {} '.format(c),
            print

    def move(self, pos):
        if pos < 0 or pos > 8:
            print 'Invalid position'
        if self.board[pos] != '-':
            print 'Position already filled'
        if self.end == True:
            print 'Game finished'

        self.log.append(''.join([self.player, str(pos)]))
        self.board[pos] = 'O' if self.player == 'A' else 'X'
        self.player = 'B' if self.player == 'A' else 'A'

        self.display()
        if self.check() == 'draw':
            print "Draw !!"
            self.end = True
        elif self.check() != 'no win':
            print ' {} Won !!'.format(self.check()[0][0])
            self.end = True

    def check(self):
        for c in self.board:
            if c == '-':
                break
        else:
            return 'draw'

        h = [self.board[x: x + 3] for x in range(0, 9, 3)]
        v = [[self.board[x + y] for x in range(0, 9, 3)] for y in range(3)]
        d = [[self.board[x] for x in range(y, 9 - y, 4 - y)] for y in [0, 2]]

        all_combos = h + v + d
        win = False
        winning_pos = []
        for i, x in enumerate(all_combos):
            if x.count(x[0]) == len(x) and x[0] != '-':
                winning_pos.append(''.join([x[0], str(i)]))
                win = True

        if win == False:
            return 'no win'
        else:
            return winning_pos

# from tictactoe import TicTacToe
t = TicTacToe()
# t.display()
t.move(4)
t.move(5)
t.move(2)
t.move(6)
t.move(3)
t.move(1)
t.move(0)
t.move(8)
t.move(7)
# t.display()
# t.check()
