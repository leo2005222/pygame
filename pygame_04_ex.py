# 파이게임 창 만들고 이미지 불러오기
# 이미지 크기는 300x300이내 사이즈
# pixlr, photopea에서 편집 혹은 투명 배경 이미지 추천

import pygame

pygame.init()

# 창 설정하기
width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

# 이미지 불러오기
player = pygame.image.load('exresources/image/dog.png')

# 창 종료 이벤트 처리까지 유효하기
while True:
    # 화면을 검정색으로
    screen.fill((0, 0, 0))
    screen.blit(player, (100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)
