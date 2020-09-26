# 파이팡 게임 화면 설정
# 01.screen_init.py
import pygame
import os

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

# 창 제목 변경하기
pygame.display.set_caption("PyPANG!")

# 이미지 경로 추출
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "images")

# 배경 이미지
background = pygame.image.load(os.path.join(img_path, "background.png"))

# 스테이지 이미지
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

running = True
# 게임 루프
while running:
    # 게임 종료 구현
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 화면 출력
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 화면 갱신
    pygame.display.update()

# 파이게임 종료
pygame.quit()
