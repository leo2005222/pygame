# 파이게임 이미지 처리

import pygame

# 창 설정하기
width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

# 이미지 불러오기
player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')

# 창 유지하기
while True:
    screen.fill((0, 0, 0))
    # 배경 이미지 채우기
    grass_width = grass.get_width()
    grass_height = grass.get_height()
    for y in range(height // grass_height + 1):
        for x in range(width // grass_width + 1):
            screen.blit(grass, (x*grass_width, y*grass_height))
    # 캐슬 이미지 채우기
    castle_height = castle.get_height()
    for y in range(height // castle_height):
        screen.blit(castle, (0, 30 + y * castle_height))
    # 토끼 이미지 그리기
    screen.blit(player, (100, 100))
    pygame.display.flip()

    # 닫기 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
