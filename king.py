class King:

    value = 200

    def __init__(self, is_white, initial_coord):
        if is_white:
            self.is_white = True
        else:
            self.is_white = False

        self.coord = initial_coord
