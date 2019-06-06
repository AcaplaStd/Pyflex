from pyflex.app import PyFlexApp
from pyflex.config import win_modes


class MyApp(PyFlexApp):
    def configure(self):
        self.config.set_win_mode(win_modes.resizable)
        self.config.set_win_size(1200, 700)
        self.config.set_win_title("Hello, world!")
        self.config.set_win_icon_using_path("icon.bmp")

    def construct_app(self):
        pass


MyApp().run_app()
