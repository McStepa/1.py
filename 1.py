import pygame
import random


WIDTH = 1600
HEIGHT = 900

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (50, 150, 50)
GREEN = (0, 255, 0)
BLUE = (117, 187, 253)
GRAYF = (58, 58, 58)
METAL1 = (222, 224, 223)
METAL2 = (200, 204, 203)

mid_x = WIDTH // 2
mid_y = HEIGHT//2

def start_window():
    pygame.draw.rect(screen, RED,(mid_x-8, mid_y-50-40, 16, 16))
    pygame.draw.circle(screen, METAL1, (mid_x, mid_y), 72)
    pygame.draw.circle(screen, METAL2, (mid_x, mid_y), 16)
    pygame.draw.circle(screen, BLACK, (mid_x, mid_y), 8)
    pygame.draw.circle(screen, GRAYF, (mid_x + 50, mid_y), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - 50, mid_y), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x , mid_y + 50), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x , mid_y - 50), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + 36, mid_y - 36), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + 36, mid_y + 36), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - 36, mid_y - 36), 20, width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - 36, mid_y + 36), 20, width = 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.image.load("map.jpg").convert()

running = True
while running:
    screen.blit(background_image, [0,0])
    start_window()








    pygame.display.flip()
    for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

pygame.quit()