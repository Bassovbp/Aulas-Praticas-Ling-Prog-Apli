#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


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
