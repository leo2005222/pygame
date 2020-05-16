# 스페이스 인베이더 - 02

import pygame
import os
import random

# 변수 설정
WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 창 타이틀 설정
pygame.display.set_caption("SPACE INVADER")

# 파이게임 초기화
pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)

# 배경이미지 처리
bg_img = pygame.image.load(os.path.join("assets", "background-black.png"))
bg_img = pygame.transform.scale(bg_img, SCREEN_SIZE)

# player 비행기
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# enemy 비행기
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))

# 우주선 클래스 생성
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
    def draw(self, window):
        # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.max_health = health

class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = RED_SPACE_SHIP

    def move(self, vel):
        self.y += vel


# 메인 함수 구현
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    # 적군 생성
    enemies = []
    wave_length = 5
    enemy_vel = 1

    # 우주선 생성
    player_vel = 5
    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(bg_img, (0, 0))

        lives_label = main_font.render(f"Lives {lives}", 1, WHITE)
        level_label = main_font.render(f"Level {level}", 1, WHITE)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (SCREEN_WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(60)
        redraw_window()

        if len(enemies) == 0:
            wave_length +=5
            for i in range(wave_length):
                enemy = Enemy(random.randint(50, 700), random.randint(-1000, -100))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel < SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel < SCREEN_HEIGHT - player.get_height():
            player.y += player_vel

        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)

main()
