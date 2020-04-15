import pygame
import time

# 화면 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 80
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화
pygame.init()

# 화면 생성
screen = pygame.display.set_mode(SCREEN_SIZE)

# 화면 지연
time.sleep(3)
