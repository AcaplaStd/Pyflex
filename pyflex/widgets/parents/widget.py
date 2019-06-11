import pygame
pygame.init()


class Widget:
    can_be_drawn = False
    has_child_widgets = True

    def draw_myself(self, cell_w, cell_h, cell_x, cell_y):
        pass

    def get_all_cells(self, cell_w, cell_h, cell_x, cell_y):
        pass

    @staticmethod
    def is_hover(width, height, widget_x, widget_y):
        m_pos_x, m_pos_y = pygame.mouse.get_pos()
        return (widget_x <= m_pos_x <= widget_x + width) and (widget_y <= m_pos_y <= widget_y + height)
