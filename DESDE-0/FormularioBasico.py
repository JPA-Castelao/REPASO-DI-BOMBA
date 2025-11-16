import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QTextEdit, QPushButton, QLabel, QFormLayout
)
from PySide6.QtCore import Qt

class Formulario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("formulario basico")
        self.setGeometry(100, 100, 500, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        #Creacion del formulario ( QFormLayout )
        form_widget = QWidget()
        self.form_layout = QFormLayout(form_widget)

        #Creacion de los campos de entrada:
        self.input_nombre = QLineEdit()
        self.input_mensaje = QTextEdit()
        self.input_mensaje.setFixedHeight(50) #altura del campo de mensaje

        # Añadimos los campos al formulario
        # El QFormLayout añade el texto de la izquierda y el widget a la derecha
        self.form_layout.addRow("nombre:", self.input_nombre)
        self.form_layout.addRow("Mensaje:", self.input_mensaje)

        # Añadimos el widget del formulario al layout principal
        main_layout.addWidget(form_widget)

        #Boton y etiqueta de estado
        self.btn_enviar = QPushButton("enviar")
        self.label_estado = QLabel("esperando datos...")
        self.label_estado.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(self.btn_enviar)
        main_layout.addWidget(self.label_estado)

        #Conexion
        self.btn_enviar.clicked.connect(self.procesar_formulario)

    def procesar_formulario(self):
        #Extraemos los datos de los Widgets:
        nombre = self.input_nombre.text().strip()
        mensaje = self.input_mensaje.toPlainText().strip()

        # Trabajo con los datos
        if nombre:
            self.label_estado.setText(f"Hola {nombre}. Tu mensaje tiene {len(mensaje)} letras")
        else:
            self.label_estado.setText("error, no pusiste ningun nombre")
            self.label_estado.setStyleSheet("color: red;")

        # Opcional: limpiar el campo de texto
        self.input_nombre.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Formulario()
    window.show()
    sys.exit(app.exec())
