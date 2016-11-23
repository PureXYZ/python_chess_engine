from board import Board
from algorithm import Algorithm
from chess_input_output import ChessIO


game = Algorithm(Board())

WHITE = True
BLACK = False

side_to_move = WHITE


game.board_history[0][0].print_board_debug()

while True:
    
    current_board = game.board_history[0][0]
    last_move = game.board_history[0][2]
    
    if len(game.board_history) > 1:
        ep = game.en_passant_move(side_to_move, current_board, last_move)
    else:
        ep = []
    
    if len(current_board.find_all_legal_moves(side_to_move, ep)) == 0:
        ChessIO().checkmate(side_to_move)
        break
        
    #stalemate check here
    
    if current_board.is_in_check(side_to_move):
        ChessIO().check(side_to_move)
    
    #move = ChessIO().user_input(side_to_move, current_board)
    
    move = game.make_computer_move(side_to_move)
    
    
    if move == -1 or move == -2:
        print("Input not recognized, try again")
        continue
         
    #move_result = game.make_user_move(side_to_move, move)
    
    """if move_result == -1:
        print("Invalid move, try again")
        continue"""
        
    side_to_move = not side_to_move
    
    game.board_history[0][0].print_board_debug()