## -- Define the class snow which is a sprite 
class Snow(pygame.sprite.Sprite): 
# Define the constructor for snow 
  def __init__(self, color, width, height): 
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
