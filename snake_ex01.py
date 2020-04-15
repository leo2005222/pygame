# 파이게임을 이용해 체크 무늬 배경 만들기
# 빨강, 녹색 (20x20) 블록으로 줄무늬를 만든다
# 블로 그리기 함수를 선언하고 사용한다.
# def draw_block(screen, color, position)

import pygame
import time

# 상수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 화면 크기 상수 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 블륵크기 상수 설정
BLOCK_SIZE = 10

# 블록 스리기 함수
def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

# 화면 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 줄무늬 그리기
for bx in range(0, SCREEN_WIDTH // BLOCK_SIZE + 1, 2):
    for by in range(0, SCREEN_HEIGHT//BLOCK_SIZE + 1, 2):
        draw_block(screen, GREEN, (bx, by))
        draw_block(screen, RED, (bx + 1, by))
        draw_block(screen, RED, (bx, by + 1))
        draw_block(screen, GREEN, (bx + 1, by + 1))
        time.sleep(0.01)
        # 화면 업데이트
        pygame.display.flip()

# 화면 지연
time.sleep(3)
