# 1024 x 600 크기의 창 만들기
import pygame, time

# 창 크기 설정
pygame.init()
width, height = 1024, 600
size = (width, height)

# 창 만들기
screen = pygame.display.set_mode(size)

# 창 유지하기
time.sleep(2)
