b = [[0]*8]*8

WHITE = -1
BLACK = 1

def print_board(board):
    for row in board:
        print(row)

class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.moved = False

class Pawn(Piece):
    """def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        self.moved = False"""

    def possible_moves(self, board):
        moves = []
        moves.append([self.x, self.y + self.color])
        if self.moved == False:
            moves.append([self.x, self.y + self.color * 2])
        return moves

white_pawn = Pawn(WHITE, 1, 4)
print(white_pawn.possible_moves(b))