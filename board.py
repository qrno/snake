from position import Position
from random import randrange

class Board:
    board = []

    BLANK = '.'
    PLAYER = 'S'
    FRUIT = 'O'
    WALL = '#'

    lineA = 10
    colA = 10

    hasLost = False

    def __init__(self, lineA=10, colA=10):
        self.lineA = lineA
        self.colA  = colA
        self.board = [[self.BLANK for x in range(colA)] for y in range(lineA)]

    def printBoard(self):
        for line in range(self.lineA):
            for col in range(self.colA):
                print(self.board[line][col], end='')
            print()

    def valid(self, position):
        if (position.line < 0) or (position.line >= self.lineA):
            return False
        if (position.col < 0) or (position.col >= self.colA):
            return False
        return True

    def empty(self, position):
        if not self.valid(position):
            return False

        symbol = self.board[position.line][position.col]
        if symbol == self.BLANK:
            return True
        return False

    def randomPos(self):
        return Position(randrange(self.lineA),
                randrange(self.colA))

    def iterate(self, S):
        headPos = S.getHead()
        headTile = self.getChar(headPos)

        fruitEaten = (headTile == self.FRUIT)
        self.hasLost = self.hasLost or ((headTile == self.PLAYER) or not self.valid(headPos))

        self.setChar(headPos, self.PLAYER)

        if fruitEaten:
            self.spawnFruit()
        else :
            tailPos = S.getTail()
            S.removeTail()
            self.setChar(tailPos, self.BLANK)

    def getChar(self, position):
        if self.valid(position):
            return self.board[position.line][position.col]
        return self.WALL
    def setChar(self, position, symbol):
        if self.valid(position):
            self.board[position.line][position.col] = symbol

    def spawnFruit(self):
        fruitPos = self.randomPos()
        while not self.empty(fruitPos):
            fruitPos = self.randomPos()
        self.setChar(fruitPos, self.FRUIT)
