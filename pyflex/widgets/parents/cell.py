class GridCell:
    def __init__(self):
        self.widget = None

    def fill_with_widget(self, object):
        self.widget = object

    def clear(self):
        self.widget = None

    def is_empty(self):
        return self.widget is None
