# 피하기 게임 - bomb02.py
# 플레이어 이미지를 화면 중앙 하단에 위치하기

import pygame

# 변수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 포기화 및 화면설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 이미지 불러오기
player_url = 'resources/d_images/man.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect()

# 이미지 위치 설정하기
player_pos.left = (SCREEN_WIDTH // 2) - (player_img.get_width() // 2)
player_pos.top = SCREEN_HEIGHT - player_img.get_height()

# 게임루프
while True:
    # 화면 배경색 설정
    screen.fill(WHITE)

    # 파이게임 이벤트 처리하기
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    # 이미지 출력하고, 화면 업데이트 하기
    screen.blit(player_img, player_pos)
    pygame.display.flip()

