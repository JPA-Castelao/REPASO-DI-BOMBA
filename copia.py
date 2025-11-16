import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTabWidget, QGroupBox,
    QLineEdit, QTextEdit, QPushButton, QLabel, QListWidget,
    QSlider, QComboBox, QRadioButton, QCheckBox, QMessageBox, QStatusBar
)
from PySide6.QtCore import Qt
from datetime import datetime

class GuiaMaestraPySide6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guía Maestra: Estructura Final (Sin Menús)")
        self.setGeometry(100, 100, 950, 700)

        # ----------------------------------------------------------------------
        # 1. SETUP INICIAL: QTabWidget como Contenedor Central Principal
        # ----------------------------------------------------------------------

        # QTabWidget: Contenedor principal que se encuentra "arriba de todo"
        self.tab_contenedor_principal = QTabWidget()
        self.setCentralWidget(self.tab_contenedor_principal)

        # ----------------------------------------------------------------------
        # 2. PESTAÑA 1: Principal (Simple)
        # ----------------------------------------------------------------------

        page_bienvenida = QWidget()
        layout_bienvenida = QVBoxLayout(page_bienvenida)
        layout_bienvenida.addWidget(QLabel("Esta es la página de inicio. Usa la pestaña de al lado para la interfaz de control."))
        layout_bienvenida.addStretch()

        self.tab_contenedor_principal.addTab(page_bienvenida, "1. Inicio")

        # ----------------------------------------------------------------------
        # 3. PESTAÑA 2: Interfaz Compleja
        # ----------------------------------------------------------------------

        page_interfaz = QWidget()
        layout_interfaz = QVBoxLayout(page_interfaz)
        self.tab_contenedor_principal.addTab(page_interfaz, "2. Controles")

        # --- QSplitter (Divisor horizontal) ---
        self.main_splitter = QSplitter(Qt.Horizontal)
        layout_interfaz.addWidget(self.main_splitter)

        # --- PANEL IZQUIERDO ---
        panel_izquierdo = QGroupBox("Navegación y Listas")
        layout_izquierdo = QVBoxLayout(panel_izquierdo)

        self.lista_navegacion = QListWidget()
        layout_izquierdo.addWidget(QLabel("Datos Guardados:"))
        layout_izquierdo.addWidget(self.lista_navegacion)

        layout_izquierdo.addWidget(QLabel("\nSelección Exclusiva (Radio):"))
        self.radio_opcion_a = QRadioButton("Opción A")
        self.radio_opcion_b = QRadioButton("Opción B")
        self.radio_opcion_a.setChecked(True) #Por defecto
        layout_izquierdo.addWidget(self.radio_opcion_a)
        layout_izquierdo.addWidget(self.radio_opcion_b)

        layout_izquierdo.addStretch()
        self.main_splitter.addWidget(panel_izquierdo)

        # --- PANEL DERECHO (QTabWidget Anidado para Formulario/Log) ---
        self.tab_contenedor_anidado = QTabWidget()
        self.main_splitter.addWidget(self.tab_contenedor_anidado)

        # ----------------------------------------------------------------------
        # 4. PESTAÑAS ANIDADAS (Formulario y Log)
        # ----------------------------------------------------------------------

        # === PESTAÑA 1 ANIDADA: Formulario (Entrada de Datos) ===
        tab_formulario = QWidget()
        form_layout = QVBoxLayout(tab_formulario)

        self.input_nombre = QLineEdit()
        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(["Desarrollo", "Diseño", "Testing"])

        # QSlider y Feedback
        slider_group = QHBoxLayout()
        self.slider_valor = QSlider(Qt.Horizontal)
        self.slider_valor.setRange(1, 100)
        self.slider_valor.setValue(50)
        self.label_feedback = QLabel(f"Valor: 50")

        slider_group.addWidget(QLabel("Nivel (QSlider):"))
        slider_group.addWidget(self.slider_valor)
        slider_group.addWidget(self.label_feedback)

        self.check_activar = QCheckBox("Activar validación estricta")
        self.btn_guardar = QPushButton("Guardar en Lista y Registrar")
        self.btn_limpiar = QPushButton("Limpiar Registro de Log") # Nuevo botón directo

        # Añadir al Layout
        form_layout.addWidget(QLabel("Nombre (QLineEdit):")); form_layout.addWidget(self.input_nombre)
        form_layout.addWidget(QLabel("Categoría (QComboBox):")); form_layout.addWidget(self.combo_categoria)
        form_layout.addLayout(slider_group)
        form_layout.addWidget(self.check_activar)
        form_layout.addWidget(self.btn_guardar)
        form_layout.addWidget(self.btn_limpiar)
        form_layout.addStretch()

        self.tab_contenedor_anidado.addTab(tab_formulario, "Formulario (Entrada)")

        # === PESTAÑA 2 ANIDADA: Log (Salida de Datos) ===
        tab_log = QWidget()
        log_layout = QVBoxLayout(tab_log)
        self.output_log = QTextEdit()
        self.output_log.setReadOnly(True)
        log_layout.addWidget(QLabel("Registro de Log (QTextEdit):"))
        log_layout.addWidget(self.output_log)
        self.tab_contenedor_anidado.addTab(tab_log, "Log (Salida)")

        # ----------------------------------------------------------------------
        # 6. CONEXIONES (Signals -> Slots)
        # ----------------------------------------------------------------------

        # QSlider
        self.slider_valor.valueChanged.connect(self.actualizar_feedback_slider)

        # QPushButton/QLineEdit (Guardar)
        self.btn_guardar.clicked.connect(self.guardar_datos_completos)
        self.input_nombre.returnPressed.connect(self.guardar_datos_completos)

        # QPushButton (Limpiar) - Conectado directamente a su Slot
        self.btn_limpiar.clicked.connect(self.limpiar_log_slot)

        # QCheckBox
        self.check_activar.toggled.connect(self.slider_valor.setDisabled)

        # QRadioButton
        self.radio_opcion_a.toggled.connect(lambda checked: self.alternar_radio_estado("A", checked))
        self.radio_opcion_b.toggled.connect(lambda checked: self.alternar_radio_estado("B", checked))


    # ----------------------------------------------------------------------
    # 7. SLOTS (Lógica del Programa)
    # ----------------------------------------------------------------------

    def actualizar_feedback_slider(self, valor):
        """SLOT para QSlider: Muestra el valor actual."""
        self.label_feedback.setText(f"Valor: {valor}")
        self.statusBar().showMessage(f"Nivel seleccionado: {valor}")

    def alternar_radio_estado(self, opcion, checked):
        """SLOT para QRadioButton: Registra el cambio."""
        if checked:
            self.output_log.append(f"LOG: RadioButton '{opcion}' seleccionado.")

    def limpiar_log_slot(self):
        """SLOT para QPushButton: Borra el contenido del QTextEdit (Registro/Log)."""
        self.output_log.clear()
        self.statusBar().showMessage("El registro de log ha sido limpiado.")


    def guardar_datos_completos(self):
        """SLOT para QPushButton/QLineEdit: Lee, valida, registra y guarda en QListWidget."""

        nombre = self.input_nombre.text().strip()
        categoria = self.combo_categoria.currentText()
        slider_val = self.slider_valor.value()

        # 1. Validación Crítica
        if not nombre:
            QMessageBox.critical(self, "Error de Validación", "Debe introducir un nombre para el elemento.")
            return

        # 2. Lógica Condicional (QCheckBox)
        if self.check_activar.isChecked() and slider_val < 50:
            QMessageBox.warning(self, "Alerta", "Validación estricta: El nivel es menor a 50.")
            return

        # 3. Formato del ítem
        radio_seleccionada = "A" if self.radio_opcion_a.isChecked() else "B"
        timestamp = datetime.now().strftime("%H:%M:%S")

        item_guardado = f"[{timestamp} | {radio_seleccionada}] {nombre} ({categoria}) - Nivel: {slider_val}"

        # 4. Salida 1: Guardar en el QListWidget (Navegación y Listas)
        self.lista_navegacion.addItem(item_guardado)

        # 5. Salida 2: Registrar en el Log (QTextEdit)
        self.output_log.append(f"GUARDADO: {item_guardado}")

        # Limpiar y Mover
        self.input_nombre.clear()
        self.input_nombre.setFocus()
        self.tab_contenedor_anidado.setCurrentIndex(1) # Mueve a la pestaña de Log


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuiaMaestraPySide6()
    window.show()
    sys.exit(app.exec())