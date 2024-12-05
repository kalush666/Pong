import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game_1")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

image = 'background.jpg'
img = pygame.image.load(image)
img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))

screen.blit(img, (0, 0))

circle_radius = 50
circle_center = (circle_radius, WINDOW_HEIGHT // 2)
pygame.draw.circle(screen, RED, circle_center, circle_radius)

ellipse_width = 100
ellipse_height = 60
ellipse_center = (WINDOW_WIDTH - ellipse_width // 2, WINDOW_HEIGHT // 2)
pygame.draw.ellipse(screen, BLACK, (ellipse_center[0] - ellipse_width // 2, ellipse_center[1] - ellipse_height // 2, ellipse_width, ellipse_height))

pygame.display.flip()

def stay():
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

stay()
