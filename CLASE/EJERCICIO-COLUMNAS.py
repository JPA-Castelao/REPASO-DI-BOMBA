import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtGui import QColor

class LayoutAnidadoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts Anidados (Morado y Rojo del Mismo Tamaño)")

        # --- FUNCIÓN UTILIDAD: Crea el Bloque de Color ---
        def create_block(color, stretch_factor=1):
            """Crea un QFrame simple con color de fondo y factor de estiramiento."""
            widget = QFrame()
            widget.setStyleSheet(f"background-color: {color};")
            return widget, stretch_factor

            # --- CONTENEDOR PRINCIPAL ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # LAYOUT PRINCIPAL: QHBoxLayout (Divide en 3 COLUMNAS de igual ancho)
        main_h_layout = QHBoxLayout(central_widget)

        # ------------------------------------------------
        # 1. Columna Izquierda (Anidada QVBoxLayout)
        # ------------------------------------------------

        left_v_layout = QVBoxLayout()

        # Tres bloques con factor 1: se reparten 1/3 de la altura cada uno
        block_red_L, stretch_red_L = create_block("red")
        left_v_layout.addWidget(block_red_L, stretch_red_L)

        block_yellow, stretch_yellow = create_block("yellow")
        left_v_layout.addWidget(block_yellow, stretch_yellow)

        block_purple_L, stretch_purple_L = create_block("purple")
        left_v_layout.addWidget(block_purple_L, stretch_purple_L)

        # ------------------------------------------------
        # 2. Columna Central (Verde Grande)
        # ------------------------------------------------

        # Factor de estiramiento horizontal 1
        block_green, stretch_green = create_block("green", stretch_factor=1)

        # ------------------------------------------------
        # 3. Columna Derecha (Anidada QVBoxLayout)
        # ------------------------------------------------

        right_v_layout = QVBoxLayout()

        # Bloque Rojo Superior: Factor 1 de altura
        block_red_R, stretch_red_R = create_block("red")
        right_v_layout.addWidget(block_red_R, stretch_red_R)

        # Bloque Morado Inferior: Factor 1 de altura
        block_purple_R, stretch_purple_R = create_block("purple", stretch_factor=1)
        right_v_layout.addWidget(block_purple_R, stretch_purple_R)

        # ------------------------------------------------
        # 4. Ensamblaje Final en el layout horizontal principal
        # ------------------------------------------------

        # Columna Izquierda: Factor 1 de ancho
        main_h_layout.addLayout(left_v_layout, 1)

        # Columna Central (Verde): Factor 1 de ancho
        main_h_layout.addWidget(block_green, stretch_green)

        # Columna Derecha: Factor 1 de ancho
        main_h_layout.addLayout(right_v_layout, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LayoutAnidadoApp()
    window.show()
    sys.exit(app.exec())