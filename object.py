import setings
import pygame
from pygame import *





#//////////////////
#player
#//////////////////
class Player(pygame.sprite.Sprite):
    def __init__(self,surface,pos):
        super().__init__()

        self.image=pygame.Surface((25,50))
        self.image.fill('red')
        self.pos=pos
        self.rect=self.image.get_rect(topleft=self.pos)
        self.surface=surface

        #player moviment
        self.direction=pygame.math.Vector2(0,0)
        self.speed=5
        self.speed_gravily=0.8
        self.speed_jump=-12

        #groups of player
        self.projectiles=pygame.sprite.Group()

    def control(self):
        
        self.press=pygame.key.get_pressed()     
        if self.press[pygame.K_d]:
            self.direction.x=1
        elif self.press[pygame.K_a]:
            self.direction.x=-1
        else:
            self.direction.x=0
        for event in pygame.event.get(768):
            if self.press[K_w] and( self.direction.y==0 or self.direction.y==0.8):
                self.direction.y=self.speed_jump
            if self.press[K_RIGHT]:
                self.atirar()


        

    def atirar(self):
        x=self.rect.x
        y=self.rect.y
        self.tiro=projectile((x,y))
        self.projectiles.add(self.tiro)
    
    def Gravily(self):
        self.direction.y+=self.speed_gravily
        self.rect.y+=self.direction.y
    
    def Jump(self): 
        self.rect.y+=self.direction.y

    def update(self):
        self.control()
        

        



#/////////////////
#chão
#/////////////////
class ground(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill('green')
        self.rect=self.image.get_rect(topleft=pos)

    def update(self,deslocamento):
        self.rect.x+=deslocamento

#////////////////
#progetil
#////////////////
class projectile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.Surface((10,10))
        self.image.fill('yellow')
        self.rect=self.image.get_rect(topleft=pos)

        self.speed=6
    
    def update(self):
        self.rect.x+=1*self.speed
