import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QGroupBox, QComboBox, QLineEdit,
    QPushButton, QVBoxLayout, QFormLayout
)


class ConnectionInputDock(QWidget):
    """UI panel for CFBW connection parameters."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CFBW Connection Designer")
        self._build_ui()

    def _build_ui(self):
        main_layout = QVBoxLayout(self)

        # Connection section
        connection_group = QGroupBox("Connection")
        conn_layout = QFormLayout()
        self.connectivity = QComboBox()
        self.connectivity.addItem("Column Flange-Beam Web")
        self.connectivity.setEnabled(False)

        self.primary_beam = QComboBox()
        self.primary_beam.addItems(["ISMB 200", "ISMB 250", "ISMB 300"])

        self.secondary_beam = QComboBox()
        self.secondary_beam.addItems(["ISMB 200", "ISMB 250", "ISMB 300"])

        self.material = QComboBox()
        self.material.addItems(["E250 Fe 410 W/A"])

        conn_layout.addRow("Connectivity", self.connectivity)
        conn_layout.addRow("Primary Beam", self.primary_beam)
        conn_layout.addRow("Secondary Beam", self.secondary_beam)
        conn_layout.addRow("Material", self.material)
        connection_group.setLayout(conn_layout)

        # Factored Loads
        load_group = QGroupBox("Factored Loads")
        load_layout = QFormLayout()
        self.shear_force = QLineEdit()
        self.axial_force = QLineEdit()
        load_layout.addRow("Shear Force (kN)", self.shear_force)
        load_layout.addRow("Axial Force (kN)", self.axial_force)
        load_group.setLayout(load_layout)

        # Bolt section
        bolt_group = QGroupBox("Bolt")
        bolt_layout = QFormLayout()
        self.diameter = QComboBox()
        self.diameter.addItems(["12", "16", "20"])
        self.bolt_type = QComboBox()
        self.bolt_type.addItems(["Bearing Bolt", "Friction Bolt"])
        self.property_class = QComboBox()
        self.property_class.addItems(["4.6", "8.8", "10.9"])
        bolt_layout.addRow("Diameter (mm)", self.diameter)
        bolt_layout.addRow("Type", self.bolt_type)
        bolt_layout.addRow("Property Class", self.property_class)
        bolt_group.setLayout(bolt_layout)

        # Plate section
        plate_group = QGroupBox("Plate")
        plate_layout = QFormLayout()
        self.plate_thickness = QComboBox()
        self.plate_thickness.addItems(["10", "12", "16"])
        plate_layout.addRow("Thickness (mm)", self.plate_thickness)
        plate_group.setLayout(plate_layout)

        # Design trigger
        self.design_button = QPushButton("Design")

        main_layout.addWidget(connection_group)
        main_layout.addWidget(load_group)
        main_layout.addWidget(bolt_group)
        main_layout.addWidget(plate_group)
        main_layout.addWidget(self.design_button)


def main():
    app = QApplication(sys.argv)
    window = ConnectionInputDock()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
