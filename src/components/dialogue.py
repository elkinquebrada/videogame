import pygame
import os

class DialogueBox:
    """Sistema de diálogos para el juego"""
    
    def __init__(self):
        self.active = False
        self.messages = []
        self.current_message_index = 0
        self.character_index = 0
        self.text_speed = 2  # Caracteres por frame
        self.font_size = 28
        self.padding = 30
        self.line_spacing = 10
        
        # Cargar fuente
        self.font = None
        self.name_font = None
        
        # Colores
        self.bg_color = (20, 20, 40, 230)  # Fondo semi-transparente
        self.border_color = (150, 130, 200)
        self.text_color = (255, 255, 255)
        self.name_color = (255, 220, 100)
        
        # Animación
        self.animation_timer = 0
        self.skip_animation = False
        
    def load_font(self):
        """Carga la fuente para el diálogo"""
        font_folder_path = "content/fonts"
        
        # CAMBIA ESTE NOMBRE POR TU ARCHIVO DE FUENTE
        # Ejemplos: "PixelFont.ttf", "MedievalSharp.ttf", "PressStart2P.ttf"
        custom_font_name = "EBGaramond-VariableFont_wght.ttf"
        
        if os.path.exists(font_folder_path):
            font_path = os.path.join(font_folder_path, custom_font_name)
            if os.path.exists(font_path):
                try:
                    self.font = pygame.font.Font(font_path, self.font_size)
                    self.name_font = pygame.font.Font(font_path, self.font_size + 4)
                    print(f"✓ Fuente personalizada cargada: {custom_font_name}")
                    return
                except Exception as e:
                    print(f"✗ Error al cargar fuente: {e}")
            else:
                print(f"✗ Archivo de fuente no encontrado: {font_path}")
        else:
            print(f"✗ Carpeta de fuentes no encontrada: {font_folder_path}")
        
        # Fuente predeterminada
        print("Usando fuente predeterminada de Pygame")
        self.font = pygame.font.Font(None, self.font_size)
        self.name_font = pygame.font.Font(None, self.font_size + 4)
    
    def start_dialogue(self, messages):
        """
        Inicia un diálogo con una lista de mensajes
        
        Args:
            messages: Lista de tuplas (nombre_personaje, texto)
                     Ejemplo: [("Guardián", "¡Bienvenido aventurero!"), 
                              (None, "El bosque es peligroso...")]
        """
        self.messages = messages
        self.current_message_index = 0
        self.character_index = 0
        self.active = True
        self.skip_animation = False
    
    def update(self):
        """Actualiza la animación del texto"""
        if not self.active or not self.messages:
            return
        
        current_message = self.messages[self.current_message_index]
        full_text = current_message[1]
        
        # Animar texto carácter por carácter
        if self.character_index < len(full_text) and not self.skip_animation:
            self.animation_timer += 1
            if self.animation_timer >= self.text_speed:
                self.character_index += 1
                self.animation_timer = 0
    
    def handle_input(self, event):
        """
        Maneja la entrada del jugador
        
        Args:
            event: Evento de pygame
        
        Returns:
            bool: True si el diálogo sigue activo, False si terminó
        """
        if not self.active:
            return False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_e:
                current_message = self.messages[self.current_message_index]
                full_text = current_message[1]
                
                # Si el texto aún se está animando, completarlo
                if self.character_index < len(full_text):
                    self.character_index = len(full_text)
                    self.skip_animation = True
                else:
                    # Avanzar al siguiente mensaje
                    self.current_message_index += 1
                    self.character_index = 0
                    self.skip_animation = False
                    
                    # Si no hay más mensajes, cerrar el diálogo
                    if self.current_message_index >= len(self.messages):
                        self.close()
                        return False
        
        return True
    
    def close(self):
        """Cierra el diálogo"""
        self.active = False
        self.messages = []
        self.current_message_index = 0
        self.character_index = 0
    
    def draw(self, screen):
        """Dibuja el cuadro de diálogo en la pantalla"""
        if not self.active or not self.messages:
            return
        
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Dimensiones del cuadro de diálogo
        box_width = screen_width - 200
        box_height = 180
        box_x = (screen_width - box_width) // 2
        box_y = screen_height - box_height - 50
        
        # Obtener mensaje actual
        current_message = self.messages[self.current_message_index]
        character_name = current_message[0]
        full_text = current_message[1]
        
        # Texto visible (animado)
        visible_text = full_text[:self.character_index]
        
        # Dibujar sombra del cuadro
        shadow_offset = 8
        shadow_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        shadow_surface.fill((0, 0, 0, 100))
        screen.blit(shadow_surface, (box_x + shadow_offset, box_y + shadow_offset))
        
        # Dibujar fondo del cuadro
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        box_surface.fill(self.bg_color)
        screen.blit(box_surface, (box_x, box_y))
        
        # Dibujar borde
        pygame.draw.rect(screen, self.border_color, 
                        (box_x, box_y, box_width, box_height), 4, border_radius=15)
        
        # Dibujar borde interior decorativo
        pygame.draw.rect(screen, (self.border_color[0]//2, self.border_color[1]//2, self.border_color[2]//2), 
                        (box_x + 8, box_y + 8, box_width - 16, box_height - 16), 2, border_radius=12)
        
        # Dibujar nombre del personaje (si existe)
        current_y = box_y + self.padding
        if character_name:
            name_surface = self.name_font.render(character_name, True, self.name_color)
            screen.blit(name_surface, (box_x + self.padding, current_y))
            current_y += name_surface.get_height() + self.line_spacing + 5
            
            # Línea separadora
            line_x1 = box_x + self.padding
            line_x2 = box_x + box_width - self.padding
            pygame.draw.line(screen, self.border_color, 
                           (line_x1, current_y - 3), (line_x2, current_y - 3), 2)
        
        # Dividir texto en líneas para que quepa en el cuadro
        words = visible_text.split(' ')
        lines = []
        current_line = ""
        max_width = box_width - (self.padding * 2)
        
        for word in words:
            test_line = current_line + word + " "
            test_surface = self.font.render(test_line, True, self.text_color)
            
            if test_surface.get_width() <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word + " "
        
        if current_line:
            lines.append(current_line)
        
        # Dibujar líneas de texto
        for line in lines:
            text_surface = self.font.render(line, True, self.text_color)
            screen.blit(text_surface, (box_x + self.padding, current_y))
            current_y += text_surface.get_height() + self.line_spacing
        
        # Indicador de "presiona para continuar" (si el texto está completo)
        if self.character_index >= len(full_text):
            indicator_text = "[ESPACIO] Continuar"
            if self.current_message_index >= len(self.messages) - 1:
                indicator_text = "[ESPACIO] Cerrar"
            
            # Animación parpadeante
            alpha = int(127 + 127 * abs(pygame.time.get_ticks() % 1000 - 500) / 500)
            indicator_surface = self.font.render(indicator_text, True, (*self.text_color, alpha))
            indicator_rect = indicator_surface.get_rect(
                bottomright=(box_x + box_width - self.padding, box_y + box_height - self.padding)
            )
            screen.blit(indicator_surface, indicator_rect)
        
        # Indicador de progreso (cuántos mensajes quedan)
        if len(self.messages) > 1:
            progress_text = f"{self.current_message_index + 1}/{len(self.messages)}"
            progress_surface = self.font.render(progress_text, True, (180, 180, 180))
            progress_rect = progress_surface.get_rect(
                bottomleft=(box_x + self.padding, box_y + box_height - self.padding)
            )
            screen.blit(progress_surface, progress_rect)


# Instancia global del sistema de diálogos
dialogue_box = DialogueBox()