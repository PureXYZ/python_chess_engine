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
    CONST_COORD_ROW = 1
    CONST_COORD_COLUMN = 0

    def __init__(self):
        #initialize board with starting piece positions
        self.board_rows = []

        for row in range(self.CONST_BOARD_ROWS):
            self.board_row = []

            for column in range(self.CONST_BOARD_COLUMNS):
                if row == 0:
                    if column == 0 or column == 7:
                        self.board_row.append(Rook(self.CONST_WHITE,(column, row)))
                    elif column == 1 or column == 6:
                        self.board_row.append(Knight(self.CONST_WHITE,(column, row)))
                    elif column == 2 or column == 5:
                        self.board_row.append(Bishop(self.CONST_WHITE,(column, row)))
                    elif column == 3:
                        self.board_row.append(Queen(self.CONST_WHITE,(column, row)))
                    elif column == 4:
                        self.board_row.append(King(self.CONST_WHITE,(column, row)))
                elif row == 1:
                    self.board_row.append(Pawn(self.CONST_WHITE,(column, row)))
                elif row == 6:
                    self.board_row.append(Pawn(self.CONST_BLACK,(column, row)))
                elif row == 7:
                    if column == 0 or column == 7:
                        self.board_row.append(Rook(self.CONST_BLACK,(column, row)))
                    elif column == 1 or column == 6:
                        self.board_row.append(Knight(self.CONST_BLACK,(column, row)))
                    elif column == 2 or column == 5:
                        self.board_row.append(Bishop(self.CONST_BLACK,(column, row)))
                    elif column == 3:
                        self.board_row.append(Queen(self.CONST_BLACK,(column, row)))
                    elif column == 4:
                        self.board_row.append(King(self.CONST_BLACK,(column, row)))
                else:
                    self.board_row.append(None)

            self.board_rows.append(self.board_row)

    def print_board_debug(self):
        #print board
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

    def is_in_board(self, coord):
        return coord[self.CONST_COORD_COLUMN] >= 0 and coord[self.CONST_COORD_COLUMN] < self.CONST_BOARD_COLUMNS\
               and coord[self.CONST_COORD_ROW] >= 0 and coord[self.CONST_COORD_ROW] < self.CONST_BOARD_ROWS

    def is_in_check(self, side):
        #find king coordinates of that side
        king_coord = None
        for row in range(self.CONST_BOARD_ROWS):
            for column in range(self.CONST_BOARD_COLUMNS):
                if type(self.board_rows[row][column]) == King and self.board_rows[row][column].is_white == side:
                    king_coord = (column, row)

        if king_coord == None:
            raise LookupError("King coord not found")

        #check rows from king to 0 (vertically)
        for row in range(king_coord[self.CONST_COORD_ROW] - 1, -1, -1):
            if self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]] is None:
                continue
            elif self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]].is_white == side:
                break
            elif type(self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]]) == Queen \
                or type(self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]]) == Rook:
                return True

        #check rows from king to 7 (vertically)
        for row in range(king_coord[self.CONST_COORD_ROW] + 1, 8, 1):
            if self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]] is None:
                continue
            elif self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]].is_white == side:
                break
            elif type(self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]]) == Queen \
                or type(self.board_rows[row][king_coord[self.CONST_COORD_COLUMN]]) == Rook:
                return True

        #check columns from king to 0 (horizontally)
        for column in range(king_coord[self.CONST_COORD_COLUMN] - 1, -1, -1):
            if self.board_rows[king_coord[self.CONST_COORD_ROW]][column] is None:
                continue
            elif self.board_rows[king_coord[self.CONST_COORD_ROW]][column].is_white == side:
                break
            elif type(self.board_rows[king_coord[self.CONST_COORD_ROW]][column]) == Queen \
                or type(self.board_rows[king_coord[self.CONST_COORD_ROW]][column]) == Rook:
                return True

        #check columns from king to 7 (horizontally)
        for column in range(king_coord[self.CONST_COORD_COLUMN] + 1, 8, 1):
            if self.board_rows[king_coord[self.CONST_COORD_ROW]][column] is None:
                continue
            elif self.board_rows[king_coord[self.CONST_COORD_ROW]][column].is_white == side:
                break
            elif type(self.board_rows[king_coord[self.CONST_COORD_ROW]][column]) == Queen \
                or type(self.board_rows[king_coord[self.CONST_COORD_ROW]][column]) == Rook:
                return True

        #check diagonals from king to NW
        for column, row in zip(range(king_coord[self.CONST_COORD_COLUMN] - 1, -1, -1),
                               range(king_coord[self.CONST_COORD_ROW] + 1, 8, 1)):
            if self.board_rows[row][column] is None:
                continue
            elif self.board_rows[row][column].is_white == side:
                break
            elif type(self.board_rows[row][column]) == Queen \
                or type(self.board_rows[row][column]) == Bishop:
                return True

        #check diagonals from king to NE
        for column, row in zip(range(king_coord[self.CONST_COORD_COLUMN] + 1, 8, 1),
                               range(king_coord[self.CONST_COORD_ROW] + 1, 8, 1)):
            if self.board_rows[row][column] is None:
                continue
            elif self.board_rows[row][column].is_white == side:
                break
            elif type(self.board_rows[row][column]) == Queen \
                or type(self.board_rows[row][column]) == Bishop:
                return True

        #check diagonals from king to SW
        for column, row in zip(range(king_coord[self.CONST_COORD_COLUMN] - 1, -1, -1),
                               range(king_coord[self.CONST_COORD_ROW] - 1, -1, -1)):
            if self.board_rows[row][column] is None:
                continue
            elif self.board_rows[row][column].is_white == side:
                break
            elif type(self.board_rows[row][column]) == Queen \
                or type(self.board_rows[row][column]) == Bishop:
                return True

        #check diagonals from king to SE
        for column, row in zip(range(king_coord[self.CONST_COORD_COLUMN] + 1, 8, 1),
                               range(king_coord[self.CONST_COORD_ROW] - 1, -1, -1)):
            if self.board_rows[row][column] is None:
                continue
            elif self.board_rows[row][column].is_white == side:
                break
            elif type(self.board_rows[row][column]) == Queen \
                or type(self.board_rows[row][column]) == Bishop:
                return True

        #check pawn
        if side == self.CONST_WHITE:
            if self.is_in_board((king_coord[self.CONST_COORD_COLUMN] - 1, king_coord[self.CONST_COORD_ROW] + 1)) \
                    and type(self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] - 1]) == Pawn \
                    and self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] - 1].is_white != side:
                return True
            elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN]  + 1, king_coord[self.CONST_COORD_ROW] + 1)) \
                    and type(self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] + 1]) == Pawn \
                    and self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] + 1].is_white != side:
                return True
        else:
            if self.is_in_board((king_coord[self.CONST_COORD_COLUMN] - 1, king_coord[self.CONST_COORD_ROW] - 1)) \
                    and type(self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] - 1]) == Pawn \
                    and self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] - 1].is_white != side:
                return True
            elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] + 1, king_coord[self.CONST_COORD_ROW] - 1)) \
                    and type(self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] + 1]) == Pawn \
                    and self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] + 1].is_white != side:
                return True

        #check knight
        if self.is_in_board((king_coord[self.CONST_COORD_COLUMN] - 1, king_coord[self.CONST_COORD_ROW] + 2)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] + 2][king_coord[self.CONST_COORD_COLUMN] - 1]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] + 2][king_coord[self.CONST_COORD_COLUMN] - 1].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] + 1, king_coord[self.CONST_COORD_ROW] + 2)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] + 2][king_coord[self.CONST_COORD_COLUMN] + 1]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] + 2][king_coord[self.CONST_COORD_COLUMN] + 1].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] - 2, king_coord[self.CONST_COORD_ROW] + 1)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] - 2]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] - 2].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] + 2, king_coord[self.CONST_COORD_ROW] + 1)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] + 2]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] + 1][king_coord[self.CONST_COORD_COLUMN] + 2].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] - 1, king_coord[self.CONST_COORD_ROW] - 2)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] - 2][king_coord[self.CONST_COORD_COLUMN] - 1]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] - 2][king_coord[self.CONST_COORD_COLUMN] - 1].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] + 1, king_coord[self.CONST_COORD_ROW] - 2)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] - 2][king_coord[self.CONST_COORD_COLUMN] + 1]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] - 2][king_coord[self.CONST_COORD_COLUMN] + 1].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] - 2, king_coord[self.CONST_COORD_ROW] - 1)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] - 2]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] - 2].is_white != side:
            return True
        elif self.is_in_board((king_coord[self.CONST_COORD_COLUMN] + 2, king_coord[self.CONST_COORD_ROW] - 1)) \
                and type(self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] + 2]) == Knight \
                and self.board_rows[king_coord[self.CONST_COORD_ROW] - 1][king_coord[self.CONST_COORD_COLUMN] + 2].is_white != side:
            return True

        #check king
        for row in range(king_coord[self.CONST_COORD_ROW] - 1, king_coord[self.CONST_COORD_ROW] + 2, 1):
            for column in range(king_coord[self.CONST_COORD_COLUMN] - 1, king_coord[self.CONST_COORD_COLUMN] + 2, 1):
                if self.is_in_board((column,row)):
                    if self.board_rows[row][column] is None or self.board_rows[row][column].is_white == side:
                        continue
                    elif type(self.board_rows[row][column]) == King and self.board_rows[row][column].is_white != side:
                        return True

        return False

    def board_with_piece_moved(self, start_coord, end_coord):
        new_board_rows = self.board_rows

        new_board_rows[end_coord[self.CONST_COORD_ROW]][end_coord[self.CONST_COORD_COLUMN]] \
            = new_board_rows[start_coord[self.CONST_COORD_ROW]][start_coord[self.CONST_COORD_COLUMN]]

        new_board_rows[start_coord[self.CONST_COORD_ROW]][start_coord[self.CONST_COORD_COLUMN]] = None

        return new_board_rows

    def move_piece(self, start_coord, end_coord):
        self.board_rows[end_coord[self.CONST_COORD_ROW]][end_coord[self.CONST_COORD_COLUMN]] \
            = self.board_rows[start_coord[self.CONST_COORD_ROW]][start_coord[self.CONST_COORD_COLUMN]]

        self.board_rows[start_coord[self.CONST_COORD_ROW]][start_coord[self.CONST_COORD_COLUMN]] = None

    def find_all_moves(self, side):
        move_list = []

        for row in range(self.CONST_BOARD_ROWS):
            for column in range(self.CONST_BOARD_COLUMNS):
                #find own pieces
                if self.board_rows[row][column] is None or self.board_rows[row][column].is_white != side:
                    continue
                else:
                    #pawn movement
                    if type(self.board_rows[row][column]) == Pawn:
                        if self.board_rows[row][column].is_white:
                            if self.is_in_board((column, row + 1)) and self.board_rows[row + 1][column] is None:
                                move_list.append(((column, row), (column, row + 1)))

                            if self.is_in_board((column, row + 2)) \
                                    and self.board_rows[row + 2][column] is None\
                                    and self.board_rows[row + 1][column] is None\
                                    and self.board_rows[row][column].initial_coord == (column, row):
                                move_list.append(((column, row), (column, row + 2)))

                            if self.is_in_board((column - 1, row + 1)) \
                                    and self.board_rows[row + 1][column - 1] is not None \
                                    and self.board_rows[row + 1][column - 1].is_white != side:
                                move_list.append(((column, row), (column - 1, row + 1)))

                            if self.is_in_board((column + 1, row + 1)) \
                                    and self.board_rows[row + 1][column + 1] is not None \
                                    and self.board_rows[row + 1][column + 1].is_white != side:
                                move_list.append(((column, row), (column + 1, row + 1)))
                        else:
                            if self.is_in_board((column, row - 1)) and self.board_rows[row - 1][column] is None:
                                move_list.append(((column, row), (column, row - 1)))

                            if self.is_in_board((column, row - 2)) \
                                    and self.board_rows[row - 2][column] is None\
                                    and self.board_rows[row - 1][column] is None\
                                    and self.board_rows[row][column].initial_coord == (column, row):
                                move_list.append(((column, row), (column, row - 2)))

                            if self.is_in_board((column - 1, row - 1)) \
                                    and self.board_rows[row - 1][column - 1] is not None \
                                    and self.board_rows[row - 1][column - 1].is_white != side:
                                move_list.append(((column, row), (column - 1, row - 1)))

                            if self.is_in_board((column + 1, row - 1)) \
                                    and self.board_rows[row - 1][column + 1] is not None \
                                    and self.board_rows[row - 1][column + 1].is_white != side:
                                move_list.append(((column, row), (column + 1, row - 1)))
                        continue

                    #knight movement
                    if type(self.board_rows[row][column]) == Knight:
                        if self.is_in_board((column - 1, row + 2)) \
                                and (self.board_rows[row + 2][column - 1] is None \
                                        or self.board_rows[row + 2][column - 1].is_white != side):
                            move_list.append(((column, row), (column - 1, row + 2)))
                            
                        if self.is_in_board((column + 1, row + 2)) \
                                and (self.board_rows[row + 2][column + 1] is None \
                                        or self.board_rows[row + 2][column + 1].is_white != side):
                            move_list.append(((column, row), (column + 1, row + 2)))
                            
                        if self.is_in_board((column - 2, row + 1)) \
                                and (self.board_rows[row + 1][column - 2] is None \
                                        or self.board_rows[row + 1][column - 2].is_white != side):
                            move_list.append(((column, row), (column - 2, row + 1)))
                            
                        if self.is_in_board((column + 2, row + 1)) \
                                and (self.board_rows[row + 1][column + 2] is None \
                                        or self.board_rows[row + 1][column + 2].is_white != side):
                            move_list.append(((column, row), (column + 2, row + 1)))
                            
                        if self.is_in_board((column - 1, row - 2)) \
                                and (self.board_rows[row - 2][column - 1] is None \
                                        or self.board_rows[row - 2][column - 1].is_white != side):
                            move_list.append(((column, row), (column - 1, row - 2)))
                            
                        if self.is_in_board((column + 1, row - 2)) \
                                and (self.board_rows[row - 2][column + 1] is None \
                                        or self.board_rows[row - 2][column + 1].is_white != side):
                            move_list.append(((column, row), (column + 1, row - 2)))
                            
                        if self.is_in_board((column - 2, row - 1)) \
                                and (self.board_rows[row - 1][column - 2] is None \
                                        or self.board_rows[row - 1][column - 2].is_white != side):
                            move_list.append(((column, row), (column - 2, row - 1)))
                            
                        if self.is_in_board((column + 2, row - 1)) \
                                and (self.board_rows[row - 1][column + 2] is None \
                                        or self.board_rows[row - 1][column + 2].is_white != side):
                            move_list.append(((column, row), (column + 2, row - 1)))
                        continue
                            


        return move_list

    def find_legal_moves(self, side):
        legal_move_list = []
        return legal_move_list




x = Board()
print(x.find_all_moves(False))
