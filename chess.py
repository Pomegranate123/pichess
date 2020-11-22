b = [[0 for i in range(8)] for j in range(8)]

WHITE = -1
BLACK = 1
PAWN = "Pawn"
KNIGHT = "Knight"
BISHOP = "Bishop"
ROOK = "Rook"
QUEEN = "Queen"
KING = "King"

def print_board(board):
    for row in board:
        print([piece.icon if piece else ' ' for piece in row])


class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.moved = False

    def add(self, board):
        board[self.y][self.x] = self
        return board

    def possible_moves(self, board):
        raise NotImplementedError()


class Pawn(Piece):
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if self.color == WHITE:
            self.icon = "♟︎"
        elif self.color == BLACK:
            self.icon = "♙"
        self.name = PAWN
        self.value = 1
        self.enpassant = False

    def possible_moves(self, board):
        moves = []

        # Kan de pion schuin slaan?
        for i in [-1, 1]:
            piece = board[self.y + self.color][self.x - i]
            if piece and piece.color != self.color:
                    moves.append([self.x - i, self.y + self.color])

        # Kan de pion en passant slaan?
        for i in [-1, 1]:
            piece = board[self.y][self.x - i]
            if piece and piece.color != self.color and piece.name == PAWN and piece.enpassant == True:
                    moves.append([self.x - i, self.y + self.color])

        # Kan de pion rechtdoor?
        piece = board[self.y + self.color * i][self.x]
        if not piece:
            moves.append([self.x, self.y + self.color])

            # Kan de pion twee stappen doen?
            if self.moved == False:
                piece = board[self.y + self.color * i][self.x]
                if not piece:
                    moves.append([self.x, self.y + self.color])
        return moves


class Knight(Piece):
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if self.color == WHITE:
            self.icon = "♞"
        elif self.color == BLACK:
            self.icon = "♘"
        self.name = KNIGHT
        self.value = 3


class Bishop(Piece):
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if self.color == WHITE:
            self.icon = "♝"
        elif self.color == BLACK:
            self.icon = "♗"
        self.name = BISHOP
        self.value = 3


class Rook(Piece):
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if self.color == WHITE:
            self.icon = "♜"
        elif self.color == BLACK:
            self.icon = "♖"
        self.name = ROOK
        self.value = 5


class Queen(Piece):
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if self.color == WHITE:
            self.icon = "♛"
        elif self.color == BLACK:
            self.icon = "♕"
        self.name = QUEEN
        self.value = 9


class King(Piece):
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if self.color == WHITE:
            self.icon = "♛"
        elif self.color == BLACK:
            self.icon = "♕"
        self.name = KING
        self.value = float('inf')

if __name__ == "__main__":    
    white_pawn = Pawn(WHITE, 1, 4)
    b = white_pawn.add(b)
    b = Pawn(BLACK, 2, 3).add(b)
    b = Pawn(BLACK, 1, 3).add(b)
    print_board(b)
    print(white_pawn.possible_moves(b))