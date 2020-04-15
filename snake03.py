import pygame
import time

# 색 정의하기
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (255, 0, 0)
RED = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 화면 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

# 블록 그리기
BLOCK_SIZE = 20
block_red = pygame.Rect((1 * BLOCK_SIZE, 1 * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, RED, block_red)
block_green = pygame.Rect((1 * BLOCK_SIZE, 3 * BLOCK_SIZE),
                          (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, GREEN, block_green)
block_blue = pygame.Rect((1 * BLOCK_SIZE, 5 * BLOCK_SIZE),
                         (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, BLUE, block_blue)

# 화면 갱신
pygame.display.flip()

# 3초간 창 지연
time.sleep(3)
