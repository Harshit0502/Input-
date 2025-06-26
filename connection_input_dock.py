import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGroupBox,
    QComboBox,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout,
    QMenu,
    QAction,
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class ConnectionInputDock(QWidget):
    """Widget representing the connection input dock."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()

    def _build_ui(self):
        self.setWindowTitle("Connection Input Dock")

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # --- Top Section: Input Dock Bar ---
        top_bar = QHBoxLayout()
        self.input_dock_btn = QPushButton("Input Dock")
        self.input_dock_btn.setStyleSheet("background-color: #6da53f; color: white; border-radius: 4px;")

        self.additional_btn = QPushButton("Additional Inputs")
        menu = QMenu(self.additional_btn)
        menu.addAction(QAction("Assumptions", self))
        menu.addAction(QAction("Preferences", self))
        self.additional_btn.setMenu(menu)

        top_bar.addWidget(self.input_dock_btn)
        top_bar.addWidget(self.additional_btn)
        top_bar.addStretch()
        main_layout.addLayout(top_bar)

        # --- Section 1: Connection ---
        conn_group = QGroupBox("Connection")
        conn_layout = QFormLayout()
        self.connectivity = QComboBox()
        self.connectivity.addItems(
            [
                "Column Flange-Beam Web",
                "Column Web-Beam Web",
                "Column Flange-Beam Flange",
                "Column Web-Beam Flange",
            ]
        )
        self.primary_beam = QComboBox()
        self.primary_beam.addItem("Select Section")
        self.secondary_beam = QComboBox()
        self.secondary_beam.addItem("Select Section")
        self.material = QComboBox()
        self.material.addItem("E 250 (Fe 410 W)A")

        conn_layout.addRow(QLabel("Connectivity *"), self.connectivity)
        conn_layout.addRow(QLabel("Primary Beam *"), self.primary_beam)
        conn_layout.addRow(QLabel("Secondary Beam *"), self.secondary_beam)
        conn_layout.addRow(QLabel("Material *"), self.material)
        conn_group.setLayout(conn_layout)
        main_layout.addWidget(conn_group)

        # --- Section 2: Factored Loads ---
        load_group = QGroupBox("Factored Loads")
        load_layout = QFormLayout()
        self.shear_force = QLineEdit()
        self.shear_force.setPlaceholderText("ex. 10 kN")
        self.axial_force = QLineEdit()
        self.axial_force.setPlaceholderText("ex. 10 kN")
        load_layout.addRow(QLabel("Shear Force"), self.shear_force)
        load_layout.addRow(QLabel("Axial Force"), self.axial_force)
        load_group.setLayout(load_layout)
        main_layout.addWidget(load_group)

        # --- Section 3: Bolt ---
        bolt_group = QGroupBox("Bolt")
        bolt_layout = QFormLayout()
        self.bolt_diameter = QComboBox()
        self.bolt_diameter.addItem("All")
        self.bolt_type = QComboBox()
        self.bolt_type.addItem("Bearing Bolt")
        self.property_class = QComboBox()
        self.property_class.addItem("All")
        bolt_layout.addRow(QLabel("Diameter (mm)"), self.bolt_diameter)
        bolt_layout.addRow(QLabel("Type *"), self.bolt_type)
        bolt_layout.addRow(QLabel("Property Class (mm)*"), self.property_class)
        bolt_group.setLayout(bolt_layout)
        main_layout.addWidget(bolt_group)

        # --- Section 4: Plate ---
        plate_group = QGroupBox("Plate")
        plate_layout = QFormLayout()
        self.plate_thickness = QComboBox()
        self.plate_thickness.addItem("All")
        plate_layout.addRow(QLabel("Thickness (mm) *"), self.plate_thickness)
        plate_group.setLayout(plate_layout)
        main_layout.addWidget(plate_group)

        # --- Bottom Action ---
        self.design_btn = QPushButton("Design")
        self.design_btn.setStyleSheet(
            "background-color: #6da53f; color: white; border-radius: 6px; padding: 6px 12px;"
        )
        main_layout.addWidget(self.design_btn, alignment=Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ConnectionInputDock()
    widget.show()
    sys.exit(app.exec())
