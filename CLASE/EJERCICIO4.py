import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from datetime import datetime


class CalculadoraEdad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de edad")
        self.setGeometry(100, 100, 400, 250)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        main_layout = QVBoxLayout(widget_central)

        # --- ELEMENTOS DE ENTRADA Y SALIDA ---

        # Campo de entrada del año de nacimiento
        entrada_group = QWidget()
        entrada_layout = QHBoxLayout(entrada_group)

        self.label_ano = QLabel("Año de nacimiento: ")
        self.input_ano = QLineEdit()

        entrada_layout.addWidget(self.label_ano)
        entrada_layout.addWidget(self.input_ano)
        main_layout.addWidget(entrada_group)

        # Etiqueta del resultado
        self.label_resultado = QLabel("Introduce tu año y pulsa calcular.")
        self.label_resultado.setAlignment(Qt.AlignCenter)
        self.label_resultado.setStyleSheet("font-weight: bold; padding: 10px;")
        main_layout.addWidget(self.label_resultado)

        # Etiqueta de error (inicialmente vacía)
        self.label_erro = QLabel("")
        self.label_erro.setAlignment(Qt.AlignCenter)

        # INICIALIZACIÓN DE ESTILO (Reemplaza a la llamada _set_error_style(False))
        self.label_erro.setStyleSheet("color: black; font-weight: normal;")

        main_layout.addWidget(self.label_erro)

        # --- BOTONES ---
        btn_group = QWidget()
        btn_layout = QHBoxLayout(btn_group)

        self.btn_calcular = QPushButton("Calcular edad")
        self.btn_limpiar = QPushButton("Limpiar")

        btn_layout.addWidget(self.btn_calcular)
        btn_layout.addWidget(self.btn_limpiar)
        main_layout.addWidget(btn_group)

        main_layout.addStretch()

        # --- CONEXION DE SEÑALES ---

        self.btn_calcular.clicked.connect(self.calcular_y_mostrar_edad)
        self.btn_limpiar.clicked.connect(self.limpiar_interfaz)


    # --- MÉTODOS DE LÓGICA ---

    def limpiar_interfaz(self):
        """Borra el campo de texto y restablece las etiquetas."""
        self.input_ano.clear()
        self.label_resultado.setText("Introduce tu año y pulsa calcular.")
        self.label_erro.setText("")
        # CÓDIGO DIRECTO: Restablecer estilo (Reemplaza a _set_error_style(False))
        self.label_erro.setStyleSheet("color: black; font-weight: normal;")
        self.input_ano.setFocus()


    def calcular_y_mostrar_edad(self):
        # Lógica de validación:
        ano_texto = self.input_ano.text().strip()
        self.label_erro.setText("")
        # Restablecer estilo al inicio del cálculo
        self.label_erro.setStyleSheet("color: black; font-weight: normal;")

        # Validar si está vacío (además del try-except)
        if not ano_texto:
            self.label_erro.setText("Error: El campo no puede estar vacío.")
            self.label_erro.setStyleSheet("color: red; font-weight: bold;") # ESTILO ROJO
            self.label_resultado.setText("")
            return

        try:
            ano_nacimiento = int(ano_texto)
            ano_actual = datetime.now().year

            #  Validar rango
            if not (1900 <= ano_nacimiento <= ano_actual):
                self.label_erro.setText(f"Error: El año {ano_nacimiento} no es válido.")
                self.label_erro.setStyleSheet("color: red; font-weight: bold;") # ESTILO ROJO
                self.label_resultado.setText("")
                return

            edad = ano_actual - ano_nacimiento
            self.label_resultado.setText(f"Tu edad es: **{edad} años**")

        except ValueError:
            self.label_erro.setText(f"Error: '{ano_texto}' no es un número válido.")
            self.label_erro.setStyleSheet("color: red; font-weight: bold;") # ESTILO ROJO
            self.label_resultado.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraEdad()
    window.show()
    sys.exit(app.exec())