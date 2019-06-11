import pygame

from pyflex.config import AppConfig
from pyflex.events.catcher import MainEventCatcher
from pyflex.widget_tree.WT_builder import WTBuilder
from pyflex.widget_tree.widget_drawer import WidgetDrawer
from pyflex.events.recorder import EvRecorder
from pyflex.widgets.parents.cell import GridCell

pygame.init()

__all__ = ["PyFlexApp"]


class PyFlexApp:
    def __init__(self):
        self.config: AppConfig = AppConfig(self)
        self.wt_builder = WTBuilder(self)
        self.ev_recorder = EvRecorder(self)
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
            self.config.get_updates()

            self.wt_builder.start_building()

            self.ev_recorder.collect()

            self.event_catcher.main()

            self.widget_drawer.main()

        pygame.quit()

    def configure(self):
        pass

    def construct_app(self):
        raise Exception("Write your build function")
