class Pawn:

    value = 1

    def __init__(self, is_white):
        if is_white == True:
            self.is_white = True
        else:
            self.is_white = False