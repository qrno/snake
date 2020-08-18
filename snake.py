from position import Position
from collections import deque

class Snake:
    snake = deque()
    direction = Position(0, 0)

    controls = {
            'w' : Position(-1, 0),
            'a' : Position(0, -1),
            's' : Position(1,  0),
            'd' : Position(0,  1)
    }

    def getHead(self):
        return self.snake[-1]
    def getTail(self):
        return self.snake[0]
    def removeTail(self):
        return self.snake.popleft()
    def getScore(self):
        return len(self.snake)

    def __init__(self, initialPos=Position(0,0)):
        self.snake.append(initialPos)

    def getDeltaPos(self, symbol):
        if symbol in self.controls:
            return self.controls[symbol]
        return Position(0, 0)

    def move(self, deltaPos):
        if deltaPos == -self.direction:
            deltaPos = self.direction
        self.snake.append(self.getHead()+deltaPos)
        if deltaPos != Position(0, 0):
            self.direction = deltaPos
