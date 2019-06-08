from pyflex.config import AppConfig, win_modes
from pyflex.widgets.parents.cell import GridCell
from pyflex.events.catcher import MainEventCatcher
import pygame
pygame.init()

__all__ = ["PyFlexApp"]


class PyFlexApp:
    def __init__(self):
        self.config: AppConfig = AppConfig()
        self.event_catcher = MainEventCatcher(self)

        self.win = None
        self.pix_array = None

        self.main_cell = GridCell()
        self.running = True

    def get_updates_from_config(self):
        result = self.config.get_updates()
        if "mode" in result.keys():
            if "size" in result.keys():
                self.update_mode(result["size"], result["mode"])
            else:
                self.update_mode(self.win.get_size(), result["mode"])

        if result["title"] != pygame.display.get_caption()[0]:
            pygame.display.set_caption(result["title"])

        if "icon_path" in result.keys():
            icon_surface = pygame.image.load(result["icon_path"])
            pygame.display.set_icon(icon_surface)

    @staticmethod
    def update_mode(win_rect, mode_int):
        if mode_int == win_modes.static:
            pygame.display.set_mode(win_rect)
        elif mode_int == win_modes.fullscreen:
            pygame.display.set_mode(win_rect, pygame.FULLSCREEN)
        elif mode_int == win_modes.resizable:
            pygame.display.set_mode(win_rect, pygame.RESIZABLE)

    def run_app(self):
        self.configure()  # Post init
        self.main_cell.fill_with_widget(self.construct_app())
        self.win = pygame.display.set_mode(self.config.get_size_faster())
        self.pix_array = pygame.PixelArray(self.win)

        while self.running:
            self.get_updates_from_config()
            events_list = pygame.event.get()
            for event in events_list:
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.event_catcher.serve_the_event(event)

            self.win.fill(self.config.filling_color)


        pygame.quit()

    def configure(self):
        pass

    def construct_app(self):
        raise Exception("Write your build function")
