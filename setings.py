#local onde se encontra os objetos e funções
from asyncio import events
import pygame
import object 


#constantes do jogo
screen_width=1000
screen_height=700

def Event():
    for event in pygame.event.get(256):
        print(event)
        if event.type == 256:
            pygame.quit()
            exit()
     

class Level:
    def __init__(self,surface,level):
        self.surface=surface
        self.level=level

        #grupos
        self.players=pygame.sprite.Group()
        self.grounds=pygame.sprite.Group()
        

    def Add(self):
        for y in range(0,len(self.level)):
            for x in range(0,len(self.level[y])):

                if self.level[y][x]=='x':
                    self.chão=object.ground((x*50,y*50))
                    self.grounds.add(self.chão)

                if self.level[y][x]=='p':
                    self.jogador=object.Player(self.surface,(x*50 ,y*50))
                    self.players.add(self.jogador)
    
    def MovLevel(self):
        jogador=self.jogador
        rect_x=jogador.rect.centerx
        if rect_x>(screen_width/5)*4 and jogador.direction.x>0:
            self.word_mov=-5
            jogador.speed=0
        elif rect_x<screen_width/5 and jogador.direction.x<0:
            self.word_mov=5
            jogador.speed=0
        else:
            self.word_mov=0
            jogador.speed=5
    

    def colisionX(self):
        player=self.jogador
        player.rect.x+=player.direction.x*player.speed
        projectiles=player.projectiles

        for object in self.grounds.sprites():
            if object.rect.colliderect(self.jogador.rect):
                if self.jogador.direction.x>0:
                    self.jogador.rect.right=object.rect.left
                elif self.jogador.direction.x<0:
                    self.jogador.rect.left=object.rect.right


    def ColisionY(self):
        player=self.jogador
        player.Gravily()
        player.Jump()

    

        for object in self.grounds.sprites():
            if object.rect.colliderect(self.jogador.rect):
                if player.direction.y>0:
                    player.rect.bottom=object.rect.top
                    player.direction.y=0
                elif player.direction.y<0:
                    player.rect.top=object.rect.bottom
                    player.direction.y=0
        

    def Run(self):
        self.MovLevel()
        self.grounds.draw(self.surface)
        self.grounds.update(self.word_mov)
        self.jogador.projectiles.draw(self.surface)
        #player 
        self.jogador.update()
        self.players.draw(self.surface)
        self.colisionX()
        self.ColisionY()
            #player sons
        self.jogador.projectiles.update()


