from pyflex.config import AppConfig, win_modes_pygame_value
from pyflex.widgets.parents.cell import GridCell
from pyflex.events.catcher import MainEventCatcher
from pyflex.inside.widget_drawer import WidgetDrawer
import pygame
pygame.init()

__all__ = ["PyFlexApp"]


class PyFlexApp:
    def __init__(self):
        self.config: AppConfig = AppConfig(self)
        self.event_catcher = MainEventCatcher(self)
        self.widget_drawer = WidgetDrawer(self)

        self.win = None
        self.main_cell = GridCell()
        self.running = True

    def run_app(self):
        self.configure()  # Post init
        self.main_cell.fill_with_widget(self.construct_app())
        self.win = pygame.display.set_mode(self.config.get_size_faster())

        while self.running:
            events_list = pygame.event.get()
            for event in events_list:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode((event.w, event.h), win_modes_pygame_value[self.config.win_mode])
                else:
                    self.event_catcher.serve_the_event(event)

            self.config.get_updates()

            self.widget_drawer.rec_widget_drawing()

        pygame.quit()

    def configure(self):
        pass

    def construct_app(self):
        raise Exception("Write your build function")
