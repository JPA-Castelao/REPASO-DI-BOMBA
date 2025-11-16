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
        self.setWindowTitle("Exercicio 1: Radio Exclusivo + Check RGB")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # --- CREACIÓN DOS CONTROIS ---
        control_widget = QWidget()
        self.control_layout = QVBoxLayout(control_widget)

        # Botóns (Simples)
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

        # CheckBoxes (Lógica RGB)
        self.control_layout.addWidget(QLabel("\n3. QCheckBox (Combinación RGB)"))
        self.check_vermello = QCheckBox("Vermello (R)")
        self.check_verde = QCheckBox("Verde (G)")
        self.check_azul = QCheckBox("Azul (B)")
        self.control_layout.addWidget(self.check_vermello)
        self.control_layout.addWidget(self.check_verde)
        self.control_layout.addWidget(self.check_azul)
        self.control_layout.addStretch()

        main_layout.addWidget(control_widget)

        # --- QStackedLayout (Páxinas de Contido) ---
        self.stacked_layout = QStackedLayout()
        # Creamos unha terceira páxina 'RGB' para as combinacións
        self.page_verde = self._create_page("Páxina VERDE", "green")
        self.page_azul = self._create_page("Páxina AZUL", "blue")

        self.stacked_layout.addWidget(self.page_verde) # Índice 0
        self.stacked_layout.addWidget(self.page_azul)  # Índice 1

        stacked_container = QWidget()
        stacked_container.setLayout(self.stacked_layout)
        main_layout.addWidget(stacked_container)

        # --- CONEXIÓN DE SINAIS (SINAIS E SLOTS) ---

        # 1. Botóns: Sincronizan coa lóxica de Coherencia Simple
        self.btn_verde.clicked.connect(lambda: self.update_coherence_simple("green", 0))
        self.btn_azul.clicked.connect(lambda: self.update_coherence_simple("blue", 1))

        # 2. RadioButtons: Chaman ao xestor de exclusividade
        self.radio_verde.toggled.connect(lambda checked: self.handle_radio_change("green", checked))
        self.radio_azul.toggled.connect(lambda checked: self.handle_radio_change("blue", checked))

        # 3. CheckBoxes: Chaman ao xestor de combinación RGB
        self.check_vermello.stateChanged.connect(self.handle_check_change_rgb)
        self.check_verde.stateChanged.connect(self.handle_check_change_rgb)
        self.check_azul.stateChanged.connect(self.handle_check_change_rgb)

        # Estado Inicial
        self.update_coherence_simple("green", 0)

    # --- MÉTODOS ---

    def _create_page(self, name, color_name):
        """Función auxiliar para crear las páxinas."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(name))
        self.apply_background_color(widget, QColor(color_name))
        return widget

    def apply_background_color(self, widget, qcolor):
        """Aplica la cor de fondo usando CSS"""
        color_string = f"rgb({qcolor.red()}, {qcolor.green()}, {qcolor.blue()})"
        widget.setStyleSheet(f"background-color: {color_string};")

    # ----------------------------------------------------------------------
    # --- LÓXICA 1: COHERENCIA SIMPLE (BOTÓNS E RADIOBUTTONS) ---
    # ----------------------------------------------------------------------

    def update_coherence_simple(self, color_name, index):
        """
        FUNCIÓN MESTRA: Sincroniza os BOTÓNS, RADIOBUTTONS e a PÁXINA.
        Os Checkboxes serán actualizados de forma simple.
        """
        # 1. Cambiar a páxina e aplicar a cor
        self.stacked_layout.setCurrentIndex(index)
        widget = self.stacked_layout.currentWidget()
        self.apply_background_color(widget, QColor(color_name))

        # 2. Sincronizar RadioButtons (Exclusivo)
        self.radio_verde.blockSignals(True)
        self.radio_azul.blockSignals(True)
        self.radio_verde.setChecked(color_name == "green")
        self.radio_azul.setChecked(color_name == "blue")
        self.radio_verde.blockSignals(False)
        self.radio_azul.blockSignals(False)

        # 3. Sincronizar CheckBoxes (Para que reflictan o cambio simple)
        self.check_vermello.blockSignals(True)
        self.check_verde.blockSignals(True)
        self.check_azul.blockSignals(True)

        # Só marcamos a cor pura (o vermello desmáracase)
        self.check_vermello.setChecked(False)
        self.check_verde.setChecked(color_name == "green")
        self.check_azul.setChecked(color_name == "blue")

        self.check_vermello.blockSignals(False)
        self.check_verde.blockSignals(False)
        self.check_azul.blockSignals(False)


    def handle_radio_change(self, color_name, checked):
        """
        SLOT para QRadioButton: Chama ao sincronizador de coherencia simple.
        """
        if checked:
            if color_name == "green":
                self.update_coherence_simple("green", 0)
            elif color_name == "blue":
                self.update_coherence_simple("blue", 1)

    # ----------------------------------------------------------------------
    # --- LÓXICA 2: COMBINACIÓN RGB (CHECKBOXES) ---
    # ----------------------------------------------------------------------

    def handle_check_change_rgb(self):
        """
        SLOT para QCheckBox: Calcula a cor RGB, aplica o fondo e desmarca os RadioButtons.
        (NON actualiza os RadioButtons, pois a lóxica é RGB, non exclusiva).
        """
        widget = self.stacked_layout.currentWidget()

        # 1. Obter estados e calcular a cor RGB
        is_red = self.check_vermello.isChecked()
        is_green = self.check_verde.isChecked()
        is_blue = self.check_azul.isChecked()
        count = sum([is_red, is_green, is_blue])

        r, g, b = 0, 0, 0
        if count == 0:
            r, g, b = 255, 255, 255
        elif count == 3:
            r, g, b = 0, 0, 0
        else:

            if is_red: r = 255
            if is_green: g = 255
            if is_blue: b = 255

        # Aplicar a cor resultante
        self.apply_background_color(widget, QColor(r, g, b))

        # 2. Sincronización Inversa (Desmarcar RadioButtons)
        # Ao usar o CheckBox (RGB), os RadioButtons DEBEN desmarcarse,
        self.radio_verde.blockSignals(True)
        self.radio_azul.blockSignals(True)
        self.radio_verde.setChecked(False)
        self.radio_azul.setChecked(False)
        self.radio_verde.blockSignals(False)
        self.radio_azul.blockSignals(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExercicioCoherencia()
    window.show()
    sys.exit(app.exec())