import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)

# Definimos la clase principal de la ventana:
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi app desde 0 para repasar tu sabe")
        self.setGeometry(100,100,400,200)

        #Creamos el widget central con el layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        #Creacion de Widgets ( botones y etiqueta )
        self.label_estado = QLabel("bomba")
        self.btn_principal = QPushButton("Boton bomba")
        self.btn_secundario = QPushButton("boton secundario")

        #añadimos los widgets creados arriba a los layouts:
        #se apilarán verticalmente
        self.main_layout.addWidget(self.label_estado)
        self.main_layout.addWidget(self.btn_principal)
        self.main_layout.addWidget(self.btn_secundario)

        #Conexion de señales ( conectamos cada evento con su botón correspondiente )
        self.btn_principal.clicked.connect(self.handle_principal_click)
        self.btn_secundario.clicked.connect(self.handle_secundario_click)

    def handle_principal_click(self):
            """funcion que se ejecuta cuando pulsas el boton princicpal"""
            print("boton pulsado")
            self.label_estado.setText("Has pulsado el boton princicpal")
            self.label_estado.setStyleSheet("color: blue;")

    def handle_secundario_click(self):
            """funcion que se ejecuta cuando pulsas el boton secundario"""
            print("boton pulsado")
            self.label_estado.setText("Has pulsado el boton secundario")
            self.label_estado.setStyleSheet("color: green;")


if __name__ == "__main__":
    app = QApplication(sys.argv) #Crea la instancia de la app
    window = MiVentana() # Crea la ventana
    window.show() # La muestra
    sys.exit(app.exec()) #Inicia el bucle de eventos