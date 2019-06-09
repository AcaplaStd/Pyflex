from pyflex.app import PyFlexApp
from pyflex.config import win_modes
from pyflex.widgets.button import Button
from pyflex.widgets.label import Label
from pyflex.widgets.table import Table


class MyApp(PyFlexApp):
    def __init__(self):
        super().__init__()
        self.main_grid_table = Table()

    def configure(self):
        self.config.large_window()
        self.config.set_win_title("table")
        self.config.set_win_icon_using_path("icon.bmp")

    def construct_app(self):

        return self.main_grid_table


MyApp().run_app()
