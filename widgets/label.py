from pyflex.widgets.parents.widget import Widget
import pygame
pygame.init()


class Label(Widget):
    def __init__(self, text="Text goes here", color=(255, 255, 255), antialias=False, font_height=20, font_path=None
                 ):
        self.can_be_drawn = True
        self.text = text
        self.color = color
        self.antialias = antialias

        self.font = pygame.font.Font(font_path, font_height)
        self.__font_height = font_height
        self.__font_path = font_path

    def draw_myself(self, cell_x, cell_y, cell_w, cell_h, application):
        text_surface = self.font.render(self.text, self.antialias, self.color)

    def change_font_height(self, new_height):
        self.__font_height = new_height
        self.font = pygame.font.Font(self.__font_path, self.__font_height)

    def change_font_path(self, new_path):
        self.__font_path = new_path
        self.font = pygame.font.Font(self.__font_path, self.__font_height)
