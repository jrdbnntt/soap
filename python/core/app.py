###
# Handles main running application
###

import sys
from .settings import SettingsManager
from gui.main_window import *
from PyQt5.QtWidgets import QApplication


class App(object):

    def __init__(self):
        self.settings = SettingsManager()
        self.app = QApplication([])
        self.gui = MainWindow(app=self)
        self.setup()

    def setup(self):
        self.gui.show()
        self.gui.resize(self.settings.get('application_width_initial'),
                        self.settings.get('application_height_initial'))

    def open(self):
        self.app.exec_()

    def suspend(self):
        pass

    def close(self):
        self.exit()

    def exit(self):
        """ Runs cleanup and then closes the app """
        self.app.exit()
        sys.exit()

