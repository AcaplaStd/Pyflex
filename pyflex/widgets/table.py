from pyflex.widgets.parents.widget import Widget
from pyflex.widgets.parents.cell import GridCell
from pyflex.inside.special_classes import get_all_cells_Response


class Table(Widget):
    def __init__(self, width_count, height_count, spacing_x=0, spacing_y=0, spacing=None):
        self.can_be_drawn = False
        self.has_child_widgets = True

        self.width_count = width_count
        self.height_count = height_count
        if spacing is None:
            self.spacing_x = spacing_x
            self.spacing_y = spacing_y
        else:
            self.spacing_x = self.spacing_y = spacing

        self.grid = [[GridCell() for ii in range(height_count)] for i in range(width_count)]
        self.cursor = [0, 0]

    def get_all_cells(self, cell_w, cell_h):
        arr = []

    def append_to_next_free(self, widget):
        while self.cursor[0] < self.width_count:
            if self.grid[self.cursor[0]][self.cursor[1]].is_empty():
                self.set_on_coords(self.cursor[0], self.cursor[1], widget)
                break
            else:
                if self.cursor[1] == self.width_count - 1:
                    self.cursor[0] += 1
                    self.cursor[1] = 0
                else:
                    self.cursor[1] += 1
        else:
            self.cursor = [0, 0]

    def set_on_coords(self, x, y, widget):
        self.grid[x][y].fill_with_widget(widget)

    def clear_table(self):
        self.grid = [[GridCell() for ii in range(self.height_count)] for i in range(self.width_count)]
        self.cursor = [0, 0]

    def remove_one_widget(self, x, y):
        pass
