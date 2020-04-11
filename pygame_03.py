# 파이게임 창 설정하기

import pygame

# pygame 초기화 및 창 설정
pygame.init()

width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

# 창 유지
while True:
    # 창 배경색 변경
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    pygame.display.flip()

    # 닫기 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
