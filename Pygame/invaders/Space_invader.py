# from typing import Any
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class House: 
    age =40
    def __init__(self):
        self.y = 440
        self.x =100
        self.colour = RED
        self.height = 100
        self.width = 200
    #end procedure

    def update(self):
        pass
    #end procedure


    def draw(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.height,self.width])
#end class

class Invader:
    def __init__(self, height,width):
        self.x = random.randint(0,700)
        self.y = random.randint(-30,-12)
        self.colour = WHITE
        self.height = height
        self.width = width
        self.speed = 0
    #end procedure

    def update(self):
        self.y = self.y + self.speed
        if self.y > 500:
            self.y = 0
            self.x = random.randint(0,700)
    #end procedure


    def draw(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.width,self.height])
#end class

class Player:
    
   
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
sprites = []
myHouse1 = House()
myHouse2 = House()
House().age = 50
print(myHouse1.age)
print(myHouse2.age)
sprites.append(myHouse1)

for n in range(50):
    sprites.append(Invader(10,10, 0))
#next n

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    for sprite in sprites:
        sprite.update()
        print(sprite.y)
    #next sprite    

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
  
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
 
    # --- Drawing code should go here
    for sprite in sprites:
        sprite.draw()
    #next sprite

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()