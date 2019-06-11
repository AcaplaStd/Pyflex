class EvRecorder:
    def __init__(self, application):
        self.application = application

    def collect(self):
        self.application.event_catcher.lists()
        for cell_info in self.application.wt_builder.current_frame:
            pass
