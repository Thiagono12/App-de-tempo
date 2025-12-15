#Vamos começar importando as libs necessarias
#Let's start by importing the required libs
import sys 
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class AppClima(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    App_Clima = AppClima()
    App_Clima.show()
    sys.exit(app.exec_())