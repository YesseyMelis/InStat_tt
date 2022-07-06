class XOTable:
    def __init__(self):
        self.table = [[[], [], []],
                      [[], [], []],
                      [[], [], []]]
        self.started = False
        self.turn_x = True

    def add_x(self, row: int, col: int):
        self.started = True
        if not self.table[row][col] and self.turn_x:
            self.table[row][col].append('x')
            self.turn_x = False

    def add_o(self, row: int, col: int):
        self.started = True
        if not self.table[row][col] and not self.turn_x:
            self.table[row][col].append('o')
            self.turn_x = True
