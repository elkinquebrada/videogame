import pygame
import os

from components.sprite import Sprite
from core.input import is_key_pressed
from core.camera import camera
from components.entity import active_objs
from components.physics import Body, triggers
from components.jump_trigger import jump_prompt 

class Player:
    def __init__(self, movement_speed=50):
        active_objs.append(self)
        self.entity = None
        self.movement_speed = movement_speed

    def update(self):
        from components.animator import Animator
        from core.area import area
        from components.jump_trigger import JumpTrigger, jump_prompt

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

        # Limpiar prompts anteriores
        jump_prompt.clear_prompts()

        # Verificar triggers (puertas y saltos)
        for t in triggers:
            if body.is_colliding_with(t):
                # Si es un JumpTrigger
                if isinstance(t, JumpTrigger):
                    t.player_in_trigger = True
                    
                    # Mostrar prompt
                    jump_prompt.add_prompt(t.prompt_text, self.entity.x, self.entity.y)
                    
                    # Verificar si el jugador presionó ESPACIO
                    if t.check_jump_input() and not t.is_jumping:
                        t.execute_jump(self.entity)
                        return  # No procesar movimiento durante el salto
                else:
                    # Otros triggers (como teleportadores)
                    t.on()
            else:
                # Si es un JumpTrigger, marcar que el jugador salió
                if isinstance(t, JumpTrigger):
                    t.player_in_trigger = False

        # Detectar movimiento y dirección
        is_moving = False
        direction = None

        # Usar actual_speed en lugar de self.movement_speed
        if is_key_pressed(pygame.K_UP) or is_key_pressed(pygame.K_w):
            self.entity.y -= actual_speed  
            is_moving = True
            direction = 'back'
        if is_key_pressed(pygame.K_DOWN) or is_key_pressed(pygame.K_s):
            self.entity.y += actual_speed 
            is_moving = True
            direction = 'front'
        if not body.is_position_valid()  or not self._is_within_map_bounds():
            self.entity.y = previous_y
            is_moving = False

        if not body.is_position_valid() or not self._is_within_map_bounds():
            self.entity.y = previous_y
            is_moving = False   
      

        if is_key_pressed(pygame.K_RIGHT) or is_key_pressed(pygame.K_d):
            self.entity.x += actual_speed  
            is_moving = True
            direction = 'right'
        if is_key_pressed(pygame.K_LEFT) or is_key_pressed(pygame.K_a):
            self.entity.x -= actual_speed  # <-- Cambiado aquí
            is_moving = True
            direction = 'left'
        if not body.is_position_valid() or not self._is_within_map_bounds():
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

        self._clamp_camera_to_map()

        # Verificar si el jugador está tocando algún trigger (como puertas o teleportadores)
        for t in triggers:
            if body.is_colliding_with(t):
                t.on()

    def _is_within_map_bounds(self):
        """NUEVO: Verifica si el jugador está dentro de los límites del mapa"""
        from core.area import area
        
        if area and area.map:
            return area.map.is_position_within_bounds(self.entity.x, self.entity.y)
        
        return True 
    
    def _clamp_camera_to_map(self):
        """NUEVO: Limita la cámara para que no salga de los límites del mapa"""
        from core.area import area
        
        if not area or not area.map:
            return
        
        map_width = area.map.width
        map_height = area.map.height
        
        # Limitar la cámara para que no muestre áreas fuera del mapa
        # Si el mapa es más pequeño que la pantalla, centrar el mapa
        if map_width <= camera.width:
            camera.x = (map_width - camera.width) / 2
        else:
            # Limitar la cámara a los bordes del mapa
            if camera.x < 0:
                camera.x = 0
            elif camera.x + camera.width > map_width:
                camera.x = map_width - camera.width
        
        if map_height <= camera.height:
            camera.y = (map_height - camera.height) / 2
        else:
            if camera.y < 0:
                camera.y = 0
            elif camera.y + camera.height > map_height:
                camera.y = map_height - camera.height