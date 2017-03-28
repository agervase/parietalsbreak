import pyscroll
from pytmx.util_pygame import load_pygame

# Load TMX data
tmx_data = load_pygame("desert.tmx")

# Make data source for the map
map_data = pyscroll.TiledMapData(tmx_data)

# Make the scrolling layer
screen_size = (400, 400)
map_layer = pyscroll.BufferedRenderer(map_data, screen_size)

# make the PyGame SpriteGroup with a scrolling map
group = pyscroll.PyscrollGroup(map_layer=map_layer)

# Add sprites to the group
group.add(sprite)

# Center the layer and sprites on a sprite
group.center(sprite.rect.center)

# Draw the layer
# If the map covers the entire screen, do not clear the screen:
# Clearing the screen is not needed since the map will clear it when drawn
# This map covers the screen, so no clearing!
group.draw(screen)

# adjust the zoom (out)
map_layer.zoom = .5

# adjust the zoom (in)
map_layer.zoom = 2.0
