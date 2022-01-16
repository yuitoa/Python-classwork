import pygame 
import random 
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# -- Initialise PyGame pygame.init()
pygame.init()

# -- Blank Screen
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen
pygame.display.set_caption("My Window") 
# -- Exit game flag set to false 
done = False 
# Create a list of the snow blocks 
snow_group = pygame.sprite.Group()
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()



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


### SRC - You need to fill in the rest of the PyGame loop here...
while not done:
# -- User input and controls 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        #End If 
    #Next event

# - Screen background is BLACK
screen.fill (BLACK)

# -- Draw here
all_sprites_group.draw (screen)

# -- flip display to reveal new position of objects 
pygame.display.flip() 
# - The clock ticks over 
clock.tick(60) 
#End While - End of game loop 
pygame.quit()

