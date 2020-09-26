# 파이팡 키 입력 처리
# 02. key_event.py
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
pygame.display.set_caption("PYPANG!")

# 이미지 경로 구하기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "images")

# 배경 이미지
background = pygame.image.load(os.path.join(img_path, "background.png"))

# 바닥 이미지
stage = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 이미지
character = pygame.image.load(os.path.join(img_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height

# 무기 이미지
weapon = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기 변수
weapons = []
weapon_speed = 10

# 캐릭터 이동 변수
character_to_x = 0
character_speed = 5

running = True
# 게임 루프
while running:
    # 프레임 설정
    dt = clock.tick(60)
    # 파이게임 종료 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width//2 - weapon_width // 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
               character_to_x = 0

    # 캐릭터 이동
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 화면 출력
    screen.blit(background, (0, 0))
    for one in weapons:
        screen.blit(weapon, one)

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()
