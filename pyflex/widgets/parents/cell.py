class GridCell:
    def __init__(self):
        self.object = None

    def fill_with_widget(self, object):
        self.object = object

    def clear(self):
        self.object = None
