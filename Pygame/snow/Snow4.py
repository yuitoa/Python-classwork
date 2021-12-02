import pygame 
import random 
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

## -- Define the class snow which is a sprite
class Snow(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__  (self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, 600) 
        self.rect.y = random.randrange(0, 400)
    #End Procedure
#End Class

def draw(self):
    pygame.draw.rect(screen,self.color,[self.rect.x,self.rect.y,self.width,self.height])
#end class

# Create a list of the snow blocks
snow_group = pygame.sprite.Group()

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

# Create the snowflakes
number_of_flakes = 50 # we are creating 50 snowflakes
for x in range (number_of_flakes):
    my_snow = Snow(WHITE, 5, 5)  # snowflakes are white with size 5 by 5 px 
    snow_group.add (my_snow) # adds the new snowflake to the group of snowflakes 
    all_sprites_group.add (my_snow) # adds it to the group of all Sprites
#Next x

# - Screen background is BLACK
screen.fill (BLACK)
# -- Draw here
all_sprites_group.draw (screen)
