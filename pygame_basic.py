import pygame
from player.player_bullet import PlayerBullet
from player.player import Player
from input.input_manager import InputManager
from enemy.enemy import Enemy
import game_objects
from enemy.enemy_spawner import EnemySpawner
# 1. Init pygame
pygame.init()
#  R - G - B (0-255)
GREEN = (0, 255, 0)
# 2. Set up screen
canvas = pygame.display.set_mode((400, 600))

input_manager = InputManager()
player = Player(200, 500, input_manager)
enemy  =  Enemy (300, 400)
spawner = EnemySpawner()

game_objects.add(player)
game_objects.add(enemy)
game_objects.add(spawner)


clock = pygame.time.Clock()



# 3. Game loop
loop = True
while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_objects.update()

    canvas.fill(GREEN)
    game_objects.render(canvas)


    pygame.display.flip()
    #  60 frame per second
    clock.tick(60)