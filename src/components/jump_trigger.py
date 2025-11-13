import pygame
from components.physics import Trigger

class JumpTrigger(Trigger):
    """
    Trigger que permite al jugador saltar un vacío al presionar ESPACIO
    """
    def __init__(self, destination_x, destination_y, x=0, y=0, width=50, height=50, prompt_text="Presiona ESPACIO para saltar"):
        """
        Args:
            destination_x: Posición X de destino después del salto
            destination_y: Posición Y de destino después del salto
            x, y: Offset del trigger
            width, height: Tamaño del trigger
            prompt_text: Texto a mostrar cuando el jugador está en el trigger
        """
        self.destination_x = destination_x
        self.destination_y = destination_y
        self.prompt_text = prompt_text
        self.player_in_trigger = False
        self.is_jumping = False
        
        # No llamamos on() automáticamente, solo detectamos cuando el jugador está aquí
        super().__init__(self.detect_player, x, y, width, height)
    
    def detect_player(self):
        """Marca que el jugador está en el trigger"""
        self.player_in_trigger = True
    
    def check_jump_input(self):
        """
        Verifica si el jugador presionó ESPACIO para saltar
        Returns:
            bool: True si debe ejecutar el salto
        """
        from core.input import is_key_pressed
        
        if self.player_in_trigger and is_key_pressed(pygame.K_SPACE):
            return True
        return False
    
    def execute_jump(self, player_entity):
        """
        Ejecuta el salto del jugador
        
        Args:
            player_entity: La entidad del jugador
        """
        if self.is_jumping:
            return
        
        self.is_jumping = True
        
        # Guardar posición inicial
        start_x = player_entity.x
        start_y = player_entity.y
        
        # Crear animación de salto (movimiento suave)
        import threading
        import time
        
        def animate_jump():
            steps = 20  # Número de pasos de la animación
            for i in range(steps + 1):
                progress = i / steps
                # Interpolación lineal
                player_entity.x = start_x + (self.destination_x - start_x) * progress
                player_entity.y = start_y + (self.destination_y - start_y) * progress
                time.sleep(0.02)  # 20ms entre frames
            
            self.is_jumping = False
        
        # Ejecutar animación en segundo plano (opcional, para no bloquear el juego)
        # Si prefieres instantáneo, comenta estas líneas y descomenta las de abajo
        thread = threading.Thread(target=animate_jump)
        thread.start()
        
        # Alternativa: Salto instantáneo (descomenta si prefieres esto)
        # player_entity.x = self.destination_x
        # player_entity.y = self.destination_y
        # self.is_jumping = False


class JumpPrompt:
    """
    Clase para dibujar el prompt de salto en pantalla
    """
    def __init__(self):
        self.active_prompts = []
        self.font = None
        self.bg_color = (20, 20, 40, 200)
        self.text_color = (255, 255, 100)
        self.border_color = (255, 255, 150)

    def _init_font(self):
        """Inicializa la fuente de forma perezosa"""
        if self.font is None:
            self.font = pygame.font.Font(None, 32)
    
    def add_prompt(self, text, x, y):
        """Agrega un prompt temporal"""
        self.active_prompts.append({
            'text': text,
            'x': x,
            'y': y,
            'alpha': 255
        })
    
    def clear_prompts(self):
        """Limpia todos los prompts"""
        self.active_prompts = []
    
    def draw(self, screen):
        """Dibuja todos los prompts activos"""
        from core.camera import camera
        
        for prompt in self.active_prompts[:]:  # Copiar lista para poder modificar
            # Calcular posición en pantalla
            screen_x = prompt['x'] - camera.x
            screen_y = prompt['y'] - camera.y - 80  # Elevado sobre el trigger
            
            # Renderizar texto
            text_surface = self.font.render(prompt['text'], True, self.text_color)
            text_rect = text_surface.get_rect(center=(screen_x, screen_y))
            
            # Calcular tamaño del fondo
            padding = 15
            bg_width = text_rect.width + padding * 2
            bg_height = text_rect.height + padding * 2
            bg_x = text_rect.x - padding
            bg_y = text_rect.y - padding
            
            # Dibujar fondo semi-transparente
            bg_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
            bg_surface.fill(self.bg_color)
            screen.blit(bg_surface, (bg_x, bg_y))
            
            # Dibujar borde
            pygame.draw.rect(screen, self.border_color, 
                           (bg_x, bg_y, bg_width, bg_height), 3, border_radius=10)
            
            # Dibujar texto
            screen.blit(text_surface, text_rect)
            
            # Animación parpadeante
            pulse = abs(pygame.time.get_ticks() % 1000 - 500) / 500
            prompt['alpha'] = int(200 + 55 * pulse)


# Instancia global del sistema de prompts
jump_prompt = JumpPrompt()