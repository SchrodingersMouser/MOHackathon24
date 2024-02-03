import pygame
import os

pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

clock = pygame.time.Clock()
class ship(object):
    def __init__(self, x, y, asset):
        self.s_location = [x, y] # ship location
        self.s_velocity = [-40, 300] # ship speed (0 - 100) and direction (0 - 360)
        # converting the image makes it run faster (supposedly). image is then resized so it looks alright
        self.ship_icon = pygame.transform.scale(pygame.image.load(asset).convert(), (50, 50))



# def update_ship_velocity():
#     #this function should modify the ship's velocity based on user inputs
    def update_ship_location(self):
        self.s_location
        # this function should modify the ship's location
        # ship orientation should be set based on the ship heading

ship_g = ship(50, 200, "assets/shipGreen.png")


while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

#steering with velocity and heading controls are really hard: implemented under here
    # pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[pygame.K_RIGHT]: # this code should make the ship turn
    #     ship_g.s_velocity[1] += 1
    # elif pressed_keys[pygame.K_LEFT]:
    #     ship_g.s_velocity[1] -= 1
    # if pressed_keys[pygame.K_UP]: #this code controls acceleration
    #     ship_g.s_velocity[0] += 1
    # elif pressed_keys[pygame.K_DOWN]:
    #     ship_g.s_velocity[0] -= 1

#steering with straight x and y
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]: # this code should make the ship turn
        ship_g.s_location[1] += 1
    elif pressed_keys[pygame.K_LEFT]:
        ship_g.s_location[1] -= 1
    if pressed_keys[pygame.K_UP]: #this code controls acceleration
        ship_g.s_location[0] += 1
    elif pressed_keys[pygame.K_DOWN]:
        ship_g.s_location[0] -= 1

    #logic updates
    # update_ship_velocity()
    #
    # update_ship_location()

    # TODO: Try to make this into an image
    screen.fill("black")  # Fill the display with a solid color

    pygame.draw.circle(screen, "#8a8a8a", (WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2), 500)
    screen.blit(ship_g.ship_icon, ship_g.s_location)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    
