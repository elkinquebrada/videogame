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
from components.dialogue import dialogue_box
from components.jump_trigger import jump_prompt 
import pyautogui

pygame.init()

print("=" * 50)
print("🎮 INICIANDO JUEGO...")
print("=" * 50)


width_test, height_test = pyautogui.size()
print(f"Resolución detectada: {width_test}x{height_test}")
 # screen = create_screen(1629, 900, "Cuentos de mentes estrelladas")
screen = create_screen(width_test, height_test, "Cuentos de mentes estrelladas")
print("✓ Pantalla creada")

clear_color = (0, 0, 0)
running = True

print("Cargando área...")

area = Area("forest.map", tile_kinds, screen)
print("Área cargada")

print("Entrando al bucle principal...")
 # Bucle de juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if dialogue_box.active:
                dialogue_box.handle_input(event)
            else:
                input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            if not dialogue_box.active:
                input.keys_down.remove(event.key)

    # Update code (solo si NO hay diálogo activo)
    if not dialogue_box.active:
        for a in active_objs:
            a.update()
    else:
        dialogue_box.update()        

    # Dibujar el codigo
    screen.fill(clear_color)
    if area and area.map:
        area.map.draw(screen)
    
    # ¡IMPORTANTE! Dibujar todos los sprites ordenados por profundidad
    sorted_sprites = sorted(sprites, key=lambda sprite: sprite.get_draw_order())
    for s in sorted_sprites:
        s.draw(screen)

    # Dibujar prompts de salto
    jump_prompt.draw(screen)
    
    # Dibujar el cuadro de diálogo (siempre encima de todo)
    dialogue_box.draw(screen)
    
    pygame.display.flip()
    pygame.time.delay(17)

pygame.quit()
