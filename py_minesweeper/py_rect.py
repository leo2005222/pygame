# 도형 연습 파일
# py_rect.py

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))  # 화면에 흰색 채우기

    # 빨간색 직사각형 그리기
    pygame.draw.rect(screen, (255, 0, 0), (10, 20, 100, 50))

    # 빨간색 직사각형 (굵기: 3)
    pygame.draw.rect(screen, (255, 0, 0), (150, 10, 100, 30), 3)

    # 녹색: x:100, y: 80 좌표에 가로 80, 세로 50 사각형 그리기 (단위: 픽셀)
    pygame.draw.rect(screen, (0, 255, 0), ((100, 80), (80, 50)))
    # 파란색: x:200, y: 60 좌표에 가로 140, 세로 80 직사각형
    b_rect = pygame.Rect(200, 60, 140, 80)
    pygame.draw.rect(screen, (0, 0, 255), b_rect)

    # 노란색: x:30, y: 160 좌표에 가로 100, 세로 50 직사각형(R + G = Y)
    y_rect = pygame.Rect((30, 160), (100, 50))
    pygame.draw.rect(screen, (255, 255, 0), y_rect)

    # 파란선: (100, 100), (200, 200)
    pygame.draw.line(screen, (0, 0, 255), (100, 100), (200, 200))

    # 빨간선: 세로 80픽셀에 가로 10~200 사이의 수평선 그리기
    pygame.draw.line(screen, (255, 0, 0), (10, 80), (200, 80))

    # 녹색선: 가로 250픽셀에 화면을 분할하는 수직선 그리기
    pygame.draw.line(screen, (0, 255, 0), (250, 0), (250, 300))

    # 화면 업데이트
    pygame.display.update()
