from pyflex.inside.special_classes import get_all_cells_Response
from pyflex.widgets.parents.cell import GridCell
from pyflex.widgets.parents.widget import Widget


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

        self.grid = [[GridCell() for ii in range(width_count)] for i in range(height_count)]
        self.cursor = [0, 0]  # 0 -> x; 1 -> y

    def get_all_cells(self, cell_w, cell_h):
        future_cells_width = (cell_w - self.spacing_x * (self.width_count - 1)) // self.width_count
        future_cells_height = (cell_h - self.spacing_y * (self.height_count - 1)) // self.height_count
        arr = []
        for line_ind in range(self.height_count):
            for column_ind in range(self.width_count):
                arr.append(get_all_cells_Response(column_ind * (self.spacing_x + future_cells_width),
                                                  line_ind * (self.spacing_y + future_cells_height),
                                                  future_cells_width,
                                                  future_cells_height,
                                                  self.grid[line_ind][column_ind]))

        return arr

    def append_to_next_free(self, widget):
        while not self.grid[self.cursor[1]][self.cursor[0]].is_empty():
            self.cursor[0] += 1
            if self.cursor[0] == self.width_count:
                self.cursor[0] = 0
                self.cursor[1] += 1
            if self.cursor[1] == self.height_count:
                raise Exception("Whooops. It seems that there is bug in code")
        self.set_on_coords(self.cursor[0], self.cursor[1], widget)

    def set_on_coords(self, x, y, widget):
        self.grid[y][x].fill_with_widget(widget)

    def clear_table(self):
        self.grid = [[GridCell() for ii in range(self.height_count)] for i in range(self.width_count)]
        self.cursor = [0, 0]

    def remove_one_widget(self, x, y):
        self.grid[y][x].clear()
        if y < self.cursor[1]:
            self.cursor = [x, y]
        elif y == self.cursor[1] and x < self.cursor[0]:
            self.cursor = [x, y]
