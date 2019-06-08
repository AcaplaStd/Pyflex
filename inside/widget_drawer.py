def rec_widget_drawing(application):


def do_with_cell(grid_cell, cell_x, cell_y, cell_w, cell_h):
    if not (grid_cell.object is None):
        grid_cell.object.draw_myself(cell_x, cell_y, cell_w, cell_h)
        cells_in_this_widget = grid_cell.object.get_all_cells()
        for cell in grid_cell.object.get_all_cells():

