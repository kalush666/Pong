import pygame
import pygame.draw

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

pygame.init()
size = (WINDOW_WIDTH,WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game_1")

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

screen.fill(WHITE)
pygame.display.flip()

def stay():
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True


image = 'background.jpg'
img = pygame.image.load(image)
img = pygame.transform.scale(img,(WINDOW_WIDTH,WINDOW_HEIGHT))
screen.blit(img, (0, 0))
pygame.display.flip()
stay()