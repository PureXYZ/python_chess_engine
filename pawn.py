class Pawn:

    value = 1

    def __init__(self, is_white, initial_coord):
        if is_white:
            self.is_white = True
        else:
            self.is_white = False

        self.coord = initial_coord
        self.initial_coord = initial_coord
        self.moved = False
