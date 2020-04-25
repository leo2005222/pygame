# 피하기 게임 - bomb03.py
# 덩 이미지 그리기

import pygame
import random

# 변수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 포기화 및 화면 설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 키 반복 입력 설정, 프레임 설정
pygame.key.set_repeat(1)
clock = pygame.time.Clock()

# 이미지 불러오기
player_url = 'resources/d_images/man.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2, bottom = SCREEN_HEIGHT)

# 적 이미지 불러오기
enemy_url = 'resources/d_images/poop.png'
enemy_img = pygame.image.load(enemy_url)
# enemies = list()
enemies = []
for cnt in range(3):
    enemy_pos = enemy_img.get_rect(left = 150 * cnt + 100, top = 100)
    enemies.append(enemy_pos)
    print(enemy_pos)

# 게임루프
while True:
    # 화면 배경색으로 지우기
    screen.fill(WHITE)

    # 키 입력 처리
    event = pygame.event.poll()

    # 파이게임 종료처리
    if event.type == pygame.QUIT:
        exit()

    # 주인공 이동처리
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -=5
        elif event.key == pygame.K_RIGHT:
            player_pos.right +=5
        # 주인공 벽처리
        if player_pos.left < 0:
            player_pos.left = 0
        if player_pos.right > SCREEN_WIDTH:
            player_pos.right = SCREEN_WIDTH

    # 적 내려오기
    for one in enemies:
        one.top += 5
        if one.bottom > SCREEN_HEIGHT:
            one.top = -100
            one.left = random.randint(0, SCREEN_WIDTH - enemy_img.get_width())
    # 이미지 그리기 및 화면 업데이트
    screen.blit(player_img, player_pos)
    for one in enemies:
        screen.blit(enemy_img, one)
    pygame.display.flip()

    # 프레임 설정하기
    clock.tick(100)
