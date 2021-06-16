import sys
import pygame
from item import Bala

#Checa as teclas
def check_event(config,tela,balitas):
    new_item = Bala(config,tela)
    balitas.add(new_item)
    for action in pygame.event.get():
        #Para sair do jogo
        if action.type == pygame.QUIT:
            sys.exit()

#Mantém as balas funcionando
def update_bala(config,balitas):
    balitas.update()
    for bala in balitas.copy():
        if bala.rect.bottom >= config.tela_H:
            balitas.remove(bala)

#Atualiza as parada que tem na tela
def updater(config,tela,balitas):
    tela.fill(config.tela_cor)
    for item in balitas.sprites():
        item.draw_item()
    pygame.display.flip()
