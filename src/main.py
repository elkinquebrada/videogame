import pygame
import core.input as input

from components.player import Player
from components.sprite import sprites, Sprite
from core.map import TileKind, Map
from core.camera import create_screen
from components.entity import Entity, active_objs
from components.physics import Body
from core.area import Area, area
from data.tile_types import tile_kinds
import pyautogui

pygame.init()

width_test, height_test = pyautogui.size()
# print(f"Screen width: {width}, Screen height: {height}")


# screen = create_screen(1629, 900, "Cuentos de mentes estrelladas")
screen = create_screen(width_test, height_test, "Cuentos de mentes estrelladas")

clear_color = (0, 0, 0)
running = True

area = Area("village.map", tile_kinds)


# Bucle de juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    # Update code
    for a in active_objs:
        a.update()

    # Dibujar el codigo
    screen.fill(clear_color)
    if area and area.map:
        area.map.draw(screen)
    
    # ¡IMPORTANTE! Dibujar todos los sprites ordenados por profundidad
    sorted_sprites = sorted(sprites, key=lambda sprite: sprite.get_draw_order())
    for s in sorted_sprites:
        s.draw(screen)
    
    pygame.display.flip()
    pygame.time.delay(17)

pygame.quit()
