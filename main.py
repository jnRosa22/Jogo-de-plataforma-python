import pygame
import level
import setings

pygame.init()

size=(setings.screen_width,setings.screen_height)


display=pygame.display.set_mode(size)
pygame.display.set_caption('pataforma')

fase=setings.Level(display,level.level_1)
fase.Add()




#loop pra rodar o game
fps=pygame.time.Clock()     
while True:
    fps.tick(64)
    display.fill('black')
    setings.Event()
    fase.Run()





    pygame.display.update()

