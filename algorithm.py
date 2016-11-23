from board import Board
from pawn import Pawn
import copy

class Algorithm:
    def __init__(self, initial_board):
        self.board_history = []
        #(board, side, move)
        self.board_history.append((initial_board, False, None))
        self.side_to_move = True

    def en_passant_move(self, side, board, last_move):
        en_passant_moves = []

        if last_move[0] == "ep" \
                or last_move[0] == "00" \
                or last_move[0] == "000" \
                or last_move[0] == "pp":
            return en_passant_moves

        last_move_start_row = last_move[0][1]
        last_move_start_column = last_move[0][0]
        last_move_end_row = last_move[1][1]
        last_move_end_column = last_move[1][0]
        current_board = copy.deepcopy(board)

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

        en_passant_moves = self.en_passant_move(side, board_history[0][0], board_history[0][2])

        if move in self.board_history[0][0].find_all_legal_moves(side, en_passant_moves):
            new_board = copy.deepcopy(self.board_history[0][0])
            new_board.move_piece(move)
            self.board_history.insert(0, (new_board, side, move))
            self.side_to_move = not self.side_to_move
            return 1
        else:
            return -1
        
    def negamax(self, side, board, last_move, depth):
        if last_move is not None:
            en_passant_moves = self.en_passant_move(side, board, last_move)
        else:
            en_passant_moves = []
            
        possible_moves = board.find_all_legal_moves(side, en_passant_moves)
        if len(possible_moves) == 0 or depth == 0:
            print("          negamax lowest node reached")
            print(board.evaluate_points(side, en_passant_moves))
            return board.evaluate_points(side, en_passant_moves)
        
        max_points = float("-inf")
        
        for move in possible_moves:
            print("     looking at move neganax loop:")
            print(move)
            copy_board = copy.deepcopy(board)
            copy_board.move_piece(move)
            x = -self.negamax(not side, copy_board, move, depth - 1)
            if x > max_points:
                max_points = x
        
        return max_points
            
    
    def make_computer_move(self, side):
        copy_board = copy.deepcopy(self.board_history[0][0])
        last_move = self.board_history[0][2]
        if last_move is not None:
            copy_board_ep = self.en_passant_move(side, copy_board, last_move)
        else:
            copy_board_ep = []
        depth = 1
        possible_moves = copy_board.find_all_legal_moves(side, copy_board_ep)
        
        analyzed_moves = []
        for move in possible_moves:
            print("looking at initial move:")
            print(move)
            analyzed_moves.append((move, self.negamax(side, copy_board, last_move, depth)))
        
        max_move_points = float("-inf")
        max_move = None
        for analysis in analyzed_moves:
            if analysis[1] > max_move_points:
                max_move_points = analysis[1]
                max_move = analysis[0]
            
        
        return max_move

