import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QMenuBar, QToolBar, QStatusBar,
    QCheckBox, QRadioButton,
    QPushButton, QLineEdit, QListWidget, QListWidgetItem,
    QTextEdit, QTabWidget, QSplitter, QGroupBox, QSlider,
    QComboBox, QLabel
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon

class InterfazCompleja(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WindowTitle")
        self.setGeometry(100, 100, 650, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget) # Layout principal: organiza los tres paneles principales verticalmente.

        # --- Panel Superior: QGroupBox "PanelCaption" ---
        self.panel_group_box = QGroupBox("PanelCaption")
        panel_layout = QVBoxLayout(self.panel_group_box)

        # QSplitter: Permite redimensionar las áreas Izquierda (Panel) y Derecha (Tabs)
        main_content_splitter = QSplitter(Qt.Horizontal)

        # 3. Panel Izquierdo (Lista + Radios + Botón)
        left_panel_box = QGroupBox("Panel")
        left_panel_layout = QVBoxLayout(left_panel_box)

        # Contenedor para Lista y RadioButtons
        list_radio_container = QHBoxLayout()
        self.list_items = QListWidget() # Lista de ítems
        for i in range(1, 6):
            QListWidgetItem(f"Item {i}", self.list_items)
        list_radio_container.addWidget(self.list_items)

        # RadioButtons
        radio_layout = QVBoxLayout()
        self.radio1 = QRadioButton("RadioButton1")
        self.radio2 = QRadioButton("RadioButton2")
        self.radio3 = QRadioButton("RadioButton3")
        self.radio4 = QRadioButton("InactiveRadio")
        self.radio4.setDisabled(True) # Simula estado inactivo
        radio_layout.addWidget(self.radio1)
        radio_layout.addWidget(self.radio2)
        radio_layout.addWidget(self.radio3)
        radio_layout.addWidget(self.radio4)
        radio_layout.addStretch()
        list_radio_container.addLayout(radio_layout)

        left_panel_layout.addLayout(list_radio_container)
        self.button = QPushButton("Button")
        left_panel_layout.addWidget(self.button) # Botón al final del panel izquierdo

        main_content_splitter.addWidget(left_panel_box)

        # 4. Panel Derecho (QTabWidget)
        self.tab_widget = QTabWidget()

        # Pestaña "SelectedTab" (con CheckBoxes y Slider)
        selected_tab = QWidget()
        selected_tab_layout = QVBoxLayout(selected_tab)
        self.check1 = QCheckBox("UncheckedCheckBox")
        self.check2 = QCheckBox("CheckedCheckBox")
        self.check2.setChecked(True)
        self.check3 = QCheckBox("InactiveCheckBox")
        self.check3.setDisabled(True) # Simula estado inactivo
        selected_tab_layout.addWidget(self.check1)
        selected_tab_layout.addWidget(self.check2)
        selected_tab_layout.addWidget(self.check3)
        self.slider = QSlider(Qt.Horizontal) # Control deslizante
        selected_tab_layout.addWidget(self.slider)
        selected_tab_layout.addStretch()

        self.tab_widget.addTab(selected_tab, "SelectedTab")
        self.tab_widget.addTab(QWidget(), "OtherTab")

        main_content_splitter.addWidget(self.tab_widget)
        panel_layout.addWidget(main_content_splitter)
        main_layout.addWidget(self.panel_group_box)

        # --- Panel Inferior ---
        bottom_panel_layout = QHBoxLayout() # Divide el área inferior en dos columnas.

        # Columna Izquierda Inferior (Campo de Contraseña y ComboBox)
        bottom_left = QVBoxLayout()
        bottom_left.addWidget(QLabel("TextField"))
        self.text_field = QLineEdit("••••••••••")
        self.text_field.setEchoMode(QLineEdit.Password) # Muestra el texto como puntos.
        bottom_left.addWidget(self.text_field)
        self.combo_box = QComboBox() # Lista desplegable
        self.combo_box.addItem("Item 1")
        self.combo_box.addItem("Item 2")
        bottom_left.addWidget(self.combo_box)
        bottom_left.addStretch()
        bottom_panel_layout.addLayout(bottom_left)

        # Columna Derecha Inferior (QTextEdit)
        bottom_right = QVBoxLayout()
        bottom_right.addWidget(QLabel("TextArea"))
        self.text_area = QTextEdit() # Área de texto multilínea
        bottom_right.addWidget(self.text_area)
        bottom_panel_layout.addLayout(bottom_right)

        main_layout.addLayout(bottom_panel_layout)

        # StatusBar y Menú/Toolbar (deben inicializarse después de la estructura principal)
        self.setStatusBar(QStatusBar(self))
        self._setup_menu_and_toolbar()

    def _setup_menu_and_toolbar(self):
        """Configura la barra de menú (QMenuBar) y la barra de herramientas (QToolBar)."""

        # --- Menu Bar ---
        menu_bar = QMenuBar()
        menu1 = menu_bar.addMenu("MenuWidget1")
        menu1.addAction(QAction("Opción 1", self))
        menu_bar.addMenu("MenuWidget2")
        self.setMenuBar(menu_bar)

        # --- Tool Bar ---
        tool_bar = QToolBar("Tool Bar")
        self.addToolBar(tool_bar)

        # Botones de la barra de herramientas (QAction y QCheckBox)
        tool_bar.addAction(QAction("ToolbarButton", self))
        tool_bar.addWidget(QCheckBox("ToolbarCheckBox")) # Widget incrustado en la toolbar


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InterfazCompleja()
    window.show()
    sys.exit(app.exec())