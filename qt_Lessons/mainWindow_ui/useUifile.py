import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file = QFile("mainWindow.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()

    window = loader.load(ui_file)
    window.show()

    sys.exit(app.exec_())