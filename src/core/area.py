import pygame
import os
from core.map import Map
from data.objects import create_entity
from data.tile_types import tile_kinds

area = None
area_folder_location = "assets/maps"

class Area:
    def __init__(self, area_file, tile_types, screen=None):
        global area
        area = self
        self.title_types = tile_types
        self.load_file(area_file, screen)

    def reset_everything(self):
        from components.physics import triggers,bodies
        from components.sprite import sprites
        from components.entity import active_objs
        triggers.clear()
        bodies.clear()
        sprites.clear()
        active_objs.clear()
        self.entities = []

    def search_for_first(self,kind):
        for e in self.entities:
            c = e.get(kind)
            if c is None:
                return e 
            
    def draw_loading_bar(self, screen, progress, text="Cargando..."):
        """Dibuja una barra de carga estilizada en la pantalla"""
        if screen is None:
            return
            
        # Limpiar pantalla con degradado oscuro
        screen.fill((10, 10, 20))
        
        # Configuración de fuentes
        font_folder_path = "content/fonts"
        custom_font_name = "EBGaramond-VariableFont_wght.ttf"  # Cambia esto por tu fuente si tienes una
        
        # Función auxiliar para cargar fuentes de forma segura
        def load_font_safe(size):
            # Intentar cargar fuente personalizada
            if os.path.exists(font_folder_path):
                font_path = os.path.join(font_folder_path, custom_font_name)
                if os.path.exists(font_path):
                    try:
                        return pygame.font.Font(font_path, size)
                    except:
                        pass
            # Si falla, usar fuente predeterminada
            return pygame.font.Font(None, size)
        
        # Dimensiones
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        bar_width = 500
        bar_height = 40
        bar_x = (screen_width - bar_width) // 2
        bar_y = (screen_height - bar_height) // 2
        
        # Título del juego
        try:
            title_font = load_font_safe(64)
            title_surface = title_font.render("Cuentos de Mentes Estrelladas", True, (220, 200, 255))
            title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 3))
            
            # Sombra del título
            shadow_surface = title_font.render("Cuentos de Mentes Estrelladas", True, (50, 40, 80))
            shadow_rect = shadow_surface.get_rect(center=(screen_width // 2 + 3, screen_height // 3 + 3))
            screen.blit(shadow_surface, shadow_rect)
            screen.blit(title_surface, title_rect)
        except:
            pass
        
        # Sombra de la barra (efecto de profundidad)
        shadow_offset = 6
        pygame.draw.rect(screen, (0, 0, 0, 128), 
                        (bar_x + shadow_offset, bar_y + shadow_offset, bar_width, bar_height), 
                        border_radius=20)
        
        # Fondo de la barra (más oscuro)
        pygame.draw.rect(screen, (30, 30, 50), 
                        (bar_x, bar_y, bar_width, bar_height), 
                        border_radius=20)
        
        # Borde exterior brillante
        pygame.draw.rect(screen, (100, 80, 150), 
                        (bar_x - 3, bar_y - 3, bar_width + 6, bar_height + 6), 
                        3, border_radius=20)
        
        # Progreso con degradado
        if progress > 0:
            progress_width = int((bar_width - 8) * progress)
            
            # Color del progreso (verde a azul según progreso)
            r = int(50 + (100 * (1 - progress)))
            g = int(200 - (50 * progress))
            b = int(100 + (155 * progress))
            
            # Barra de progreso con esquinas redondeadas
            pygame.draw.rect(screen, (r, g, b), 
                            (bar_x + 4, bar_y + 4, progress_width, bar_height - 8), 
                            border_radius=17)
            
            # Brillo en la parte superior de la barra
            highlight_height = (bar_height - 8) // 3
            pygame.draw.rect(screen, (min(r + 50, 255), min(g + 50, 255), min(b + 50, 255), 128), 
                            (bar_x + 4, bar_y + 4, progress_width, highlight_height), 
                            border_radius=17)
        
        # Texto de carga
        try:
            font = load_font_safe(32)
            percent_font = load_font_safe(36)
            
            text_surface = font.render(text, True, (200, 200, 220))
            text_rect = text_surface.get_rect(center=(screen_width // 2, bar_y - 50))
            
            # Sombra del texto
            shadow_text = font.render(text, True, (30, 30, 40))
            shadow_rect = shadow_text.get_rect(center=(screen_width // 2 + 2, bar_y - 48))
            screen.blit(shadow_text, shadow_rect)
            screen.blit(text_surface, text_rect)
            
            # Porcentaje dentro de la barra
            percent_text = f"{int(progress * 100)}%"
            percent_surface = percent_font.render(percent_text, True, (255, 255, 255))
            percent_rect = percent_surface.get_rect(center=(screen_width // 2, bar_y + bar_height // 2))
            
            # Sombra del porcentaje
            percent_shadow = percent_font.render(percent_text, True, (0, 0, 0))
            percent_shadow_rect = percent_shadow.get_rect(center=(screen_width // 2 + 1, bar_y + bar_height // 2 + 1))
            screen.blit(percent_shadow, percent_shadow_rect)
            screen.blit(percent_surface, percent_rect)
            
            # Animación de puntos suspensivos
            dots = "." * (int(progress * 10) % 4)
            loading_hint = font.render(f"Por favor espere{dots}", True, (150, 150, 170))
            loading_rect = loading_hint.get_rect(center=(screen_width // 2, bar_y + bar_height + 50))
            screen.blit(loading_hint, loading_rect)
            
        except Exception as e:
            print(f"Error rendering text: {e}")
         # Partículas decorativas (estrellas)
        import random
        random.seed(int(progress * 100))  # Seed para consistencia
        for _ in range(int(progress * 20)):
            star_x = random.randint(0, screen_width)
            star_y = random.randint(0, screen_height)
            star_size = random.randint(1, 3)
            brightness = random.randint(150, 255)
            pygame.draw.circle(screen, (brightness, brightness, brightness), (star_x, star_y), star_size)
        
        pygame.display.flip()
        
             
        
    def load_file(self, area_file, screen=None):
        self.reset_everything()

        # Limpiar el estado de las teclas antes de cargar
        from core import input as game_input
        game_input.keys_down.clear()
        
        # Progreso 0%: Inicio de carga
        self.draw_loading_bar(screen, 0.0, "Iniciando carga del mundo")
        
        # Progreso 10%: Leer archivo
        self.draw_loading_bar(screen, 0.05, "Abriendo portal dimensional")
        file = open(area_folder_location + "/" + area_file, "r")
        data = file.read()
        file.close()
        self.draw_loading_bar(screen, 0.15, "Datos del mundo recuperados")
        
        chunks = data.split('-')
        title_map_data = chunks[0]
        entity_data = chunks[1]
        
        # Progreso 30%: Cargar mapa
        self.draw_loading_bar(screen, 0.25, "Tejiendo el paisaje")
        self.draw_loading_bar(screen, 0.35, "Pintando el terreno")
        self.map = Map(title_map_data, self.title_types)
        self.draw_loading_bar(screen, 0.50, "Mundo materializado")
        
        # Progreso 50-100%: Cargar entidades
        self.entities = []
        entity_lines = entity_data.split('\n')[1:]
        total_entities = len([line for line in entity_lines if line.strip()])
        
        for i, line in enumerate(entity_lines):
            try:
                items = line.split(',')
                if len(items) < 3:
                    continue
                    
                id = int(items[0])
                x = int(items[1])
                y = int(items[2])
                self.entities.append(create_entity(id, x, y, items))
                
                # Actualizar progreso (de 0.5 a 1.0)
                progress = 0.5 + (0.5 * (i + 1) / max(total_entities, 1))
                
                # Mensajes más descriptivos según el progreso
                if progress < 0.7:
                    message = "Invocando criaturas"
                elif progress < 0.9:
                    message = "Colocando objetos mágicos"
                else:
                    message = "Últimos toques de magia"

                if i % 5 == 0 or i == total_entities - 1:    
                    self.draw_loading_bar(screen, progress, f"{message} ({i+1}/{total_entities})")
                
            except Exception as e:
                print(f"Error parsing line: {line} - {e}")
        
        # Progreso 100%: Completado
        self.draw_loading_bar(screen, 1.0, "¡El mundo está listo!")
        pygame.time.delay(300)
        
        
        game_input.keys_down.clear()

        print("✓ Carga completada exitosamente!")
        print(f"✓ Entidades cargadas: {len(self.entities)}")
        print(f"✓ Mapa cargado: {self.map.width}x{self.map.height}") 