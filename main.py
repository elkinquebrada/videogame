import pygame
import input

from player import Player
from sprite import sprites, Sprite
from map import TileKind, Map
from camera import create_screen
from entity import Entity, active_objs
from physics import Body
from area import Area, area
from tile_types import tile_kinds

pygame.init()

screen = create_screen(1629, 900, "Cuentos de mentes estrelladas")

clear_color = (30, 150, 50)
running = True


area = Area("tavern.map", tile_kinds)


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