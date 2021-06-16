import pygame
from pygame.sprite import Sprite
import random

#Classe para as balas (7belo intensifies)
class Bala(Sprite):
    def __init__(self,config,tela):
        super().__init__()
        self.tela = tela
    #Cria o projétil e define a posição
        self.rect = pygame.Rect(0,0,config.bala_W,config.bala_H)
        self.rect.centerx = random.randint(0,config.tela_W)
        self.rect.bottom = 0
    #Armazeza a posição como um valor decimal (float)
        self.y = float(self.rect.y)
        self.color = config.bala_cor
        self.velocidade_item = config.velocidade_item

    def draw_item(self):
        pygame.draw.rect(self.tela,self.color,self.rect)

    def update(self):
    #Atualiza a posição decimal
        self.y += self.velocidade_item
        self.rect.y = self.y

    def blitme(self):
        self.tela.blit(self.imagem,self.rect)
