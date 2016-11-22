from board import Board
from pawn import Pawn
import copy

class Algorithm:
    def __init__(self, initial_board):
        self.board_history = []
        #(board, side, move)
        self.board_history.append((initial_board, False, None))
        self.side_to_move = True

    def en_passant_move(self, side):
        en_passant_moves = []

        if len(self.board_history) <= 1 or self.board_history[0][2][0] == "ep":
            return en_passant_moves

        last_move_start_row = self.board_history[0][2][0][1]
        last_move_start_column = self.board_history[0][2][0][0]
        last_move_end_row = self.board_history[0][2][1][1]
        last_move_end_column = self.board_history[0][2][1][0]
        current_board = copy.deepcopy(self.board_history[0][0])

        if type(current_board.board_rows[last_move_end_row][last_move_end_column]) == Pawn:
            if abs(last_move_end_row - last_move_start_row) == 2:
                if current_board.is_in_board((last_move_end_column - 1, last_move_end_row)):
                    if current_board.board_rows[last_move_end_row][last_move_end_column - 1] is not None \
                            and type(current_board.board_rows[last_move_end_row][last_move_end_column - 1]) == Pawn \
                            and current_board.board_rows[last_move_end_row][last_move_end_column - 1].is_white == side:
                        if side == True:
                            en_passant_moves.append(("ep", (last_move_end_column - 1, last_move_end_row), (last_move_end_column, last_move_end_row + 1), (last_move_end_column, last_move_end_row)))
                        else:
                            en_passant_moves.append(("ep", (last_move_end_column - 1, last_move_end_row), (last_move_end_column, last_move_end_row - 1), (last_move_end_column, last_move_end_row)))

                if current_board.is_in_board((last_move_end_column + 1, last_move_end_row)):
                    if current_board.board_rows[last_move_end_row][last_move_end_column + 1] is not None \
                            and type(current_board.board_rows[last_move_end_row][last_move_end_column + 1]) == Pawn \
                            and current_board.board_rows[last_move_end_row][last_move_end_column + 1].is_white == side:
                        if side == True:
                            en_passant_moves.append(("ep", (last_move_end_column + 1, last_move_end_row), (last_move_end_column, last_move_end_row + 1), (last_move_end_column, last_move_end_row)))
                        else:
                            en_passant_moves.append(("ep", (last_move_end_column + 1, last_move_end_row), (last_move_end_column, last_move_end_row - 1), (last_move_end_column, last_move_end_row)))

        return en_passant_moves
    
    def make_user_move(self, side, move):
        
        if side != self.side_to_move:
            raise ValueError("Not user side to move")

        en_passant_moves = self.en_passant_move(side)

        if move in self.board_history[0][0].find_all_legal_moves(side, en_passant_moves):
            new_board = copy.deepcopy(self.board_history[0][0])
            new_board.move_piece(move)
            self.board_history.insert(0, (new_board, side, move))
            self.side_to_move = not self.side_to_move
            return 1
        else:
            return -1
    
    def computer_move(self, side):
        return False

