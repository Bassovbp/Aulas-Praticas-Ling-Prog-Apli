#!/usr/bin/python
#-*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    # def __init__(self):   --> não sera instanciado objeto na classe fabrica, vai usar somente o método
    #     pass

    @staticmethod    # método estático, não precisa instanciar objeto para usar o método
    def get_entity(entity_name: str, position=(0,0)):  # se eu não passar posição usará a padrão colocada ali
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0))) # copiando a imagem e colocando pra iniciar no fim da tela
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 50)) # - 50 em relação ao meio pra nao ficarem sobrepostas

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 50))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))  # random para sorter a posição onde vai nascer o inimigo

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))  # + 40 e - 40 pra nao ficar nem muito em cima e nem muito embaixo da tela
