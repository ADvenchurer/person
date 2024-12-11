import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill(white)
pygame.display.update()

class rect():
    def __init__(self,color,dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)    

greenRect = rect(green,(50,20,100,100))
redRect = rect(red,(150,200,150,150))
blueRect = rect(blue,(300,400,200,200))

greenRect.draw()
redRect.draw()
blueRect.draw()

pygame.display.update()
