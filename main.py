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
        self.cidade_label = QLabel("Digite o nome da cidade: ", self)
        self.cidade_input = QLineEdit(self)
        self.get_clima_button = QPushButton("Veja o clima!", self)
        self.temperatura_label = QLabel("15°C", self)
        self.emoji_label = QLabel("☀️", self)
        self.descricao_label = QLabel("Ensolarado", self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    App_Clima = AppClima() 
    App_Clima.show()
    sys.exit(app.exec_())