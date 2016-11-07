
class TicTacToe():

    def __init__(self):
        self.board = ['-' for x in range(9)]
        self.log = []
        self.winner = None
        self.player = 'A'
        self.status = None

    def display(self):
        for r in [self.board[x: x + 3] for x in range(0, 9, 3)]:
            for c in r:
                print ' {} '.format(c),
            print

    def move(self, pos):
        # TODO : remove this comdition later
        if pos < 0 or pos > 8 or self.board[pos] != '-' or self.status != None:
            print 'Invalid position -', pos
            return

        self.log.append(''.join([self.player, str(pos)]))
        self.board[pos] = 'O' if self.player == 'A' else 'X'
        self.player = 'B' if self.player == 'A' else 'A'
        result = self.check()

        if result == 'draw':
            print "Draw !!"
            self.status = 'draw'
        elif result != None:
            print ' {} Won !!'.format(result[0][0])
            self.status = 'won'
            self.winner = result

    def check(self):
        h = [self.board[x: x + 3] for x in range(0, 9, 3)]
        v = [[self.board[x + y] for x in range(0, 9, 3)] for y in range(3)]
        d = [[self.board[x] for x in range(y, 9 - y, 4 - y)] for y in [0, 2]]
        winning_pos = []

        for i, x in enumerate(h + v + d):
            if x.count(x[0]) == len(x) and x[0] != '-':
                winning_pos.append(''.join([x[0], str(i)]))

        if winning_pos != []:
            return winning_pos
        if '-' not in self.board:
            return 'draw'
        return None
