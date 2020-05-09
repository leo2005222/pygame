# 폭탄 피하기 - bomb05.py

import pygame
import random

# 변수 설정 (튜플)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 변수 초기화
score = 0
enemy_num = 10
gameover = False

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bomb GAME! - MinKwang")
frame = pygame.time.Clock()
pygame.key.set_repeat(1)

# 글꼴 설정
small_font = pygame.font.SysFont("Agency FB", 36)
large_font = pygame.font.SysFont("HYNAML", 72)

# 이미지 불러오기
player_url = "resources/d_images/man.png"
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH//2,
                                 bottom = SCREEN_HEIGHT)
# 적 이미지 불러오기
enemy_url = "resources/d_images/poop.png"
enemy_img = pygame.image.load(enemy_url)
# enemies_info는 적의 좌표와 속도를 리스트로 저장하는 리스트
enemies_info = []
for cnt in range(enemy_num):
    enemy_pos = enemy_img.get_rect(left = random.randint(0, SCREEN_WIDTH-enemy_img.get_width()),
                                   bottom = -100 * cnt)
    enemy_speed = random.randint(5, 15)
    enemies_info.append([enemy_pos, enemy_speed])

# 음악 불러오기
pygame.mixer.init()
bgm_url = 'resources/audio/buk.mp3'
pygame.mixer.music.load(bgm_url)
pygame.mixer.music.play(-1)

# 게임 루프 생성
while True:
    # 이벤트 처리
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos.left -= 5
            elif event.key == pygame.K_RIGHT:
                player_pos.left +=5

    # 벽 충돌처리
    if player_pos.left<0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    # 적 이동하기
    if not gameover:
        for one in enemies_info:
            one[0].top += one[1]
            if one[0].top > 800:
                one[0].left = random.randint(0, SCREEN_WIDTH - enemy_img.get_width())
                one[0].top = -100
                one[1] = random.randint(5, 15)
                score += 1
                if (score % 10 == 0):
                    enemy_pos = enemy_img.get_rect(left=random.randint(0, SCREEN_WIDTH - enemy_img.get_width()),
                                                   bottom=-100 * cnt)
                    enemy_speed = random.randint(5, 15)
                    enemies_info.append([enemy_pos, enemy_speed])

    # 적 충돌처리
    for one in enemies_info:
        if one[0].colliderect(player_pos):
            gameover = True

    # 화면 이미지 출력하기
    screen.fill(WHITE)
    screen.blit(player_img, player_pos)
    for one in enemies_info:
        screen.blit(enemy_img, one[0])

    # 점수 출력
    score_img = small_font.render("SCORE: {}".format(score), True, BLACK)
    screen.blit(score_img, (10, 10))

    # 게임종료
    if gameover:
        gameover_img = large_font.render("게임종료", True, BLACK)
        screen.blit(gameover_img, (SCREEN_WIDTH // 2 - gameover_img.get_width() // 2,
                                   SCREEN_HEIGHT // 2 - gameover_img.get_height() // 2))

    pygame.display.flip()
    frame.tick(60)
