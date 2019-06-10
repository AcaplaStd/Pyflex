import pygame

pygame.init()

win_modes_pygame_value = [0, -2147483648, 16]


class WinModesClass:
    static = 0
    fullscreen = 1
    resizable = 2


__all__ = ["win_modes", "AppConfig"]

win_modes = WinModesClass()


class AppConfig:
    def __init__(self, application):
        self.application = application

        self.win_width = 300
        self.win_height = 100
        self.win_mode: int = win_modes.static
        self.win_title = "pyflex application title(caption) goes here"
        self.win_icon_path = ""

        self.check_list = [False, False, False, True]

        self.filling_color = (0, 0, 0)

    def set_win_size(self, width, height):
        self.win_width = width
        self.win_height = height
        self.check_list[0] = False

    def large_window(self):
        info = pygame.display.Info()
        self.set_win_size(info.current_w, info.current_h)
        self.set_win_mode(win_modes.fullscreen)

    def set_win_mode(self, mode):
        if type(mode).__name__ == "int":
            self.win_mode = mode
        elif type(mode).__name__ == "str":
            self.win_mode = getattr(win_modes, mode, win_modes.static)
        self.check_list[1] = False

    def set_win_title(self, new_caption):
        self.win_title = new_caption

    def set_win_icon_using_path(self, path):
        self.win_icon_path = path
        self.check_list[2] = False

    def get_updates(self):
        # Crutch
        if not self.check_list[1]:
            if not self.check_list[0]:
                self.update_mode((self.win_width, self.win_height), self.win_mode)
            else:
                self.update_mode(self.application.win.get_size(), self.win_mode)
        else:
            if not self.check_list[0]:
                self.update_mode(self.application.win.get_size(), self.win_mode)

        if self.win_title != pygame.display.get_caption()[0]:
            pygame.display.set_caption(self.win_title)

        if not self.check_list[2]:
            icon_surface = pygame.image.load(self.win_icon_path)
            pygame.display.set_icon(icon_surface)

        self.check_list = [True for i in range(4)]

    def get_size_faster(self):
        self.check_list[0] = True
        return self.win_width, self.win_height

    @staticmethod
    def update_mode(win_rect, mode_int):
        if mode_int == win_modes.static:
            pygame.display.set_mode(win_rect)
        elif mode_int == win_modes.fullscreen:
            pygame.display.set_mode(win_rect, pygame.FULLSCREEN)
        elif mode_int == win_modes.resizable:
            pygame.display.set_mode(win_rect, pygame.RESIZABLE)
