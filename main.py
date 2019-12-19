from PySide2.QtCore import QThread, SIGNAL
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtGui import QIcon, QPixmap
# from PySide2 import QtCharts

from window import Ui_MainWindow
import logging
from classify import classify


class classifyBackground(QThread):
    def __init__(self, path):
        QThread.__init__(self)
        self.path = path

    def run(self):
        classify(self.path)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def getPath(self):
        self.path = QFileDialog.getExistingDirectory()
        self.ui.pathEdit.setText(self.path)

    def start(self):
        self.path = self.ui.pathEdit.text()
        self.ui.statusLabel.setText("working")
        self.classifyThread = classifyBackground(self.path)
        self.connect(self.classifyThread, SIGNAL('finished()'), self.done)
        self.classifyThread.start()

    def done(self):
        self.ui.statusLabel.setText("Done! Result save in path + classify.csv")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                        format='%(asctime)s - %(levelname)s: %(message)s')
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
