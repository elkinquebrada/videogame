from entity import Entity
from sprite import Sprite
from player import Player
from physics import Body
from teleporter import Teleporter
from animator import Animator

entity_factories = [

#===================================
#--------------TABERNA--------------
#===================================
    # 0 - Jugador
    lambda args:Entity(Player(movement_speed=50), 
    Animator('assets/Character', scale_factor=1.0),
    Sprite("assets/Character/Idle/Front.png", base_scale=0.1, depth_scale=True),
    Body(50,50,16,16)),

    # 1 - Columna
    lambda args:Entity(Sprite("assets/Background/Tavern/tavern_colum.png", base_scale=0.3, depth_scale=True),
    Body(180,200,55,30)),

    # 2 - Barra
    lambda args: Entity(
    Sprite("assets/Background/Tavern/tavern_bar.png", base_scale=0.2, depth_scale=True), 
    Body(-240,-260,550,320)),

    # 3 - Mesa
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_table.png", base_scale=0.13, depth_scale=True),
    Body()),

    # 4 - Piano
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_piano.png", base_scale=0.14, depth_scale=True),
    Body()),

    # 5 - Silla 1
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_chair.png", base_scale=0.1, depth_scale=True),
    Body()),

    # 6 - Iluminación1
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_light1.png", base_scale=0.15, depth_scale=True, draw_order_override=961),
    Body()),

    # 7 - Iluminación2
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_light2.png", base_scale=0.18, depth_scale=True),
    Body()),

    # 8 - Iluminación3
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_light3.png", base_scale=0.35, depth_scale=True, draw_order_override=701),
    Body()),

    # 9 - Iluminación4
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_light4.png", base_scale=0.15, depth_scale=True, draw_order_override=1051),
    Body()),
    # 10 - Radio
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_radio.png", base_scale=0.13, depth_scale=True, draw_order_override=961),
    Body()),

    # 11 - Cerveza
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_beer.png", base_scale=0.1, depth_scale=True, draw_order_override=1051),
    Body()),

    # 12 - Cartel caza sombras
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_poster.png", base_scale=0.08, depth_scale=True, draw_order_override=601),
    Body()),

    # 13 Teletransportación a Villa
    lambda args: Entity(
        Teleporter(
            area_file=args[3],          # 1. Nombre del archivo (ej: 'village.map')
            x=int(args[4]),             # 2. Offset X de la colisión (ej: -20)
            y=int(args[5]),             # 3. Offset Y de la colisión (ej: 15)
            width=int(args[6]),         # 4. Ancho de la colisión (ej: 50)
            height=int(args[7])         # 5. Alto de la colisión (ej: 20)
        ), 
        Sprite("assets/Background/Tavern/tavern_door.png", base_scale=0.2, depth_scale=True)
    ),

#===================================
#--------------VILLA--------------
#===================================

    # 14 - Jugador
    lambda args:Entity(Player(movement_speed=80),
    Animator('assets/Character', scale_factor=1.0), 
    Sprite("assets/Character/Idle/Front.png", base_scale=0.05, depth_scale=True),
    Body(50,50,16,16)),

    # 15 - Taberna
    lambda args: Entity(Sprite("assets/Background/Village/Village_Tavern/village_tavern.png", base_scale=0.32, depth_scale=True),
    Body()),

    # 16 Teletransportación a Taberna
    lambda args: Entity(
        Teleporter(
            area_file=args[3],          # 1. Nombre del archivo (ej: 'village.map')
            x=int(args[4]),             # 2. Offset X de la colisión (ej: -20)
            y=int(args[5]),             # 3. Offset Y de la colisión (ej: 15)
            width=int(args[6]),         # 4. Ancho de la colisión (ej: 50)
            height=int(args[7])         # 5. Alto de la colisión (ej: 20)
        ), 
        Sprite("assets/Background/Village/Village_Tavern/village_tavern_door.png", base_scale=0.12, depth_scale=True)
    ),
    # 17 - Taberna/Escaleras
    lambda args: Entity(Sprite("assets/Background/Village/Village_Tavern/village_tavern_stairs.png", base_scale=0.13, depth_scale=True),
    Body()),

     # 18 - Tienda
    lambda args: Entity(Sprite("assets/Background/Village/Village_Shop/village_shop.png", base_scale=0.5, depth_scale=True),
    Body()),

    # 19 Teletransportación a Tienda
    lambda args: Entity(
        Teleporter(
            area_file=args[3],          # 1. Nombre del archivo (ej: 'village.map')
            x=int(args[4]),             # 2. Offset X de la colisión (ej: -20)
            y=int(args[5]),             # 3. Offset Y de la colisión (ej: 15)
            width=int(args[6]),         # 4. Ancho de la colisión (ej: 50)
            height=int(args[7])         # 5. Alto de la colisión (ej: 20)
        ), 
        Sprite("assets/Background/Village/Village_Shop/village_shop_door.png", base_scale=0.08, depth_scale=True, draw_order_override=581)
    ),

    # 20 - Tienda/Escaleras
    lambda args: Entity(Sprite("assets/Background/Village/Village_Shop/village_shop_stairs.png", base_scale=0.13, depth_scale=True),
    Body()),

    # 21 - Estatua
    lambda args: Entity(Sprite("assets/Background/Village/village_statue.png", base_scale=0.15, depth_scale=True),
    Body()),

    # 22 - Casa del leñador
    lambda args: Entity(Sprite("assets/Background/Village/Lumber_House/lumber_house.png", base_scale=0.43, depth_scale=True),
    Body()),

    # 23 Teletransportación a Casa del Leñador
    lambda args: Entity(
        Teleporter(
            area_file=args[3],          # 1. Nombre del archivo (ej: 'village.map')
            x=int(args[4]),             # 2. Offset X de la colisión (ej: -20)
            y=int(args[5]),             # 3. Offset Y de la colisión (ej: 15)
            width=int(args[6]),         # 4. Ancho de la colisión (ej: 50)
            height=int(args[7])         # 5. Alto de la colisión (ej: 20)
        ), 
        Sprite("assets/Background/Village//Lumber_House/lumber_house_door.png", base_scale=0.07, depth_scale=True, draw_order_override=801)
    ),

]

def create_entity(id,x,y,data=None):
    factory = entity_factories [id]
    e = factory(data)
    e.x = x
    e.y = y
    return e
