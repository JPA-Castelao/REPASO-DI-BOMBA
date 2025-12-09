import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QLabel, QSlider, QComboBox, QGroupBox
)
from PyQt6.QtCore import Qt


class ControlesAvanzados(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listas: Controles avanzados")
        self.setGeometry(100, 100, 700, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # PANEL DE ENTRADA DE DATOS (GroupBox para agrupar)
        input_group = QGroupBox("Añadir nueva tarea:")
        input_layout = QVBoxLayout(input_group)

        # Entrada de texto:
        input_layout.addWidget(QLabel("Nombre de la tarea:"))
        self.input_tarea = QLineEdit()
        input_layout.addWidget(self.input_tarea)

        # QComboBox ( selector desplegable )
        selector_layout = QHBoxLayout()
        selector_layout.addWidget(QLabel("Prioridad:"))
        self.combo_prioridad = QComboBox()
        self.combo_prioridad.addItems(["Alta", "Media", "Baja"])
        selector_layout.addWidget(self.combo_prioridad)

        selector_layout.addStretch()

        # QSilder
        selector_layout.addWidget(QLabel("Tiempo estimado (horas): "))
        # self.slider_tiempo = QSlider(Qt.Horizontal)
        self.slider_tiempo = QSlider(Qt.Orientation.Horizontal)
        self.slider_tiempo.setMinimum(1)
        self.slider_tiempo.setMaximum(20)
        self.slider_tiempo.setValue(10)

        self.label_tiempo = QLabel(f"{self.slider_tiempo.value()}h")
        self.label_tiempo.setFixedWidth(30)

        selector_layout.addWidget(self.slider_tiempo)
        selector_layout.addWidget(self.label_tiempo)

        input_layout.addLayout(selector_layout)

        # Boton de añadir y mensaje de texto
        self.btn_anadir = QPushButton("Añadir")
        input_layout.addWidget(self.btn_anadir)

        main_layout.addWidget(input_group)

        # Panel de lista ( QListWidget )
        main_layout.addWidget(QLabel("Tareas del proyecto:"))
        self.list_proyecto = QListWidget()
        main_layout.addWidget(self.list_proyecto)

        self.btn_eliminar = QPushButton("Eliminar Tarea selecionada")
        main_layout.addWidget(self.btn_eliminar)

        # Conexiones

        # Slider
        self.slider_tiempo.valueChanged.connect(self.actualizar_tiempo)

        # Botones y entrada de texto
        self.btn_anadir.clicked.connect(self.añadir_tarea)
        self.input_tarea.returnPressed.connect(self.añadir_tarea)
        self.btn_eliminar.clicked.connect(self.eliminar_tarea)

        # Slots

    def actualizar_tiempo(self, valor_recibido):
        self.label_tiempo.setText(f"{valor_recibido}h")

    def añadir_tarea(self):
        nombre_tarea = self.input_tarea.text().strip()
        if not nombre_tarea:
            return

        # Obtener valores de los controles avanzados:
        prioridad = self.combo_prioridad.currentText()
        tiempo = self.slider_tiempo.value()

        # Formato del ítem que se verá en la lista
        item_final = f"[{prioridad}] Tarea: {nombre_tarea} ({tiempo}h)"

        self.list_proyecto.addItem(item_final)

        # Limpiar y resetear
        self.input_tarea.clear()
        self.slider_tiempo.setValue(10)
        self.combo_prioridad.setCurrentIndex(0)
        self.input_tarea.setFocus()

    def eliminar_tarea(self):
        items_a_eliminar = self.list_proyecto.selectedItems()

        if not items_a_eliminar:
            return

        for item in items_a_eliminar:
            self.list_proyecto.takeItem(self.list_proyecto.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlesAvanzados()
    window.show()
    sys.exit(app.exec())
