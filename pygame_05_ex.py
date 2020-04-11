import pygame

pygame.init()

# 창 설정
width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)

# 이미지 불러오기
bug = pygame.image.load('exresources/image/bug.png')
grass = pygame.image.load('exresources/image/grass.png')
frog = pygame.image.load('exresources/image/frog.png')

# 창 유지하기
while True:
    screen.fill((0, 0, 0))
    # 배경 이미지 채우기
    grass_width = grass.get_width()
    grass_height = grass.get_height()
    for y in range(height // grass_height):
        for x in range(width // grass_width):
            screen.blit(grass, (x*100, y*75))
    # 버그
    bug_height = bug.get_height()
    for y in range(height // bug_height):
        screen.blit(bug, (0, y*51))
    # 개구리
    screen.blit(frog, (450, 300))
    pygame.display.flip()
    # 닫기 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
