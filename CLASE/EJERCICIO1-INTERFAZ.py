import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLabel, QLayout
)
from PySide6.QtCore import Qt

class GestorHojasQT(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Hojas")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        #  Contenedor Principal de Listas y Botones
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # 1. Lista de Hojas Visibles (Izquierda)
        listas_visibles_layout = QVBoxLayout()
        listas_visibles_layout.addWidget(QLabel("Hojas visibles"))
        self.lstVisibles = QListWidget()
        listas_visibles_layout.addWidget(self.lstVisibles)
        content_layout.addLayout(listas_visibles_layout)

        # Contenedor de Botones (Centro)
        botones_layout = QVBoxLayout()
        botones_layout.addStretch() # Espaciador superior

        # Botón Ocultar
        self.btnOcultar = QPushButton("Ocultar >>")
        botones_layout.addWidget(self.btnOcultar)

        # Botón Mostrar
        self.btnMostrar = QPushButton("<< Mostrar")
        botones_layout.addWidget(self.btnMostrar)

        botones_layout.addStretch() # Espaciador inferior
        content_layout.addLayout(botones_layout)

        # Lista de Hojas Ocultas (Derecha)
        listas_ocultas_layout = QVBoxLayout()
        listas_ocultas_layout.addWidget(QLabel("Hojas ocultas"))
        self.lstOcultas = QListWidget()
        listas_ocultas_layout.addWidget(self.lstOcultas)
        content_layout.addLayout(listas_ocultas_layout)

        # --- Botón Cerrar (Parte inferior) ---

        # Contenedor para alinear el botón 'Cerrar' a la derecha
        cerrar_container = QHBoxLayout()
        cerrar_container.addStretch()
        self.btnCerrar = QPushButton("Cerrar")
        self.btnCerrar.setFixedWidth(100) # Tamaño fijo para el botón
        cerrar_container.addWidget(self.btnCerrar)

        main_layout.addLayout(cerrar_container)

        # --- Lógica Inicial y Conexiones ---
        self._cargar_datos_simulados()
        self._conectar_senales()


    def _cargar_datos_simulados(self):
        """Simula la carga inicial de hojas de Excel."""

        # Hojas Visibles simuladas
        for i in range(4, 7):
            self.lstVisibles.addItem(f"Hoja{i}")

        # Hojas Ocultas simuladas
        for i in range(1, 4):
            self.lstOcultas.addItem(f"Hoja{i}")


    def _conectar_senales(self):
        """Conecta los botones a los métodos de movimiento y cierre."""

        # Conexión principal de los botones de acción
        self.btnOcultar.clicked.connect(self.mover_a_ocultas)
        self.btnMostrar.clicked.connect(self.mover_a_visibles)

        # Conexión del botón de cierre
        self.btnCerrar.clicked.connect(self.close)


    def mover_a_ocultas(self):
        """Mueve los ítems seleccionados de 'Visibles' a 'Ocultas' (simulación de ocultar)."""

        # Obtenemos los ítems seleccionados de la lista de origen (lstVisibles)
        items_a_mover = self.lstVisibles.selectedItems()

        if not items_a_mover:
            return # No hacemos nada si no hay selección.

        for item in items_a_mover:
            # Añadir el ítem a la lista de destino (lstOcultas)
            self.lstOcultas.addItem(item.text())

            # Eliminar el ítem de la lista de origen (lstVisibles)
            self.lstVisibles.takeItem(self.lstVisibles.row(item))


    def mover_a_visibles(self):
        """Mueve los ítems seleccionados de 'Ocultas' a 'Visibles' (simulación de mostrar)."""

        # Obtenemos los ítems seleccionados de la lista de origen (lstOcultas)
        items_a_mover = self.lstOcultas.selectedItems()

        if not items_a_mover:
            return # No hacemos nada si no hay selección.

        for item in items_a_mover:
            # Añadir el ítem a la lista de destino (lstVisibles)
            self.lstVisibles.addItem(item.text())

            # Eliminar el ítem de la lista de origen (lstOcultas)
            self.lstOcultas.takeItem(self.lstOcultas.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestorHojasQT()
    window.show()
    sys.exit(app.exec())