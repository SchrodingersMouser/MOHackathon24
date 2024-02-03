# Welcome to our project for the Missouri Hackathon 2024

NOTE: This project is far from finished, replace most "has"s with "is supposed to have"

This game, designed using pygame, is a 2-player spaceship game with the intent to shoot the other player's ship down. This game also takes inspiration from the early videogame "Spacewar!"

## Controls
One player controls their ship through WASD and uses E to shoot. The second player uses IJKL and uses O to shoot. The forward key (W or I) for both spaceships will apply some velocity to the ship while the backward key (S or K) will propel the ship backwards, but not as fast as going forward. The left keys (A or J) will make the ship rotate to the left, while the right keys (D or L) rotate the ship to the right. The shoot key (E or O) will fire a bullet everytime the key is pressed (There is a delay).

## How it works
Both players start on opposite ends of the map with a star in the center. This star has gravity, which will draw both players and their bullets into it. If a player touches the star or the opponent's ship, then the player's ship blows up and loses. Bullets will also be drawn into the star as well, disabling and destroying them.

## The Goal
The goal of this game is to destroy your opponent's ship while dodging your opponent's bullets and ship while avoiding the star in the center. After a player dies, the game resets.

Have fun with this take on this classic space game!