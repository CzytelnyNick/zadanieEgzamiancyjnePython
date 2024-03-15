
duze = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
male = "abcdefghijklmnopqrstuvwxyz"
cyfry = "0123456789"
special = "!@#$%^&*()_+-="
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QMainWindow
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QPixmap
import sys

class Egzamin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('egzamiacyjne.ui', self)
        self.ui.nameLineEdit
        self.show()
        
    

app = QApplication(sys.argv)
egzam = Egzamin()
sys.exit(app.exec())