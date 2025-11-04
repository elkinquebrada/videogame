import pygame

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
        previous_x = self.entity.x
        previous_y = self.entity.y
        body = self.entity.get(Body)

        if self.entity is None:
            return  
        
        sprite = self.entity.get(Sprite)
        if sprite:
            current_scale = sprite.get_depth_scale_factor()
            actual_speed = self.movement_speed * current_scale
        else:
            actual_speed = self.movement_speed

        # Usar actual_speed en lugar de self.movement_speed
        if is_key_pressed(pygame.K_UP) or is_key_pressed(pygame.K_w):
            self.entity.y -= actual_speed  # <-- Cambiado aquí
        if is_key_pressed(pygame.K_DOWN) or is_key_pressed(pygame.K_s):
            self.entity.y += actual_speed  # <-- Cambiado aquí

        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_RIGHT) or is_key_pressed(pygame.K_d):
            self.entity.x += actual_speed  # <-- Cambiado aquí
        if is_key_pressed(pygame.K_LEFT) or is_key_pressed(pygame.K_a):
            self.entity.x -= actual_speed  # <-- Cambiado aquí

        if not body.is_position_valid():
            self.entity.x = previous_x

        # Actualizar la cámara para seguir al jugador
        if sprite:
            # Obtener las dimensiones del sprite escalado
            current_scale = sprite.get_depth_scale_factor()
            scaled_width = int(sprite.original_image.get_width() * current_scale)
            scaled_height = int(sprite.original_image.get_height() * current_scale)
            
            # AQUÍ ESTÁ EL CAMBIO CRUCIAL:
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