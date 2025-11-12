from components.entity import Entity
from components.sprite import Sprite
from components.player import Player
from components.physics import Body
from components.teleporter import Teleporter
from components.animator import Animator

entity_factories = [

#===================================
#--------------TABERNA--------------
#===================================
    # 0 - Jugador
    lambda args:Entity(Player(movement_speed=200), 
    Animator('assets/Character', scale_factor=1.0),
    Sprite("assets/Character/Idle/Front.png", base_scale=0.1, depth_scale=True),
    Body(50,50,16,16)),

    # 1 - Columna
    lambda args:Entity(Sprite("assets/Background/Tavern/tavern_colum.png", base_scale=0.3, depth_scale=True),
    Body(30,40,60,20)),

    # 2 - Barra
    lambda args: Entity(
    Sprite("assets/Background/Tavern/tavern_bar.png", base_scale=0.2, depth_scale=True), 
    Body(-240,-260,550,320)),

    # 3 - Mesa
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_table.png", base_scale=0.13, depth_scale=True),
    Body(-120,0,365,100)),

    # 4 - Piano
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_piano.png", base_scale=0.14, depth_scale=True),
    Body(-80,0,282,100)),

    # 5 - Silla 1
    lambda args: Entity(Sprite("assets/Background/Tavern/tavern_chair.png", base_scale=0.1, depth_scale=True),
    Body(40,0,30,60)),

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
    
    # 14 - Paredes de colisión genéricas
    lambda args: Entity(
        Body(
            int(args[3]) if len(args) > 3 else 0,    # offset x
            int(args[4]) if len(args) > 4 else 0,    # offset y
            int(args[5]) if len(args) > 5 else 50,   # width (default: 50)
            int(args[6]) if len(args) > 6 else 50    # height (default: 50)
        )
    ),

#===================================
#--------------VILLA--------------
#===================================

    # 15 - Jugador
    lambda args:Entity(Player(movement_speed=200),
    Animator('assets/Character', scale_factor=1.0), 
    Sprite("assets/Character/Idle/Front.png", base_scale=0.05, depth_scale=True),
    Body(50,50,16,16)),

    # 16 - Taberna
    lambda args: Entity(Sprite("assets/Background/Village/Village_Tavern/village_tavern.png", base_scale=0.32, depth_scale=True),
    Body()),

    # 17 Teletransportación a Taberna
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
    # 18 - Taberna/Escaleras
    lambda args: Entity(Sprite("assets/Background/Village/Village_Tavern/village_tavern_stairs.png", base_scale=0.13, depth_scale=True),
    Body()),

     # 19 - Tienda
    lambda args: Entity(Sprite("assets/Background/Village/Village_Shop/village_shop.png", base_scale=0.5, depth_scale=True),
    Body()),

    # 20 Teletransportación a Tienda
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

    # 21 - Tienda/Escaleras
    lambda args: Entity(Sprite("assets/Background/Village/Village_Shop/village_shop_stairs.png", base_scale=0.13, depth_scale=True),
    Body()),

    # 22 - Estatua
    lambda args: Entity(Sprite("assets/Background/Village/village_statue.png", base_scale=0.15, depth_scale=True),
    Body()),

    # 23 - Casa del leñador
    lambda args: Entity(Sprite("assets/Background/Village/Lumber_House/lumber_house.png", base_scale=0.43, depth_scale=True),
    Body()),

    # 24 Teletransportación a Casa del Leñador
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
     # 25 Teletransportación a el bosque
    lambda args: Entity(
        Teleporter(
            area_file=args[3],          # 1. Nombre del archivo (ej: 'village.map')
            x=int(args[4]),             # 2. Offset X de la colisión (ej: -20)
            y=int(args[5]),             # 3. Offset Y de la colisión (ej: 15)
            width=int(args[6]),         # 4. Ancho de la colisión (ej: 50)
            height=int(args[7])         # 5. Alto de la colisión (ej: 20)
        ), 
        Sprite("assets/Background/Village///forest_gate_door.png", base_scale=0.15, depth_scale=True, draw_order_override=0)
    ),

    #===================================
    #--------------FOREST--------------
    #===================================
    # 26 - Árbol
    lambda args: Entity(Sprite("assets/Background/Forest/forest_tree.png", base_scale=0.2, depth_scale=True),
    Body()),
    # 27 - Piedra
    lambda args: Entity(Sprite("assets/Background/Forest/forest_rock.png", base_scale=0.1, depth_scale=True),
    Body()),
    # 28 - Tocón
    lambda args: Entity(Sprite("assets/Background/Forest/forest_stump.png", base_scale=0.1, depth_scale=True),
    Body()),
    # 29 - Arbusto
    lambda args: Entity(Sprite("assets/Background/Forest/forest_bush.png", base_scale=0.1, depth_scale=True),
    Body()),
    # 30 - Flor
    lambda args: Entity(Sprite("assets/Background/Forest/forest_flower.png", base_scale=0.05, depth_scale=True),
    Body()),
    # 31 -mountain rock
    lambda args: Entity(Sprite("assets/Background/Forest/mountain_rock.png", base_scale=0.2, depth_scale=True),
    Body()),

    # 32 Teletransportación a la villa
    lambda args: Entity(
        Teleporter(
            area_file=args[3],          # 1. Nombre del archivo (ej: 'village.map')
            x=int(args[4]),             # 2. Offset X de la colisión (ej: -20)
            y=int(args[5]),             # 3. Offset Y de la colisión (ej: 15)
            width=int(args[6]),         # 4. Ancho de la colisión (ej: 50)
            height=int(args[7])         # 5. Alto de la colisión (ej: 20)
        ), 
        Sprite("assets/Background/Forest///Village_gate_door.png", base_scale=0.07, depth_scale=True, draw_order_override=801)
    ),


]

def create_entity(id,x,y,data=None):
    factory = entity_factories [id]
    e = factory(data)
    e.x = x
    e.y = y
    return e
