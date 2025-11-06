import pygame
import os

from sprite import Sprite
from input import is_key_pressed
from camera import camera
from entity import active_objs
from physics import Body, triggers

class Player:
    def __init__(self, movement_speed=50):
        active_objs.append(self)
        self.entity = None
        self.movement_speed = movement_speed

    def update(self):
        from animator import Animator

        previous_x = self.entity.x
        previous_y = self.entity.y
        body = self.entity.get(Body)
        animator = self.entity.get(Animator)

        if self.entity is None:
            return  
        
        sprite = self.entity.get(Sprite)
        if sprite:
            current_scale = sprite.get_depth_scale_factor()
            actual_speed = self.movement_speed * current_scale
        else:
            actual_speed = self.movement_speed

        # Detectar movimiento y dirección
        is_moving = False
        direction = None

        # Usar actual_speed en lugar de self.movement_speed
        if is_key_pressed(pygame.K_UP) or is_key_pressed(pygame.K_w):
            self.entity.y -= actual_speed  # <-- Cambiado aquí
            is_moving = True
            direction = 'back'
        if is_key_pressed(pygame.K_DOWN) or is_key_pressed(pygame.K_s):
            self.entity.y += actual_speed  # <-- Cambiado aquí
            is_moving = True
            direction = 'front'
        if not body.is_position_valid():
            self.entity.y = previous_y
            is_moving = False

        if is_key_pressed(pygame.K_RIGHT) or is_key_pressed(pygame.K_d):
            self.entity.x += actual_speed  # <-- Cambiado aquí
            is_moving = True
            direction = 'right'
        if is_key_pressed(pygame.K_LEFT) or is_key_pressed(pygame.K_a):
            self.entity.x -= actual_speed  # <-- Cambiado aquí
            is_moving = True
            direction = 'left'
        if not body.is_position_valid():
            self.entity.x = previous_x
            is_moving = False
        # Actualizar la cámara para seguir al jugador
        if animator:
            animator.set_movement_state(is_moving, direction)
            animator.update()

        if sprite:
            # Obtener las dimensiones del sprite escalado
            current_scale = sprite.get_depth_scale_factor()
             # Si hay animator, usar el frame actual para calcular dimensiones
            if animator:
                current_frame = animator.get_current_frame()
                scaled_width = int(current_frame.get_width() * current_scale)
                scaled_height = int(current_frame.get_height() * current_scale)
            else:
                scaled_width = int(sprite.original_image.get_width() * current_scale)
                scaled_height = int(sprite.original_image.get_height() * current_scale)
                
            # Ahora que entity.y representa los pies del personaje (anchor_y_ratio=1.0),
            # necesitamos calcular dónde está el centro visual del sprite para centrar la cámara ahí
            
            # El centro visual del personaje está a media altura del sprite por encima de sus pies
            visual_center_y = self.entity.y - (scaled_height / 2)
            
            # Centrar la cámara en el centro visual del personaje
            camera.x = self.entity.x - camera.width / 2
            camera.y = visual_center_y - camera.height / 2
        else:
            # Si no hay sprite, simplemente centrar en la posición de la entidad
            camera.x = self.entity.x - camera.width / 2
            camera.y = self.entity.y - camera.height / 2

        # Verificar si el jugador está tocando algún trigger (como puertas o teleportadores)
        for t in triggers:
            if body.is_colliding_with(t):
                t.on()

        
