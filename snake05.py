import pygame

# 색상 상수 결정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기 상수 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 블록 크기 설정
BLOCK_SIZE = 20

# 블록 스리기 함수 설정
def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

# 화면 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 블록 위치 초기화
block_position = [0, 0]

# 게임 루프 실행
while True:
    # 이벤트 처리
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # 블록 이동 코드 작성
            if event.key == pygame.K_RIGHT:
                block_position[0] +=1
            if event.key == pygame.K_LEFT:
                block_position[0] -=1
            if event.key == pygame.K_UP:
                block_position[1] -=1
            if event.key == pygame.K_DOWN:
                block_position[1] +=1
    # 화면 그리기
    screen.fill(WHITE)
    draw_block(screen, GREEN, block_position)
    pygame.display.flip()
