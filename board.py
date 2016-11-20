from king import King
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight
from pawn import Pawn


class Board:

    CONST_BOARD_ROWS = 8
    CONST_BOARD_COLUMNS = 8
    CONST_WHITE = True
    CONST_BLACK = False

    def __init__(self):
        self.board_rows = []

        for row in range(self.CONST_BOARD_ROWS):
            self.board_row = []

            for column in range(self.CONST_BOARD_COLUMNS):
                if row == 0:
                    if column == 0 or column == 7:
                        self.board_row.append(Rook(self.CONST_WHITE))
                    elif column == 1 or column == 6:
                        self.board_row.append(Knight(self.CONST_WHITE))
                    elif column == 2 or column == 5:
                        self.board_row.append(Bishop(self.CONST_WHITE))
                    elif column == 3:
                        self.board_row.append(Queen(self.CONST_WHITE))
                    elif column == 4:
                        self.board_row.append(King(self.CONST_WHITE))
                elif row == 1:
                    self.board_row.append(Pawn(self.CONST_WHITE))
                elif row == 6:
                    self.board_row.append(Pawn(self.CONST_BLACK))
                elif row == 7:
                    if column == 0 or column == 7:
                        self.board_row.append(Rook(self.CONST_BLACK))
                    elif column == 1 or column == 6:
                        self.board_row.append(Knight(self.CONST_BLACK))
                    elif column == 2 or column == 5:
                        self.board_row.append(Bishop(self.CONST_BLACK))
                    elif column == 3:
                        self.board_row.append(Queen(self.CONST_BLACK))
                    elif column == 4:
                        self.board_row.append(King(self.CONST_BLACK))
                else:
                    self.board_row.append(None)

            self.board_rows.append(self.board_row)

    def print_board_debug(self):
        for row in reversed(self.board_rows):
            for piece in row:
                if piece is None:
                    print("| _ |", end="")
                elif type(piece) is Pawn and piece.is_white == self.CONST_WHITE:
                    print("| p |", end="")
                elif type(piece) is Pawn and piece.is_white == self.CONST_BLACK:
                    print("| P |", end="")
                elif type(piece) is Rook and piece.is_white == self.CONST_WHITE:
                    print("| r |", end="")
                elif type(piece) is Rook and piece.is_white == self.CONST_BLACK:
                    print("| R |", end="")
                elif type(piece) is Knight and piece.is_white == self.CONST_WHITE:
                    print("| n |", end="")
                elif type(piece) is Knight and piece.is_white == self.CONST_BLACK:
                    print("| N |", end="")
                elif type(piece) is Bishop and piece.is_white == self.CONST_WHITE:
                    print("| b |", end="")
                elif type(piece) is Bishop and piece.is_white == self.CONST_BLACK:
                    print("| B |", end="")
                elif type(piece) is Queen and piece.is_white == self.CONST_WHITE:
                    print("| q |", end="")
                elif type(piece) is Queen and piece.is_white == self.CONST_BLACK:
                    print("| Q |", end="")
                elif type(piece) is King and piece.is_white == self.CONST_WHITE:
                    print("| k |", end="")
                elif type(piece) is King and piece.is_white == self.CONST_BLACK:
                    print("| K |", end="")
            print("\n")





