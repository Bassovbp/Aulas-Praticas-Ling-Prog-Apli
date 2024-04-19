#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):  # ABC = maneira de dizer que a classe é abstrata em python *precisa importar*
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() # otmiza carregamento de imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # left e top é onde a imagem começa a ser desenhada
        self.speed = 0

    @abstractmethod    # classes abstratas precisam de métodos abstratos *precisa importar* faz com que as classes filhas obrigatoriamente importem esse método
    def move(self):
        pass
