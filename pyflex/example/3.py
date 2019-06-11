# Events

from pyflex.app import PyFlexApp
from pyflex.config import win_modes
from pyflex.widgets.table import Table
from pyflex.widgets.button import Button
from pyflex.widgets.label import Label


class TestApp(PyFlexApp):
    def __init__(self):
        super().__init__()
        self.tablichka = Table(width_count=2, height_count=2, spacing=4)

    def configure(self):
        self.config.set_win_mode(win_modes.static)
        self.config.set_win_size(1345, 767)
        self.config.set_win_title("cnopachki, zdorovo!")
        self.config.set_win_icon_using_path("icon.bmp")

    def construct_app(self):
        self.tablichka.append_to_next_free(Button())
        self.tablichka.append_to_next_free(Button())
        # self.tablichka.append_to_next_free(Label(text="print(\"Hello\")"))
        # self.tablichka.append_to_next_free(Label(text="print(\"world\")"))
        self.tablichka.append_to_next_free(Button(color=(200, 80, 80)))
        self.tablichka.append_to_next_free(Button(color=(80, 200, 80)))

        return self.tablichka


TestApp().run_app()
