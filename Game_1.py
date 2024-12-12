import pygame
import math

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game_1")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

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
pygame.draw.ellipse(screen, BLACK, (
    ellipse_center[0] - ellipse_width // 2, ellipse_center[1] - ellipse_height // 2, ellipse_width, ellipse_height))

def draw_star_with_lines(surface, color, center, size, num_lines):
    angle_step = 360 / num_lines
    for i in range(num_lines):
        angle = math.radians(i * angle_step)
        x_end = center[0] + size * math.cos(angle)
        y_end = center[1] + size * math.sin(angle)
        pygame.draw.line(surface, color, center, (x_end, y_end))

star_center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
star_size = 150
num_lines = 101

draw_star_with_lines(screen, YELLOW, star_center, star_size, num_lines)

pygame.display.flip()

def stay():
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

stay()
