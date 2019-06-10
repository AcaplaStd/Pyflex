from pyflex.config import win_modes_pygame_value
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

    def main(self):
        events_list = pygame.event.get()
        for event in events_list:
            if (event.type == pygame.QUIT) or (
                    event.type == pygame.KEYDOWN and event.key == 285):
                self.application.running = False
            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((event.w, event.h), win_modes_pygame_value[self.application.config.win_mode])
            else:
                self.serve_the_event(event)

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
