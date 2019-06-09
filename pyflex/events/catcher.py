from pyflex.config import win_modes_pygame_value, win_modes
# from pyflex.app import PyFlexApp
import pygame
pygame.init()


class MainEventCatcher:
    def __init__(self, application):
        self.application = application

        self.MOUSE_BUTTON_DOWN_events = []
        self.MOUSE_BUTTON_UP_events = []
        self.KEY_UP_events = []
        self.KEY_DOWN_events = []
        self.MOUSE_MOVE_events = []

    def serve_the_event(self, event):
        if event.type == pygame.KEYDOWN and len(self.KEY_DOWN_events) != 0:
            pass
        elif event.type == pygame.KEYDOWN and len(self.KEY_DOWN_events) != 0:
            pass
        elif event.type == pygame.KEYDOWN and len(self.KEY_DOWN_events) != 0:
            pass
        elif event.type == pygame.KEYDOWN and len(self.KEY_DOWN_events) != 0:
            pass
        elif event.type == pygame.KEYDOWN and len(self.KEY_DOWN_events) != 0:
            pass

    def videoresize_event(self, ev):
        if self.application.config.win_mode == win_modes.fullscreen:
            pygame.display.set_mode(self.application.config.get_size_faster(), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode((ev.w, ev.h), win_modes_pygame_value[self.application.config.win_mode])

