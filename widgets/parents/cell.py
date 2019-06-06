class GridCell:
    def __init__(self):
        self.filled = False
        self.object = None

    def fill_with_widget(self, object):
        self.object = object
        self.filled = True

    def clear(self):
        self.object = None
        self.filled = False
