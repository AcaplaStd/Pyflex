import pygame
pygame.init()


class WinModesClass:
    static = 0
    fullscreen = 1
    resizable = 2


__all__ = ["win_modes", "AppConfig"]

win_modes = WinModesClass()


class AppConfig:
    def __init__(self):
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
        result = {}
        if not self.check_list[0]:
            result["size"] = (self.win_width, self.win_height)
        if not self.check_list[1]:
            result["mode"] = self.win_mode
        result["title"] = self.win_title
        if not self.check_list[2]:
            result["icon_path"] = self.win_icon_path

        self.check_list = [True for i in range(4)]
        return result

    def get_size_faster(self):
        self.check_list[0] = True
        return self.win_width, self.win_height
