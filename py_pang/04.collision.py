# PYPANG 충돌 처리
# 04.collision.py
import pygame
import os

# 파이게임 초기화
pygame.init()

# 클럭 설정
clock = pygame.time.Clock()

# 화면 설정
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("파이팡!")

# 이미지 경로 설정
path = os.path.dirname(__file__)
img_path = os.path.join(path, 'images')

# 이미지 불러오기
background = pygame.image.load(os.path.join(img_path, 'background.png'))
stage = pygame.image.load(os.path.join(img_path, 'stage.png'))
stage_height = stage.get_rect().size[1]
character = pygame.image.load(os.path.join(img_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width//2 - character_width//2
character_y_pos = screen_height - stage_height - character_height
character_speed = 0

# 무기 이미지
weapon = pygame.image.load(os.path.join(img_path, 'weapon.png'))
weapon_width = weapon.get_rect().size[0]

# 무기 정보
weapons = []
weapon_speed = 10

# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(img_path, 'balloon1.png')),
    pygame.image.load(os.path.join(img_path, 'balloon2.png')),
    pygame.image.load(os.path.join(img_path, 'balloon3.png')),
    pygame.image.load(os.path.join(img_path, 'balloon4.png'))
]

# 공 저장 변수와 초기 공 추가
balls = []
ball_speed_y = [-18, -15, -12, -9]
balls.append(
    {
        "pos_x": 50,
        "pos_y": 50,
        "img_idx": 0,
        "to_x": 3,
        "to_y": -6,
        "init_spd_y": ball_speed_y[0]
    }
)

# 제거할 공, 무기의 인덱스 초기화
ball_to_remove = -1
weapon_to_remove = -1

# 게임 루프
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_speed = -6
            elif event.key == pygame.K_RIGHT:
                character_speed = 6
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width//2 - weapon_width//2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    # 캐릭터 위치 업데이트
    character_x_pos += character_speed
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 업데이트
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 업데이트
    for ball_idx, ball_one in enumerate(balls):
        ball_pos_x = ball_one["pos_x"]
        ball_pos_y = ball_one["pos_y"]
        ball_img_idx = ball_one["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_rect[0]
        ball_height = ball_rect[1]

        # 공 가로 위치 확인
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_one["to_x"] *= -1

        # 공 세로 위치 확인
        if ball_pos_y > screen_height - stage_height - ball_height:
            ball_one["to_y"] = ball_one["init_spd_y"]
        else:
            ball_one["to_y"] += 0.5

        # 공 위치 업데이트
        ball_one["pos_x"] += ball_one["to_x"]
        ball_one["pos_y"] += ball_one["to_y"]

    # 충돌 처리
    # 캐릭터 rect 정보 가져오기
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 공 rect 정보 가져오기
    for ball_idx, ball_one in enumerate(balls):
        ball_pos_x = ball_one["pos_x"]
        ball_pos_y = ball_one["pos_y"]
        ball_img_idx = ball_one["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 무기  rect 정보 가져오기
        for weapon_idx, weapon_one in enumerate(weapons):
            weapon_pos_x = weapon_one[0]
            weapon_pos_y = weapon_one[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.top = weapon_pos_y
            weapon_rect.left = weapon_pos_x

            # 무기와 공 충돌 비교
            if weapon_rect.colliderect(ball_rect):
                # 제거할 공, 무기의 인덱스 추출
                ball_to_remove = ball_idx
                weapon_to_remove = weapon_idx
                break

        if ball_to_remove > -1:
            del balls[ball_to_remove]
            ball_to_remove = -1
        if weapon_to_remove > -1:
            del weapons[weapon_to_remove]
            weapon_to_remove = -1

    # 화면에 이미지 출력하기
    screen.blit(background, (0, 0))
    for one in weapons:
        screen.blit(weapon, (one[0], one[1]))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    for one in balls:
        ball_pos_x = one["pos_x"]
        ball_pos_y = one["pos_y"]
        ball_img_idx = one["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()
