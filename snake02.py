import pygame
import time

# 색 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# 화면 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 80
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화
pygame.init()

# 화면 생성
screen = pygame.display.set_mode(SCREEN_SIZE)

# 화면 전체에 흰색 채우기
screen.fill(WHITE)

# 사각형 그리기
# pygame.Rect((x,y), (width, height))
# 화면 왼쪽에 녹색 사각형 그리기
green_rect = pygame.Rect((10, 10), (30, 30))
pygame.draw.rect(screen, GREEN, green_rect)

# 화면 우측 하단에 빨강 사각형(80, 30) 그리기
red_rect = pygame.Rect((310, 40), (80, 30))
pygame.draw.rect(screen, RED, red_rect)

# 화면 갱신 후 3초 기다리기
pygame.display.flip()
time.sleep(3)
