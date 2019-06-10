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
