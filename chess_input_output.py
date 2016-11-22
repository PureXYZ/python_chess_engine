from board import Board

class ChessIO:
    
    char_num_mapping = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
        
    def user_input(self, side_to_move, current_board):
        if side_to_move:
            print("White to move")
        else:
            print("Black to move")
            
        input_move = input("input:")
        input_move = input_move.strip()
        
        if len(input_move) > 10:
            print("Unrecognized input")
            return -2
        
        translated_move = -1
        
        if input_move == "0-0":
            if side_to_move:
                translated_move = ("00", (4, 0), (6, 0), (7, 0), (5, 0))
            else:
                translated_move = ("00", (4, 7), (6, 7), (7, 7), (5, 7))
            
        elif input_move == "0-0-0":
            if side_to_move:
                translated_move = ("000", (4, 0), (2, 0), (0, 0), (3, 0))
            else:
                translated_move = ("000", (4, 7), (2, 7), (0, 7), (3, 7))
            
        elif input_move[-4:] == "e.p.":
            input_move = input_move[:-4]
            
            translated_move_start_column = self.char_num_mapping[input_move[0]]
            translated_move_start_row = int(input_move[1])
            translated_move_end_column = self.char_num_mapping[input_move[3]]
            translated_move_end_row = int(input_move[4])
            
            translated_move = ("ep", (translated_move_start_column, translated_move_start_row), (translated_move_end_column, translated_move_end_row), (translated_move_end_column, translated_move_start_row))
            
        else:
            if input_move[0] in ["Q", "K", "N", "R", "B"]:
                input_move = input_move[:-1]
            
            translated_move_start_column = self.char_num_mapping[input_move[0]]
            translated_move_start_row = int(input_move[1])
            translated_move_end_column = self.char_num_mapping[input_move[3]]
            translated_move_end_row = int(input_move[4])
            
            translated_move = ((translated_move_start_column,translated_move_start_row),(translated_move_end_column,translated_move_end_row))
        
        
        return translated_move
        
        
        
    def checkmate(self, side_to_move):
        print("Checkmate")
        if side_to_move:
            print("White loses")
        else:
            print("Black loses")
            
            
    def check(self, side_to_move):
        if side_to_move:
            print("White in check")
        else:
            print("Black in check")
        
