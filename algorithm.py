from board import Board
import copy

class Algorithm:
    def __init__(self, initial_board):
        self.board_history = []
        #(board, side, move)
        self.board_history.append((initial_board, False, None))
        self.side_to_move = True
        
    
    def en_passant_move_list(self, move_list, side):
        return False
    
    def find_possible_moves(self, side):
        all_moves = self.board_history[0][0].find_all_moves(side)
        check_free_moves = []
        
        for move in all_moves:
            test_check = copy.deepcopy(self.board_history[0][0])
            test_check.move_piece(move[0], move[1])
            if not test_check.is_in_check(side):
                check_free_moves.append(move)
        
        return check_free_moves
    
    def make_user_move(self, side, move):
        
        if side != self.side_to_move:
            raise ValueError("Not user side to move")
        
        if move in self.find_possible_moves(side):
            new_board = copy.deepcopy(self.board_history[0][0])
            new_board.move_piece(move[0], move[1])
            self.board_history.insert(0, (new_board, side, move))
            self.side_to_move = not self.side_to_move
            return 1
        else:
            return -1
    
    def computer_move(self, side):
        return False
    