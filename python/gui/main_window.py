

from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle(app.settings.get('application_name'))

    def init_ui(self):
        self.setMinimumHeight(self.app.settings.get('application_height_min'))
        self.setMinimumWidth(self.app.settings.get('application_width_min'))



