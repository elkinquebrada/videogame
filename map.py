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
    
    def draw(self, screen):
        from camera import camera
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size - camera.x, y * self.tile_size - camera.y)
                image = self.tile_kinds[tile].image
                screen.blit(image,location)