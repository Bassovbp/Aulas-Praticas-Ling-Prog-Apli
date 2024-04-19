#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()  # otmiza carregamento de imagem
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # ./ antes de asset é para sair da pasta code e entrar em asset
        pygame.mixer_music.play(-1)  # -1 significa rodar indefinidamente
        menu_option = 0
        while True:
            # desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)  # blit desenha a tela
            self.menu_text(50, "Cities", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "WAR", COLOR_ORANGE, ((WIN_WIDTH / 2), 130))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 200 + 30 * i))
            pygame.display.flip()  # flip atualiza a tela OBS: tem que ficar após o ultimo elemento de desenhar na tela

            # verificar eventos
            for event in pygame.event.get():     # interação com cliques, teclas
                if event.type == pygame.QUIT:
                    pygame.quit()            # aqui fecha o pygame, mas ainda rodaria o resto e daria erro.
                    sys.exit()                          # com o sys exit ele finaliza tudo.
                if event.type == pygame.KEYDOWN:                # testar se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN:   # se a seta para baixo for pressionada
                        if menu_option < len(MENU_OPTION)-1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:    # se a seta para cima for pressionada
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION)-1
                    if event.key == pygame.K_RETURN:   # se enter for pressionado
                        return MENU_OPTION[menu_option]  # retorna o texto do menu

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
