from pyflex.widgets.parents.widget import Widget
from pyflex.widgets.parents.cell import GridCell
from pyflex.widgets.label import Label
from pyflex.inside.special_classes import get_all_cells_Response
import pygame
pygame.init()


class Button(Widget):
    def __init__(self, text_inside=None, color=(127, 127, 127)):
        self.can_be_drawn = True
        self.color = color
        self.has_child_widgets = False
        if not (text_inside is None):
            self.has_child_widgets = True
            self.center_cell = GridCell()
            self.label_inside_me = Label(text=text_inside, bg_color=self.color)
            self.center_cell.fill_with_widget(self.label_inside_me)

    def get_all_cells(self, cell_w, cell_h):
        # This method will be called in case of "has_child_widgets"
        one_of_three_from_height = cell_h // 3
        self.label_inside_me.change_font_height(one_of_three_from_height)
        return [get_all_cells_Response(0, one_of_three_from_height, cell_w, one_of_three_from_height, self.center_cell)]

    def draw_myself(self, cell_w, cell_h):
        new_surface = pygame.Surface((cell_w, cell_h))
        new_surface.fill(self.color)
        return new_surface
