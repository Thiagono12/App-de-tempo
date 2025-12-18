#Vamos começar importando as libs necessarias
#Let's start by importing the required libs
import sys 
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout)  
from PyQt5.QtCore import Qt 
#A lib PyQT5, nos permite criar uma interface visual
#PyQt5 allows us to create visual interface

class AppClima(QWidget): #Criamos uma classe para definir oq teremos na tela Inicial, como a planta de uma casa # We create a Class to define what will be on our screen, serving as a blueprint
    def __init__(self):
        super().__init__() #A herença da nossa classe é a QWidget, inicializamos a herança do pai chamando a função super #Our class inherits from QWidget, we initialize the parent class calling the function super()
        self.cidade_label = QLabel("Digite o nome da cidade: ", self) #prompting for the user
        self.cidade_input = QLineEdit(self) #city name input
        self.get_clima_button = QPushButton("Veja o clima!", self) #Botão para ver o clima #button to fetch the weather
        self.temperatura_label = QLabel(self) #temperature label
        self.emoji_label = QLabel(self) #Displays emoji based on weather
        self.descricao_label = QLabel(self) #description of the weather condition, for example: "raining"
        self.initUI()
    
    def initUI(self): #Definimos a função para iniciar a UI #Defining the function to start the UI
        self.setWindowTitle("App de Clima")

        vbox = QVBoxLayout() #fazendo nosso layout no formato de widgets em Vbox #Making our layout, using vbox

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

        #dando nome aos objetos 
        #giving name for the objects
        self.cidade_label.setObjectName("cidade_label") 
        self.cidade_input.setObjectName("cidade_input")
        self.temperatura_label.setObjectName("temperatura_label")
        self.get_clima_button.setObjectName("get_clima_button")
        self.emoji_label.setObjectName("emoji_label")
        self.descricao_label.setObjectName("descricao_label")

        self.setStyleSheet(""" 
                QLabel, QPushbutton{
                           font-family: Calibir;
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

            """) #Estilizando as fontes #Styling the fonts
            
        self.get_clima_button.clicked.connect(self.get_clima)


    #Função para obter o clima
    #Function to get the weather
    def get_clima(self): 
        
        api_key = "9d53a2dd349290061af" #sua chave api #your apikey
        cidade = self.cidade_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}" #usando Fstring par subistutir o link #using the F str to replace the URL

        #exception block, to show what went wrong
        #bloco para mostrar o erro 
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            data = resposta.json()

            if data ["cod"] == 200:
                self.mostrar_clima(data)

                 

        except requests.exceptions.HTTPError as http_error:
            match resposta.status_code:
                case 400:
                    self.mostrar_erro("Não deu amigo!\nPor favor olhe o que digitou")
                case 401:
                    self.mostrar_erro("Não Autorizado\n chave api key inválida")
                case 403:
                    self.mostrar_erro("Aceso negado.")
                case 404:
                    self.mostrar_erro("Não encontrado\n Cidade não encontrada")
                case 500:
                    self.mostrar_erro("Problemas no servidor\nPor favor tente mais tarde")
                case 502:
                    self.mostrar_erro("Porta de entrada com problemas\nResposta de sesrvidor inválida")
                case 503:
                    self.mostrar_erro("Serviço indisponível\nServidor caiu")
                case 504:
                    self.mostrar_erro("Porta de entrada timeout\n Sem resposta do servidor")
                case _:
                    self.mostrar_erro(f"Ocorreu um erro HTTP\n {http_error}")

        except requests.exceptions.ConnectionError:
            self.mostrar_erro("Erro na conexão\n Veja sua conexão")
        except requests.exceptions.TooManyRedirects:
            self.mostrar_erro("Muitos pedidos\Olhe sua Url")
        except requests.exceptions.Timeout:
            self.mostrar_erro("Erro de tempo")
        except requests.exceptions.RequestException as req_error:
            self.mostrar_erro(f"Request eRROR: \n{req_error}")



        

    def mostrar_erro(self, msg):
        self.temperatura_label.setStyleSheet("font-size : 30px;")
        self.temperatura_label.setText(msg)
    


    #function to display the weather. The Api fetches data, using the field that user entered (city name). And converts the result from K to C
    #função para mostrar o clima. A API busca, usando o campo que o usuario escreveu antes (nome da cidade). E converte o resultado de K para C
    def mostrar_clima(self, data):
        self.temperatura_label.setStyleSheet("font-size: 30px;")
        temperatura_k = data["main"]["temp"]
        temperatura_c = temperatura_k - 273.15
        weather_id = data["weather"][0]["id"]
        tempo_descricao = data["weather"][0]["description"]
        
        self.temperatura_label.setText(f"{temperatura_c:.2f}°C")
        self.emoji_label.setText(self.get_tempo_emoji(weather_id))
        self.descricao_label.setText(f"{tempo_descricao}")


    #Displays emoji based on the weather_id
    #Mostra emoji baseado no clima_id
    @staticmethod
    def get_tempo_emoji(weather_id):
        
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌁"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🍃"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
        

    #Main
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    App_Clima = AppClima() 
    App_Clima.show()
    sys.exit(app.exec_())