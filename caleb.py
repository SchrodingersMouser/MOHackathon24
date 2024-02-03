import pygame
import os
pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    # TODO: Try to make this into an image
    screen.fill("black")  # Fill the display with a solid color

    pygame.draw.circle(screen, "#8a8a8a", (WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2), 500)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)