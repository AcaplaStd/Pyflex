from pyflex.app import PyFlexApp
from pyflex.widgets.button import Button
from pyflex.widgets.table import Table


class MyApp(PyFlexApp):
    def __init__(self):
        super().__init__()
        self.main_grid_table = Table(width_count=2, height_count=4, spacing=2)

    def configure(self):
        self.config.large_window()
        self.config.set_win_title("table")
        self.config.set_win_icon_using_path("icon.bmp")

    def construct_app(self):
        for i in range(8):
            self.main_grid_table.append_to_next_free(Button(text_inside=str(i)))
        return self.main_grid_table


MyApp().run_app()
