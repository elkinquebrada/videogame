import pygame
import pyautogui
pygame.init()

engine = None

class Engine:
    def __init__(self, game_title):
        global engine
        engine = self

        self.active_objs = []

        self.background_drawables = []
        self.drawables = []
        self.ui_drawables = []

        from core.camera import create_screen
        self.clear_color = (0, 0, 0)
        
        # CORREGIDO: Usar el tamaño de pantalla automático
        width, height = pyautogui.size()
        self.screen = create_screen(width, height, game_title)
        
        self.stages = {}
        self.current_stage = None

    def register(self, stage_name, func):
        self.stages[stage_name] = func

    def swith_to(self, stage_name):
        self.reset()
        self.current_stage = stage_name
        func = self.stages[stage_name]
        print(f"Switching to {self.current_stage}")
        func()
    
    def run(self):
        from core.input import keys_down

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    keys_down.add(event.key)
                elif event.type == pygame.KEYUP:
                    keys_down.remove(event.key)

            # Update code
            for a in self.active_objs:
                a.update()

            # CORREGIDO: Limpiar la pantalla antes de dibujar
            self.screen.fill(self.clear_color)

            # Dibujar backgrounds (mapas)
            for b in self.background_drawables:
                b.draw(self.screen)

            # CORREGIDO: Ordenar sprites por profundidad antes de dibujar
            sorted_drawables = sorted(self.drawables, key=lambda sprite: sprite.get_draw_order())
            for s in sorted_drawables:
                s.draw(self.screen)

            # Dibujar UI (labels, etc)
            for l in self.ui_drawables:
                l.draw(self.screen)

            pygame.display.flip()
            pygame.time.delay(17)

        pygame.quit()

    def reset(self):
        from components.physics import reset_physics
        reset_physics()
        self.active_objs.clear()
        self.drawables.clear()
        self.ui_drawables.clear()
        self.background_drawables.clear()