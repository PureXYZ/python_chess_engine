class ChessIO:
        
    def user_input(self, side_to_move):
        if side_to_move:
            print("White to move")
        else:
            print("Black to move")
            
        input_move = input("input:")
        start_column = int(input_move[0])
        start_row = int(input_move[1])
        end_column = int(input_move[2])
        end_row = int(input_move[3])
        
        return ((start_column, start_row), (end_column, end_row))
        
        
        
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
        
