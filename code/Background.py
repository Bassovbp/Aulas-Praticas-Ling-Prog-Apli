#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # fazendo a imagem de mover no eixo x utilizando a constante por cada nome com sua velocidade
        if self.rect.right <= 0:        # efeito rolo de filme para imagem repetir quando chegar no final da tela
            self.rect.left = WIN_WIDTH
        pass
