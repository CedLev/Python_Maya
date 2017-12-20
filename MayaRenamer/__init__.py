from PySide2 import QtWidgets
import os
import pyside2uic
from maya import cmds
import pymel.core as pymel

pyside2uic.compileUiDir(os.path.dirname(__file__))

import main_window
reload(main_window)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.pressed.connect(self.on_rename)

    def on_rename(self):
        pattern_inn = self.ui.lineEdit_from.text()
        pattern_out = self.ui.lineEdit_to.text()
        print("Will replace {0} by {1}".format(pattern_inn, pattern_out))

        objs = pymel.selected()
        for obj in objs:
            new_name = obj.name().replace(pattern_inn, pattern_out)
            obj.rename(new_name)


win = None
def show():
    global win
    win = MyWindow()
    win.show()

