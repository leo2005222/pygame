# 파이게임 키입력 처리

import pygame

# 화면 크기, 색상 상수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 주인공 좌표
player_pos = [100, 100]

while True:
    screen.fill(BLACK)

    for bx in range(SCREEN_WIDTH // grass.get_width() + 1):
        for by in range(SCREEN_HEIGHT // grass.get_height() + 1):
            screen.blit(grass, (bx * grass.get_width(), by * grass.get_height()))
    # 캐슬 그리기
    for cy in range(SCREEN_HEIGHT // castle.get_height()):
        screen.blit(castle, (0, 30 + cy * castle.get_height()))

    # 토끼 그리기
    screen.blit(player, player_pos)

    # 화면 갱신
    pygame.display.flip()

    # 이벤트 처리
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()