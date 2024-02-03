import pygame
import os

pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

clock = pygame.time.Clock()
def ship():
    s_location = (300, 500) # ship location
    s_velocity = (-40, 300) # ship speed (0 - 100) and direction (0 - 360)
    ship_icon = pygame.image.load("images/ship.png").convert() # converting the image makes it run faster (supposedly)
def update_ship_velocity():
    #this function should modify the ship's velocity based on user inputs
def update_ship_location():
    #this function should modify the ship's location
    # ship orientation should be set based on the ship heading


while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    #logic updates
    update_ship_velocity()

    update_ship_location()

    # TODO: Try to make this into an image
    screen.fill("black")  # Fill the display with a solid color

    pygame.draw.circle(screen, "#8a8a8a", (WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2), 500)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    
