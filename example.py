import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import pyqtgraph


FormUiClass, FormBaseClass  = uic.loadUiType(".\\test1.ui")

class Ui(FormUiClass, FormBaseClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        list_1 = [1, 2, 3, 4, 5, 6, 7]
        list_2 = [23, 324, 6, 56, 54, 576, 12]

        pen = pyqtgraph.mkPen(color=('green'), width=3)

        self.widget.setBackground('w')
        self.widget.plot(list_1, list_2, pen=pen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()

# print(uic.loadUiType(".\\test.ui"))
