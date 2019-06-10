import pygame

pygame.init()


class WidgetDrawer:
    def __init__(self, application):
        self.application = application

    # def rec_widget_drawing(self):
    #     self.application.win.fill(self.application.config.filling_color)
    #     app_win_size = self.application.win.get_size()
    #     self.do_with_cell(self.application.main_cell, 0, 0, app_win_size[0], app_win_size[1])
    #     pygame.display.flip()
    #
    # def do_with_cell(self, grid_cell, cell_x, cell_y, cell_w, cell_h):
    #     if not (grid_cell.widget is None):
    #         if grid_cell.widget.can_be_drawn:
    #             issued_surface = grid_cell.widget.draw_myself(cell_w, cell_h)
    #             self.application.win.blit(issued_surface, (cell_x, cell_y))
    #
    #         if grid_cell.widget.has_child_widgets:
    #             cells_in_this_widget: List[get_all_cells_Response] = grid_cell.widget.get_all_cells(cell_w, cell_h)
    #             for cell_r in cells_in_this_widget:
    #                 self.do_with_cell(cell_r.cell,
    #                                   cell_x + cell_r.cell_x, cell_y + cell_r.cell_y, cell_r.cell_w,
    #                                   cell_r.cell_h)  # Crutch

    def main(self):
        self.application.win.fill(self.application.config.filling_color)
        for cell_info in self.application.wt_builder.current_frame:
            if cell_info.cell.widget.can_be_drawn:
                        issued_surface = cell_info.cell.widget.draw_myself(cell_info.cell_w, cell_info.cell_h)
                        self.application.win.blit(issued_surface, (cell_info.cell_x, cell_info.cell_y))
        pygame.display.flip()