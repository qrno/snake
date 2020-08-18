class Position:
    line = 0
    col  = 0
    def __init__(self, line=0, col=0):
        self.line = line
        self.col = col
    def __add__(self, other):
        return Position(self.line+other.line,
                self.col+other.col)
    def __neg__(self):
        return Position(-self.line, -self.col)
    def __eq__(self, other):
        return ((self.line == other.line) and 
                (self.col == other.col))
