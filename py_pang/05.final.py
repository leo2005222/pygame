# pypang_final.py
# 파이팡 만들기
# 1. 파이게임 초기화
# 2. 게임환경 초기화
# 3. 캐릭터 이동
# 4. 무기 발사
# 5. 공 추가
# 6. 충돌처리
# 7. 공 나누기
# 8. 메시지 출력

import pygame
import os

# 파이게임 초기화
pygame.init()

# FPS (Frame Per Second)
clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!!")

# 이미지 불러오기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, 'images')

background_img = pygame.image.load(os.path.join(img_path, 'background.png'))
stage_img = pygame.image.load(os.path.join(img_path, 'stage.png'))
stage_height = stage_img.get_rect().size[1]
character_img = pygame.image.load(os.path.join(img_path, 'character.png'))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_pos_x = screen_width//2 - character_width//2
character_pos_y = screen_height - stage_height - character_height
character_speed = 0
weapon_img = pygame.image.load(os.path.join(img_path, 'weapon.png'))
weapon_width = weapon_img.get_rect().size[0]
weapon_pos_x = character_pos_x + character_width // 2 - weapon_width // 2
weapon_pos_y = character_pos_y
weapon_speed = 10
weapons = []  # 무기 리스트 초기화
ball_img = [
    pygame.image.load(os.path.join(img_path, 'balloon1.png')),
    pygame.image.load(os.path.join(img_path, 'balloon2.png')),
    pygame.image.load(os.path.join(img_path, 'balloon3.png')),
    pygame.image.load(os.path.join(img_path, 'balloon4.png'))
]
ball_spd_y = [-18, -15, -12, -9]  # 공이 바닥에 닿으면 초기화 할 값
balls = [{
    'pos_x': 50,
    'pos_y': 50,
    'to_x': 3,
    'to_y': -6,
    'img_idx': 0,
    'init_spd_y': ball_spd_y[0]
}]

# 제거할 공과 무기 인덱스 초기화
remove_ball_idx = -1
remove_weapon_idx = -1

# 폰트 설정 및 타이머 초기화
game_font = pygame.font.Font(None, 40)

total_time = 30
start_time = pygame.time.get_ticks()

game_result = 'GAME OVER'

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
                weapon_pos_x = character_pos_x + character_width // 2 - weapon_width // 2
                weapon_pos_y = character_pos_y
                weapons.append([weapon_pos_x, weapon_pos_y])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    character_pos_x += character_speed
    if character_pos_x < 0:
        character_pos_x = 0
    if character_pos_x > screen_width - character_width:
        character_pos_x = screen_width - character_width

    # 무기 이동
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]]for w in weapons if w[1] > 0]

    # 공 이동
    for cur_ball in balls:
        cur_ball_img = ball_img[cur_ball['img_idx']]
        cur_ball_rect = cur_ball_img.get_rect().size
        cur_ball_width = cur_ball_rect[0]
        cur_ball_height = cur_ball_rect[1]

        if cur_ball['pos_y'] > screen_height - stage_height - cur_ball_height:
            cur_ball['to_y'] = cur_ball['init_spd_y']
        else:
            cur_ball['to_y'] += 0.5
        if cur_ball['pos_x'] > screen_width - cur_ball_width or cur_ball['pos_x'] < 0:
            cur_ball['to_x'] *= -1
        cur_ball['pos_x'] += cur_ball['to_x']
        cur_ball['pos_y'] += cur_ball['to_y']

    # 캐릭터 영역 추출
    character_rect = character_img.get_rect()
    character_rect.top = character_pos_y
    character_rect.left = character_pos_x

    # 충돌 처리
    for idx_ball, one_ball in enumerate(balls):
        # 공 영역 추출
        one_ball_rect = ball_img[one_ball['img_idx']].get_rect()
        one_ball_rect.top = one_ball['pos_y']
        one_ball_rect.left = one_ball['pos_x']

        # 공와 캐릭터 충돌 확인
        if one_ball_rect.colliderect(character_rect):
            running = False
            print("GAME OVER")

        # 공과 무기 충돌 확인
        for idx_weapon, one_weapon in enumerate(weapons):
            one_weapon_rect = weapon_img.get_rect()
            one_weapon_rect.top = one_weapon[1]
            one_weapon_rect.left = one_weapon[0]
            if one_ball_rect.colliderect(one_weapon_rect):
                remove_ball_idx = idx_ball
                remove_weapon_idx = idx_weapon

                # 공 추가하기
                if one_ball['img_idx'] < 3:
                    one_ball_width = one_ball_rect.size[0]
                    one_ball_height = one_ball_rect.size[1]
                    small_ball_rect = ball_img[one_ball['img_idx']+1].get_rect().size
                    small_ball_width = small_ball_rect[0]
                    small_ball_height = small_ball_rect[1]

                    balls.append({
                        'pos_x': one_ball['pos_x'] + one_ball_width//2 - small_ball_width//2,
                        'pos_y': one_ball['pos_y'] + one_ball_height//2 - small_ball_height//2,
                        'to_x': 3,
                        'to_y': -6,
                        'img_idx': one_ball['img_idx']+1,
                        'init_spd_y': ball_spd_y[one_ball['img_idx'] + 1]
                    })
                    balls.append({
                        'pos_x': one_ball['pos_x'] + one_ball_width//2 - small_ball_width//2,
                        'pos_y': one_ball['pos_y'] + one_ball_height//2 - small_ball_height//2,
                        'to_x': -3,
                        'to_y': -6,
                        'img_idx': one_ball['img_idx']+1,
                        'init_spd_y': ball_spd_y[one_ball['img_idx'] + 1]
                    })

                break
        if remove_weapon_idx > -1:
            del weapons[remove_weapon_idx]
            remove_weapon_idx = -1
        if remove_ball_idx > -1:
            del balls[remove_ball_idx]
            remove_ball_idx = -1
            if len(balls) == 0:
                game_result = "YOU WIN!"
                running = False

    # 화면 출력
    screen.blit(background_img, (0, 0))
    for one in weapons:
        screen.blit(weapon_img, (one[0], one[1]))
    for one in balls:
        screen.blit(ball_img[one['img_idx']], (one['pos_x'], one['pos_y']))
    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_pos_x, character_pos_y))

    # 타이머 출력
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer = game_font.render("TIME: {}".format(int(total_time - elapsed_time)), True, (255, 255, 0))
    screen.blit(timer, (10, 10))

    if int(total_time - elapsed_time) < 1:
        game_result = "TIME OVER"
        start_time = pygame.time.get_ticks()
        running = False

    # 화면 업데이트
    pygame.display.update()

# 메세지 출력
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(screen_width//2, screen_height//2))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)  # 2000ms는 2초

# 파이게임 종료
pygame.quit()
