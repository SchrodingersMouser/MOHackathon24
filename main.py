import math

import pygame
import os

pygame.init()

# Variables used in the window
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000
bg = pygame.image.load("assets/bg.png")

screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

clock = pygame.time.Clock()
global_r = 0
angle = 0
class ship(object):

    velocity_m = 1
    def __init__(self, x, y, asset):
        self.s_location = [x, y]  # ship location
        self.s_velocity = 0  # ship speed (0 - 100)
        self.s_heading = 0  # direction (0 - 360)
        # converting the image makes it run faster (supposedly). image is then resized so it looks alright
        self.base_ship_icon = pygame.transform.scale(pygame.image.load(asset), (50, 50))


    def update_ship_location(self):

        # enforcing velocity
        if self.s_velocity < -10:
            self.s_velocity = -10
        elif self.s_velocity > 30:
            self.s_velocity = 30

        deltax = float(math.cos(self.s_heading+90) * self.s_velocity)
        deltay = -float(math.sin(self.s_heading+90) * self.s_velocity)

        self.s_location[0] += deltax
        self.s_location[1] += deltay

        #if you go off the screen, you show up on the other side
        if self.s_location[0] <= 0:
            self.s_location[0] = WINDOW_WIDTH - 20
        elif self.s_location[0] >= WINDOW_WIDTH:
            self.s_location[0] = 20
        if self.s_location[1] <= 0:
            self.s_location[1] = WINDOW_HEIGHT - 20
        elif self.s_location[1] >= WINDOW_HEIGHT:
            self.s_location[1] = 20

        # this function should modify the ship's location
        # ship orientation should be set based on the ship heading

    # this code is attempting to visibly rotate the sprite
    def draw(self, rotation):
        rotated_ship = pygame.transform.rotate(self.base_ship_icon, rotation)
        new_ship = rotated_ship.get_rect(center = self.s_location) #center = self.base_ship_icon.get_rect().center
        screen.blit(rotated_ship, new_ship)


# in the final game these missiles will fire from the ship on their heading
class missile(object):

    def __init__(self, x, y, asset):
        self.s_location = [x, y]  # ship location
        # converting the image makes it run faster (supposedly). image is then resized so it looks alright
        self.ship_icon = pygame.transform.scale(pygame.image.load("assets/redShot.png").convert(), (30, 30))

class star(object):
    def __init__(self, x, y, asset):
        self.location = [x, y]  # star location
        self.icon = pygame.image.load(asset)  # star icon


ship_g = ship(20, 500, "assets/shipGreen.png")
vel_reducer = 1

star_ = star(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, "assets/star.png")

while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_g.s_heading -= 10
            if event.key == pygame.K_LEFT:
                ship_g.s_heading += 10
            if event.key == pygame.K_UP:
                ship_g.s_velocity -= 1 * ship_g.velocity_m
            if event.key == pygame.K_DOWN:
                ship_g.s_velocity += 1 * ship_g.velocity_m

    # steering with velocity and heading controls are really hard: implemented under here
    # pressed_keys = pygame.key.get_pressed()
    # #
    # rotate = (pressed_keys[pygame.K_LEFT] - pressed_keys[pygame.K_RIGHT]) * 5
    # ship_g.s_velocity += (pressed_keys[pygame.K_UP] - pressed_keys[pygame.K_DOWN]) * vel_reducer
    # ship_g.s_heading += rotate

    #
    ship_g.update_ship_location()
    print(ship_g.s_heading)
    # # TODO: Try to make this into an image
    # screen.fill("black")  # Fill the display with a solid color
    #
    # pygame.draw.circle(screen, "#8a8a8a", (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 500)
    #
    # TODO: Try to make this into an image
    screen.fill("black")  # Fill the display with a solid color

    screen.blit(bg, (0, 0))
    ship_g.draw((ship_g.s_heading))


    screen.blit(star_.icon, star_.location)
    pygame.event.clear()
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(10)  # wait until next frame (at 60 FPS)
