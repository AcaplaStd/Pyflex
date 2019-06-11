import pygame

pygame.init()


class WidgetDrawer:
    def __init__(self, application):
        self.application = application

    def main(self):
        self.application.win.fill(self.application.config.filling_color)
        for cell_info in self.application.wt_builder.current_frame:
            if cell_info.cell.widget.can_be_drawn:
                        issued_surface = cell_info.cell.widget.draw_myself(cell_info.cell_w, cell_info.cell_h)
                        self.application.win.blit(issued_surface, (cell_info.cell_x, cell_info.cell_y))
        pygame.display.flip()
