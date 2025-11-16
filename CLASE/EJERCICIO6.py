import sys
import random
import string
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QSlider
) # Importamos los widgets necesarios.
from PySide6.QtCore import Qt # Necesario para la alineación y la orientación del slider.

class GeneradorContrasenas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Contraseñas Aleatorias")
        self.setGeometry(100, 100, 450, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget) # Layout principal: organiza los elementos verticalmente.

        # ----------------------------------------------------------------------
        # --- 1. CONFIGURACIÓN DE LA LONGITUD (QSlider) ---
        # ----------------------------------------------------------------------

        # Etiqueta que muestra la longitud actual
        self.label_longitud = QLabel("Longitud: 12") # Texto inicial, coherente con el valor inicial del slider.
        self.label_longitud.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label_longitud)

        # Control deslizante (QSlider)
        self.slider_longitud = QSlider(Qt.Horizontal) # Orientación horizontal.
        self.slider_longitud.setMinimum(6) # Longitud mínima (6 caracteres).
        self.slider_longitud.setMaximum(20) # Longitud máxima (20 caracteres).
        self.slider_longitud.setValue(12) # Valor inicial.
        self.slider_longitud.setSingleStep(1)
        self.slider_longitud.setTickInterval(2) # Define el intervalo de las marcas.
        self.slider_longitud.setTickPosition(QSlider.TicksBelow) # Muestra las marcas debajo del slider.

        # CONEXIÓN DEL SLIDER: Llama a un método cada vez que se mueve.
        self.slider_longitud.valueChanged.connect(self.actualizar_etiqueta_longitud)
        main_layout.addWidget(self.slider_longitud)

        main_layout.addSpacing(15)

        # ----------------------------------------------------------------------
        # --- 2. MOSTRAR LA CONTRASEÑA ---
        # ----------------------------------------------------------------------

        output_container = QHBoxLayout() # Contenedor horizontal para la etiqueta y el campo de texto.

        # Etiqueta de título
        output_container.addWidget(QLabel("Contraseña generada:"))

        # Cuadro de texto para mostrar la contraseña
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setReadOnly(True) # ¡Importante! Hace el campo de solo lectura.
        self.input_contrasena.setStyleSheet("font-size: 14px; padding: 5px;")

        output_container.addWidget(self.input_contrasena)
        main_layout.addLayout(output_container)

        main_layout.addSpacing(15)

        # ----------------------------------------------------------------------
        # --- 3. BOTÓN DE GENERACIÓN ---
        # ----------------------------------------------------------------------

        self.btn_generar = QPushButton("Generar nueva contraseña")
        self.btn_generar.setStyleSheet("padding: 10px; font-weight: bold;")

        # CONEXIÓN DEL BOTÓN: Llama al método que realiza la generación.
        self.btn_generar.clicked.connect(self.generar_y_mostrar_contrasena)
        main_layout.addWidget(self.btn_generar)

        # Estado inicial: Generar una contraseña al iniciar la aplicación.
        self.generar_y_mostrar_contrasena()

    # ----------------------------------------------------------------------
    # --- MÉTODOS SLOTS (Conectados a señales de Widgets) ---
    # ----------------------------------------------------------------------

    def actualizar_etiqueta_longitud(self, valor):
        """
        Se activa con la señal 'valueChanged' del QSlider.
        Actualiza el texto de la etiqueta con la longitud seleccionada.
        """
        self.label_longitud.setText(f"Longitud: {valor}")

    def generar_y_mostrar_contrasena(self):
        """
        Se activa con la señal 'clicked' del QPushButton.
        Obtiene la longitud, genera la contraseña y la muestra en el QLineEdit.
        """
        # 1. Obtener la longitud seleccionada por el usuario (el valor actual del slider).
        longitud = self.slider_longitud.value()

        # 2. Generar la contraseña aleatoria.
        contrasena = self._generar_contrasena_logica(longitud)

        # 3. Mostrar el resultado.
        self.input_contrasena.setText(contrasena)

    # ----------------------------------------------------------------------
    # --- LÓGICA DE NEGOCIO (Función auxiliar) ---
    # ----------------------------------------------------------------------

    def _generar_contrasena_logica(self, longitud):
        """
        Implementa la lógica para generar una contraseña fuerte.
        Asegura que la contraseña contenga al menos un carácter de cada tipo (letras, dígitos, símbolos).
        """
        # Definir el conjunto de caracteres permitido.
        caracteres = (
                string.ascii_letters +   # Letras (a-z y A-Z)
                string.digits +          # Dígitos (0-9)
                string.punctuation       # Símbolos (!@#$%^...)
        )

        # 1. Asegurar la presencia de al menos uno de cada tipo (garantiza una contraseña fuerte):
        pwd = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # 2. Rellenar el resto de la longitud con caracteres aleatorios:
        long_restante = longitud - len(pwd)
        pwd.extend(random.choice(caracteres) for _ in range(long_restante))

        # 3. Mezclar (shuffle) la lista para que la posición de los caracteres sea aleatoria:
        random.shuffle(pwd)

        # 4. Devolver como una cadena de texto.
        return "".join(pwd)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeneradorContrasenas()
    window.show()
    sys.exit(app.exec())