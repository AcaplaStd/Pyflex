class GridCell:
    def __init__(self):
        self.widget = None

        # TODO: Config goes here

    def fill_with_widget(self, widget):
        self.widget = widget

    def clear(self):
        self.widget = None

    def is_empty(self):
        return self.widget is None
