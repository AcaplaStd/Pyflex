import pygame
from typing import Iterable
from pyflex.widget_tree.WT_builder import ChildCellsResponse
from pyflex.widgets.label import Label
from pyflex.widgets.parents.cell import GridCell
from pyflex.widgets.parents.widget import Widget

pygame.init()


class Button(Widget):
    def __init__(self, text_inside=None, color=(127, 127, 127), text_height=20, hover_color=None,
                 click_color=(235, 235, 255)):
        self.can_be_drawn = True
        self.has_child_widgets = False

        self.color = color
        self.click_color = click_color
        if hover_color is None:
            self.hover_color = button_hover_color(self.color)
        else:
            self.hover_color = hover_color

        if not (text_inside is None):
            self.has_child_widgets = True

            self.text_height = text_height
            self.center_cell = GridCell()
            self.label_inside_me = Label(text=text_inside, bg_color=self.color, font_height=self.text_height)
            self.center_cell.fill_with_widget(self.label_inside_me)

    def get_all_cells(self, cell_w, cell_h, cell_x, cell_y):
        # This method will be called in case of "has_child_widgets"
        self.label_inside_me.change_font_height(self.text_height)
        return [ChildCellsResponse(0, (cell_h - self.text_height) // 2, cell_w, self.text_height, self.center_cell)]

    def draw_myself(self, cell_w, cell_h, cell_x, cell_y):
        new_surface = pygame.Surface((cell_w, cell_h))
        if self.is_hover(cell_w, cell_h, cell_x, cell_y):
            new_surface.fill(self.hover_color)
        else:
            new_surface.fill(self.color)
        return new_surface


def button_hover_color(basic_color: Iterable[int]):
    # Don't carp at the opinion of the author!
    new_color = []
    for channel in basic_color:
        if channel < 128:
            new_color.append(channel + int(20 - channel / 8))
        else:
            new_color.append(channel - int(5 + (channel - 128) / 8))
    return tuple(new_color)
