# 피하기게임 - bomb03.py
# 플레이어 이동하기

import pygame

# 변수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화 및 화면설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# 키 반복 설정하기
pygame.key.set_repeat(1)

# 이미지 불러오기
# 화면 중앙 하단 배치: centerx, bottom 속성 사용하기
player_url = 'resources/d_images/man.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2, bottom = SCREEN_HEIGHT)

# 게임루프 생성
while True:
    # 화면 배경 설정
    screen.fill(WHITE)

    # 키 입력 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        # 방향키로 캐릭터 이동하기
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.right += 5
        # 벽 충돌처리
        if player_pos.left < 0:
            player_pos.left = 0
        elif player_pos.right > SCREEN_WIDTH:
            player_pos.right = SCREEN_WIDTH

    # 주인공 이미지 출력하기
    screen.blit(player_img, player_pos)
    pygame.display.flip()

    # 프레임 설정
    clock.tick(60)

