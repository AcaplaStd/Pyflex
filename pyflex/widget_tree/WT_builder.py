from typing import List
from pyflex.inside.special_classes import get_all_cells_Response


class WTBuilder:
    def __init__(self, application):
        self.application = application
        self.current_frame = []

    def start_building(self):
        app_win_size = self.application.win.get_size()
        self.do_with_cell(self.application.main_cell, 0, 0, app_win_size[0], app_win_size[1])

    def do_with_cell(self, grid_cell, cell_x, cell_y, cell_w, cell_h):
        if not (grid_cell.widget is None):
            self.current_frame.append(DoneCellInfo(cell_x, cell_y, cell_w, cell_h, grid_cell))

            if grid_cell.widget.has_child_widgets:
                cells_in_this_widget: List[get_all_cells_Response] = grid_cell.widget.get_all_cells(cell_w, cell_h)
                for cell_r in cells_in_this_widget:
                    self.do_with_cell(cell_r.cell,
                                      cell_x + cell_r.cell_x, cell_y + cell_r.cell_y, cell_r.cell_w, cell_r.cell_h)


class DoneCellInfo(get_all_cells_Response):
    pass
