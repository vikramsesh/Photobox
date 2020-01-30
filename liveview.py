import os
from omxplayer.player import OMXPlayer
import subprocess

# GUI
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt

cmd = """kill $(pgrep omxplayer) & pkill -f gphoto2 & gphoto2 --reset"""


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        self.do_init = QtCore.QEvent.registerEventType()
        QtWidgets.QMainWindow.__init__(self)
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("uiFiles/liveviewclose.ui", self)
        self.move(840, 385)

        # Disable title bar
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        self.pushButton_close.clicked.connect(self.closeOMX)

    def closeOMX(self):
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        output, error = process.communicate()
        print(output)
        QtWidgets.qApp.closeAllWindows()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec_()
