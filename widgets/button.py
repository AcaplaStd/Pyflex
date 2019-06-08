from pyflex.widgets.parents.widget import Widget
from pyflex.widgets.parents.cell import GridCell
from pyflex.widgets.label import Label


class Button(Widget):
    def __init__(self, text_inside=None, color=(127, 127, 127)):
        self.can_be_drawn = True
        self.color = color
        self.has_widget_inside = False
        if not (text_inside is None):
            self.has_widget_inside = True
            self.center_cell = GridCell()
            self.label_inside_me = Label(text=text_inside)
            self.center_cell.fill_with_widget(self.label_inside_me)

    def get_all_cells(self):
        pass

    def draw_myself(self, cell_x, cell_y, cell_w, cell_h, application):
        pass
