import pygame
import os
# 파이게임 초기화
pygame.init()

# 화면 설정(640x480)
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)

# 창 제목 설정
pygame.display.set_caption("파이 팡!")

# FPS
clock = pygame.time.Clock()

# 파일 경로 추출
current_path = os.path.dirname(__file__) #현재 파일 경로 반환
image_path = os.path.join(current_path, "images")

# 게임 이미지 불러오기 (배경, 플레이어)
background = pygame.image.load(os.path.join(image_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - stage_height - character_height

# 캐릭터 이동 변수
character_to_x = 0
character_speed = 5

# 게임 루프 설정
running = True
while running:
    st = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    # 플레이어 처리
    character_x_pos += character_to_x

    # 충돌 처리

    # 화면 출력
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()


# 파이게임 종료
pygame.quit()
