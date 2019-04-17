
#结合所有组件
import controler
import DataHandling
from window import MainWin
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
sys.exit(app.exec())