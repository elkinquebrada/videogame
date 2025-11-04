from physics import Trigger
from player import Player

def teleport(area_file):
    from area import area
    area.load_file(area_file)

class Teleporter(Trigger):
    def __init__(self, area_file, x=0, y=0, width=0, height=0):
        super().__init__(lambda: teleport(area_file), x, y, width, height)
