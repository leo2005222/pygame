# 폭탄 피하기 게임 (bomb01.py)
# 이미지 그리기

import pygame

# 변수 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화 및 화면 설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 이미지 불러오기
player_url = 'resources/d_images/man.png'
player_img = pygame.image.load(player_url)

# 게임 루프 생성
while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    # 화면에 플레이어 이미지 보여주기
    screen.blit(player_img, (300, 700))

    pygame.display.flip()

