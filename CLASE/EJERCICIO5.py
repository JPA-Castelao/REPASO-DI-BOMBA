import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QTextEdit, QPushButton, QLabel, QFormLayout
)
from PySide6.QtCore import Qt

class FormularioSimple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario Simple de Contacto")
        self.setGeometry(100, 100, 500, 350) # Establece la posición y tamaño de la ventana.

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget) # Layout principal: organiza todo verticalmente.

        # CREACIÓN DO FORMULARIO
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget) # QFormLayout: organiza etiquetas y campos en dos columnas.

        # Campos de entrada
        self.input_nome = QLineEdit() # QLineEdit: Cadro de texto de una sola línea para el nombre.
        self.input_email = QLineEdit() # QLineEdit: Cadro de texto de una sola línea para el email.
        self.input_mensaje = QTextEdit() # QTextEdit: Cadro de texto multilínea para el mensaje.
        self.input_mensaje.setFixedHeight(100) # Fija la altura del campo de mensaje para mejor estética.

        # Añadir elementos al QFormLayout
        form_layout.addRow("Nome:", self.input_nome)
        form_layout.addRow("Email:", self.input_email)
        form_layout.addRow("Mensaxe:", self.input_mensaje)

        main_layout.addWidget(form_widget)

        # BOTÓN DE ENVÍO
        self.btn_enviar = QPushButton("Enviar")
        self.btn_enviar.setStyleSheet("padding: 10px; font-size: 14px;")

        # Conexión: Al hacer clic, se llama al método validar_e_enviar, que contiene la lógica.
        self.btn_enviar.clicked.connect(self.validar_e_enviar)
        main_layout.addWidget(self.btn_enviar)

        # ETIQUETA DE ESTADO/MENSAXE
        self.label_estado = QLabel("Esperando...")
        self.label_estado.setAlignment(Qt.AlignCenter) # Centra el texto de la etiqueta.
        self.label_estado.setStyleSheet("font-weight: bold; padding: 15px; border: 1px solid #ccc;")
        main_layout.addWidget(self.label_estado)

        main_layout.addStretch() # Empuja los widgets hacia la parte superior.

    # LÓXICA DE VALIDACIÓN

    def validar_e_enviar(self):
        """
        Método SLOTS: Se activa al pulsar 'Enviar'.
        Función: Comprueba si todos los campos tienen contenido.
        """

        # Obtener los textos de los QLineEdit y QTextEdit, eliminando espacios iniciales/finales.
        nome = self.input_nome.text().strip()
        email = self.input_email.text().strip()
        mensaje = self.input_mensaje.toPlainText().strip() # Se usa toPlainText() para QTextEdit.

        # 1. Comprobación de campos vacíos. 'not' evalúa si la cadena está vacía (True si está vacía).
        if not nome or not email or not mensaje:
            # Mostrar mensaxe de erro
            self.label_estado.setText("Faltan datos. Completa todos os campos.")
            # Estilo para erro: cambia el fondo y el color del texto a rojo para feedback visual.
            self.label_estado.setStyleSheet("background-color: #FFEEEE; color: red; font-weight: bold; padding: 15px; border: 1px solid red;")
            return # Detiene la ejecución si hay un campo vacío.

        # 2. Se pasan todas as validacións (ÉXITO)
        self.label_estado.setText("Formulario enviado correctamente.")
        # Estilo para éxito: cambia el fondo y el color del texto a verde.
        self.label_estado.setStyleSheet("background-color: #EEFFEE; color: green; font-weight: bold; padding: 15px; border: 1px solid green;")

        # Después de un envío exitoso, es una buena práctica limpiar los campos.
        self.limpar_campos()


    def limpar_campos(self):
        """Método auxiliar para resetear los campos del formulario."""
        self.input_nome.clear() # Borra el contenido del campo Nombre.
        self.input_email.clear() # Borra el contenido del campo Email.
        self.input_mensaje.clear() # Borra el contenido del campo Mensaje.
        self.input_nome.setFocus() # Coloca el cursor en el campo Nombre.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormularioSimple()
    window.show()
    sys.exit(app.exec())