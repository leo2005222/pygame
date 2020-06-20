'''
스페이스 인베이더

1. 화면 설정 및 배경 이미지 출력
2. 플레이어 조작하기
3. 적 생성하기
4. 플레이어 레이저 발사
5. 레이저 발사 속도 설정
'''

import pygame
import os
import random

# 변수 초기화
WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화 및 창 제목 설정
pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("스페이스 인베이더")

# 배경 이미지 처리
bg_img = pygame.image.load(os.path.join('assets', 'background-black.png'))
bg_img = pygame.transform.scale(bg_img, SCREEN_SIZE)

# 이미지 불러오기
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))
RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))


# 비행선 클래스 만들기
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


# 아군 비행기 클래스
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP


# 메인 함수
def main():
    run = True
    FPS = 60
    level = 0
    lives = 5

    clock = pygame.time.Clock()

    player = Player(350, 600)
    player_vel = 5

    main_font = pygame.font.SysFont('comicsans', 50)

    # 화면 갱신 함수
    def redraw_window():
        WIN.blit(bg_img, (0, 0))

        lives_label = main_font.render(f"Lives:{lives}", 1, WHITE)
        level_label = main_font.render(f"Level:{level}", 1, WHITE)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (SCREEN_WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel >= 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel <= SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel >= 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel <= SCREEN_HEIGHT - player.get_height():
            player.y += player_vel




# 게임 실행
main()