import pygame
import game_func as gf
from config_diy import Atributos
from pygame.sprite import Group


def game():
    pygame.init()
#Cria a instância para as configurações
    config = Atributos()
#Define a tela e seu título
    tela = pygame.display.set_mode((config.tela_W,config.tela_H))
    pygame.display.set_caption('Rain')
    balitas = Group()
#Laço inicial do jogo
    while True:
        gf.check_event(config,tela,balitas)
        balitas.update()
        gf.update_bala(config,balitas)
        gf.updater(config,tela,balitas)

#Run it!
game()
