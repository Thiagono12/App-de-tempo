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
        self.temperatura_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.descricao_label = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("App de Clima")

        vbox = QVBoxLayout()

        vbox.addWidget(self.cidade_label)
        vbox.addWidget(self.cidade_input)
        vbox.addWidget(self.get_clima_button)
        vbox.addWidget(self.temperatura_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.descricao_label)

        self.setLayout(vbox)

        self.cidade_label.setAlignment(Qt.AlignCenter)
        self.cidade_input.setAlignment(Qt.AlignCenter)
        self.temperatura_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.descricao_label.setAlignment(Qt.AlignCenter)

        self.cidade_label.setObjectName("cidade_label")
        self.cidade_input.setObjectName("cidade_input")
        self.temperatura_label.setObjectName("temperatura_label")
        self.get_clima_button.setObjectName("get_clima_button")
        self.emoji_label.setObjectName("emoji_label")
        self.descricao_label.setObjectName("descricao_label")

        self.setStyleSheet(""" 
                QLabel, QPushbutton{
                           font-family: calibir;
                           }
                           QLabel#cidade_label{
                                font-size: 40px;
                                font-style: italic;
                           }

                           QLineEdit#cidade_input{
                           font-size: 40px;
                           }

                           QPushButton#get_clima_button{
                           font-size: 30px;
                           font-weight: bold;
                           }

                           QLabel#temperatura_label{
                           font-size: 75px;
                           }

                           QLabel#emoji_label{
                           font-size: 100px;
                           font-family: Segoe UI emoji;
                           }

                            QLabel#descricao_label{
                           font-size: 50px;
                           }

            """)
            
        self.get_clima_button.clicked.connect(self.get_clima)

    def get_clima(self):
        
        api_key = "9d53a2dd349290061af70390aa033b15"
        cidade = self.cidade_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"

        
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            data = resposta.json()

            if data ==["cod"] == 200:
                self.mostrar_clima(data)

                 

        except requests.exceptions.HTTPError:
            match resposta.status_code:
                case 400:
        except requests.exceptions.RequestException:
            pass

        

    def mostrar_erro(self, msg):
        pass
    

    def mostrar_clima(self, data):
        pass






if __name__ == "__main__":
    app = QApplication(sys.argv)
    App_Clima = AppClima() 
    App_Clima.show()
    sys.exit(app.exec_())