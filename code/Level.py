#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface

from code.Const import MENU_OPTION, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) # extend para concatenar, se não vai adicionar lista dentro da lista
        self.entity_list.append(EntityFactory.get_entity('Player1')) # append porque é um unico objeto
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)  # colocando um cronometro para evento criado por mim. cria inimigo a cada 4 segundos

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(50)                  # cada 1 segundo roda 50x o laço while (50 FPS-> frame por seg)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # verificando de novo evento para sair do jogo
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice (('Enemy1', 'Enemy2')) # sorteia o inimigo
                    self.entity_list.append(EntityFactory.get_entity(choice)) # adiciona na lista
            pygame.display.flip()
        pass
