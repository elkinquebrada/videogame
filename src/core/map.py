import pygame

map = None

map_folder_location = "assets/maps"
image_folder_location = "assets"
tile_size = 500

class TileKind:
    def __init__(self, name, image, is_solid, scale = 1.0,x=0,y=0):
        x= x
        y = y
        self.name = name
        self.is_solid = is_solid
        original_image = pygame.image.load(image)
        if scale != 1.0:
            new_width = int(original_image.get_width() * scale)
            new_height = int(original_image.get_height() * scale)
            self.image = pygame.transform.scale(original_image, (new_width, new_height))
        else:
            self.image = original_image
       

class Map:
    def __init__(self, data, tile_kinds):
        self.tile_kinds = tile_kinds

        #Configuracion 
        self.tiles = []
        for line in data.split("\n"):
            row = []
            for tile_number in line:
                row.append(int(tile_number))
            self.tiles.append(row)
        
        #Tamaño
        self.tile_size = tile_size

       # NUEVO: Calcular límites del mapa basándose en el tamaño de la imagen del background
        if tile_kinds and len(tile_kinds) > 0 and len(self.tiles) > 0 and len(self.tiles[0]) > 0:
            # Obtener el índice del primer tile del mapa (normalmente el background)
            first_tile_index = self.tiles[0][0]
            
            # Validar que el índice existe en tile_kinds
            if first_tile_index < len(tile_kinds):
                # Obtener la imagen del background correcto para ESTE mapa
                background_image = tile_kinds[first_tile_index].image
                self.width = background_image.get_width()
                self.height = background_image.get_height()
                
                # Definir márgenes de colisión (ajusta estos valores según necesites)
                self.margin = -10  # Píxeles de margen desde el borde
                
                # Límites ajustados
                self.min_x = self.margin
                self.max_x = self.width - self.margin
                self.min_y = self.margin
                self.max_y = self.height - self.margin
                
                print(f"Map bounds set: width={self.width}, height={self.height}")
            else:
                # Si el índice no es válido, usar valores por defecto
                self._set_default_bounds()
        else:
            # Valores por defecto si no hay tile_kinds
            self._set_default_bounds()



    def _set_default_bounds(self):
            # Valores por defecto si no hay tile_kinds
            self.width = 1920
            self.height = 1080
            self.margin = 50
            self.min_x = self.margin
            self.max_x = self.width - self.margin
            self.min_y = self.margin
            self.max_y = self.height - self.margin
            print(f"Using default map bounds: width={self.width}, height={self.height}")
    
    def is_position_within_bounds(self, x, y):
        """Verifica si una posición está dentro de los límites del mapa"""
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y 
    
    def draw(self, screen):
        from core.camera import camera
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)
                image = self.tile_kinds[tile].image
                screen.blit(image,location)
