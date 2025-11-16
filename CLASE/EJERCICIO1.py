import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QPushButton, QRadioButton, QCheckBox, QLabel
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class ExercicioCoherencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio 1: Coherencia Simple (Ajustado al Enunciado)")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # --- CREACIÓN DOS CONTROIS ---
        control_widget = QWidget()
        self.control_layout = QVBoxLayout(control_widget)

        # Botóns
        self.control_layout.addWidget(QLabel("1. QPushButton"))
        self.btn_verde = QPushButton("Ir a Verde")
        self.btn_azul = QPushButton("Ir a Azul")
        self.control_layout.addWidget(self.btn_verde)
        self.control_layout.addWidget(self.btn_azul)

        # RadioButtons (Selección exclusiva)
        self.control_layout.addWidget(QLabel("\n2. QRadioButton (Exclusivo)"))
        self.radio_verde = QRadioButton("Páxina Verde")
        self.radio_azul = QRadioButton("Páxina Azul")
        self.control_layout.addWidget(self.radio_verde)
        self.control_layout.addWidget(self.radio_azul)

        # CheckBoxes (Solo Verde y Azul para coherencia simple)
        self.control_layout.addWidget(QLabel("\n3. QCheckBox (Coherencia Simple)"))
        self.check_verde = QCheckBox("Páxina Verde")
        self.check_azul = QCheckBox("Páxina Azul")
        self.control_layout.addWidget(self.check_verde)
        self.control_layout.addWidget(self.check_azul)
        self.control_layout.addStretch()

        main_layout.addWidget(control_widget)

        # --- QStackedLayout (Páxinas de Contido) ---
        self.stacked_layout = QStackedLayout()
        self.page_verde = self._create_page("Páxina VERDE", "green")
        self.page_azul = self._create_page("Páxina AZUL", "blue")

        self.stacked_layout.addWidget(self.page_verde) # Índice 0
        self.stacked_layout.addWidget(self.page_azul)  # Índice 1

        stacked_container = QWidget()
        stacked_container.setLayout(self.stacked_layout)
        main_layout.addWidget(stacked_container)

        # --- CONEXIÓN DE SINAIS (SINAIS E SLOTS) ---

        # 1. Botóns
        self.btn_verde.clicked.connect(lambda: self.update_coherence("green", 0))
        self.btn_azul.clicked.connect(lambda: self.update_coherence("blue", 1))

        # 2. RadioButtons
        self.radio_verde.toggled.connect(lambda checked: self.handle_radio_change("green", checked))
        self.radio_azul.toggled.connect(lambda checked: self.handle_radio_change("blue", checked))

        # 3. CheckBoxes (Simplificamos la lógica a una sola función)
        self.check_verde.stateChanged.connect(lambda state: self.handle_check_change("green", state))
        self.check_azul.stateChanged.connect(lambda state: self.handle_check_change("blue", state))

        # Estado Inicial
        self.update_coherence("green", 0)

    # --- MÉTODOS DE UTILIDADE ---

    def _create_page(self, name, color_name):
        """Función auxiliar para crear las páginas."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(name))
        self.apply_background_color(widget, QColor(color_name))
        return widget

    def apply_background_color(self, widget, qcolor):
        """Aplica el color de fondo usando CSS (StyleSheets)."""
        color_string = f"rgb({qcolor.red()}, {qcolor.green()}, {qcolor.blue()})"
        widget.setStyleSheet(f"background-color: {color_string};")

    # ----------------------------------------------------------------------
    # --- LÓXICA CENTRAL: UPDATE_COHERENCE (LA COHERENCIA) ---
    # ----------------------------------------------------------------------

    def update_coherence(self, color_name, index):
        """
        FUNCIÓN MESTRA: Sincroniza TODOS los controles (Botones, Radios, Checks)
        a la opción simple seleccionada (Verde o Azul).
        """
        # 1. Cambiar la página y color
        self.stacked_layout.setCurrentIndex(index)
        widget = self.stacked_layout.currentWidget()
        self.apply_background_color(widget, QColor(color_name))

        # 2. Sincronizar RadioButtons (Bloquear para evitar recurrencia)
        self.radio_verde.blockSignals(True)
        self.radio_azul.blockSignals(True)
        self.radio_verde.setChecked(color_name == "green")
        self.radio_azul.setChecked(color_name == "blue")
        self.radio_verde.blockSignals(False)
        self.radio_azul.blockSignals(False)

        # 3. Sincronizar CheckBoxes (Bloquear para evitar recurrencia)
        self.check_verde.blockSignals(True)
        self.check_azul.blockSignals(True)

        # En el CheckBox, solo se debe marcar la opción correspondiente
        self.check_verde.setChecked(color_name == "green")
        self.check_azul.setChecked(color_name == "blue")

        self.check_verde.blockSignals(False)
        self.check_azul.blockSignals(False)


    def handle_radio_change(self, color_name, checked):
        """
        SLOT para QRadioButton: Solo actúa si se ha marcado (toggled=True) y llama a la coherencia.
        """
        if checked:
            if color_name == "green":
                self.update_coherence("green", 0)
            elif color_name == "blue":
                self.update_coherence("blue", 1)

    def handle_check_change(self, color_name, state):
        """
        SLOT para QCheckBox: Asegura que al marcar un CheckBox, se mantenga la coherencia.
        Nota: Esto asegura que el CheckBox funcione como el Botón y el RadioButton.
        """
        # Si se MARCA (state == Qt.Checked)
        if state == Qt.Checked:
            if color_name == "green":
                # Si marco Checkbox Verde, voy a la coherencia Verde
                self.update_coherence("green", 0)
            elif color_name == "blue":
                # Si marco Checkbox Azul, voy a la coherencia Azul
                self.update_coherence("blue", 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExercicioCoherencia()
    window.show()
    sys.exit(app.exec())