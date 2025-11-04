import pygame
from camera import camera

sprites = []
loaded = {}

class Sprite:
    def __init__(self, image, base_scale=1.0, depth_scale=True, anchor_y_ratio=1.0):
        # Load and cache the original image
        if image in loaded:
            self.original_image = loaded[image]
        else:
            self.original_image = pygame.image.load(image)
            loaded[image] = self.original_image

        self.base_scale = base_scale
        self.depth_scale = depth_scale
        self.image = self.original_image
        self.entity = None  # Whether this sprite should scale with depth

        # anchor_y_ratio determina dónde está el "punto de anclaje" verticalmente en el sprite
        # 0.0 = parte superior del sprite
        # 0.5 = centro del sprite
        # 1.0 = parte inferior del sprite (por defecto, donde "toca el suelo")
        self.anchor_y_ratio = anchor_y_ratio
        
        sprites.append(self)

    def get_depth_scale_factor(self):
        """
        Calculate how much to scale based on Y position (depth).
        You'll need to tune these values based on your game's feel.
        
        The idea: objects higher on screen (lower Y) are farther away and smaller.
        Objects lower on screen (higher Y) are closer and bigger.
        """
        if not self.depth_scale or self.entity is None:
            return self.base_scale
        
        # Define your depth range
        # min_y: the farthest point in your scene (smallest scale)
        # max_y: the closest point in your scene (largest scale)
        min_y = 500  # Objects at Y=200 will be at minimum size
        max_y = 1100  # Objects at Y=800 will be at maximum size
        
        # Scale range
        min_scale = 0.9  # Farthest objects are 50% size
        max_scale = 1.5  # Closest objects are 150% size
        
        # Clamp Y to the valid range
        clamped_y = max(min_y, min(max_y, self.entity.y))
        
        # Calculate the scale factor
        # As Y increases (moving down/closer), scale increases
        progress = (clamped_y - min_y) / (max_y - min_y)
        scale_factor = min_scale + (max_scale - min_scale) * progress
        
        return self.base_scale * scale_factor
   
    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        if self.entity is None:
            return
        
        # Calcular la escala actual basada en la profundidad
        current_scale = self.get_depth_scale_factor()
        
        # Escalar la imagen
        new_width = int(self.original_image.get_width() * current_scale)
        new_height = int(self.original_image.get_height() * current_scale)
        scaled_image = pygame.transform.scale(self.original_image, (new_width, new_height))
        
        # ESTO ES CRUCIAL: Calcular la posición de dibujo basándose en el punto de anclaje
        # La posición de la entidad representa el punto de anclaje del sprite
        # Necesitamos ajustar la posición de dibujo para que el punto de anclaje
        # esté en el lugar correcto dentro del sprite
        
        # Centrar horizontalmente: restar la mitad del ancho
        draw_x = self.entity.x - (new_width / 2)
        
        # Verticalmente: ajustar según el anchor_y_ratio
        # Si anchor_y_ratio es 1.0 (por defecto), la entidad.y está en la base del sprite
        # Si anchor_y_ratio es 0.5, la entidad.y está en el centro del sprite
        # Si anchor_y_ratio es 0.0, la entidad.y está en la parte superior del sprite
        draw_y = self.entity.y - (new_height * self.anchor_y_ratio)
        
        # Aplicar el offset de la cámara y dibujar
        screen.blit(scaled_image, (draw_x - camera.x, draw_y - camera.y))
    
    def get_draw_order(self):
        """
        Retorna la posición Y para ordenar por profundidad.
        
        ¡Este es el SECRETO del ordenamiento correcto en juegos 2.5D!
        
        El orden de dibujo debe basarse en dónde el objeto "toca el suelo" en el mundo del juego.
        Dado que ahora la posición de la entidad representa el punto de anclaje del sprite
        (que por defecto está en la base), simplemente devolvemos entity.y.
        
        Esto asegura que los personajes caminen detrás de objetos que están "más atrás"
        incluso si esos objetos son altos.
        """
        if self.entity is None:
            return 0
        
        # La posición Y de la entidad ya representa el punto de anclaje
        # Por defecto (anchor_y_ratio=1.0), esto es la base del objeto
        # Así que podemos usarla directamente para el ordenamiento
        return self.entity.y