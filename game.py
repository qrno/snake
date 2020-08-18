from board import Board
from snake import Snake
from position import Position
from random import randrange
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 800])

def drawBoard(board):
    dx = 0
    dy = 0
    size = 800/max(len(board), len(board[0]))
    for line in board:
        dx = 0
        for tile in line:
            color = (255, 255, 255)
            if tile == 'S':
                color = (0, 255, 0)
            if tile == 'O':
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (dx, dy, size, size))
            dx += size
        dy += size
    pygame.display.flip()


class Game:
    B = Board(20, 20)
    S = Snake(B.randomPos())

    def play(self):
        self.B.spawnFruit()
        last_key='d'
        while True:
            pygame.time.delay(200)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        last_key = 'w'
                    if event.key == pygame.K_LEFT:
                        last_key = 'a'
                    if event.key == pygame.K_DOWN:
                        last_key = 's'
                    if event.key == pygame.K_RIGHT:
                        last_key = 'd'

            deltaPos = self.S.getDeltaPos(last_key)
            self.S.move(deltaPos)
            self.B.iterate(self.S)
            drawBoard(self.B.board)

            if self.B.hasLost:
                pygame.time.delay(1000)
                print("SCORE: ", self.S.getScore())
                pygame.quit()

g = Game()
g.play()
