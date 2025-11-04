from map import Map
from objects import create_entity
from tile_types import tile_kinds

area = None
area_folder_location = "assets/maps"

class Area:
    def __init__(self, area_file, tile_types):
        global area
        area = self
        self.title_types = tile_types
        self.load_file(area_file)

    def reset_everything(self):
        from physics import triggers,bodies
        from sprite import sprites
        from entity import active_objs
        triggers.clear()
        bodies.clear()
        sprites.clear()
        active_objs.clear()
        self.entities = []
        
    def load_file(self, area_file):
        self.reset_everything()
        
        file = open(area_folder_location + "/" + area_file, "r")
        data =file.read()
        file.close()

        chunks = data.split ('-')
        title_map_data = chunks[0]
        entity_data = chunks[1]

    #Carga el mapa
        self.map = Map(title_map_data, self.title_types)

    #Carga las entidades
        self.entities = []
        entity_lines = entity_data.split ('\n') [1:]
        for line in entity_lines:
            try:
                items = line.split (',')
                id = int(items[0])
                x = int(items[1])
                y = int(items[2])
                self.entities.append(create_entity(id,x,y,items))
            except:
                print(f"Error parsing line:{line}")