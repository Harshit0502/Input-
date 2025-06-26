# New PySide6 UI interface for structural connection design

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QComboBox,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QFrame,
    QFormLayout,
    QStyle,
)


class ConnectionDesignWidget(QWidget):
    """Main widget containing the connection design form."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()

    def _build_ui(self):
        self.setWindowTitle("Structural Connection Designer")

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # --- Top Bar ---
        top_bar = QVBoxLayout()
        bar_row = QHBoxLayout()
        self.input_dock_btn = QPushButton("Input Dock")
        self.input_dock_btn.setStyleSheet("background-color: #015a01; color: white; padding: 4px 10px;")

        self.additional_btn = QPushButton("Additional Inputs")
        self.additional_btn.setStyleSheet("background-color: #a8d5a8; padding: 4px 6px;")
        self.additional_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowDown))
        self.close_additional_btn = QPushButton("×")
        self.close_additional_btn.setStyleSheet("background-color: #a8d5a8; padding: 4px;")

        bar_row.addWidget(self.input_dock_btn)
        bar_row.addWidget(self.additional_btn)
        bar_row.addWidget(self.close_additional_btn)
        bar_row.addStretch()

        additional_opts = QHBoxLayout()
        self.assumptions_btn = QPushButton("Assumptions")
        self.assumptions_btn.setStyleSheet("background-color: #a8d5a8; padding: 2px 4px;")
        self.preferences_btn = QPushButton("Preferences")
        self.preferences_btn.setStyleSheet("background-color: #a8d5a8; padding: 2px 4px;")
        additional_opts.addWidget(self.assumptions_btn)
        additional_opts.addWidget(self.preferences_btn)
        additional_opts.addStretch()

        top_bar.addLayout(bar_row)
        top_bar.addLayout(additional_opts)
        main_layout.addLayout(top_bar)

        # --- Section 1: Connection ---
        connection_box = QGroupBox("Connection")
        connection_box.setStyleSheet(
            "QGroupBox { background-color: #a8d5a8; border: 1px solid #79b279; margin-top: 0.5em; }" \
            "QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }"
        )
        conn_layout = QVBoxLayout()

        conn_layout.addWidget(QLabel("Connectivity *"))
        self.conn_list = QListWidget()
        for i in range(4):
            item = QListWidgetItem(f"Column Flange-Beam Web  ×")
            self.conn_list.addItem(item)
        conn_layout.addWidget(self.conn_list)

        self.diagram_label = QLabel("[Connection Diagram]")
        self.diagram_label.setAlignment(Qt.AlignCenter)
        conn_layout.addWidget(self.diagram_label)

        form = QFormLayout()
        self.primary_beam = QComboBox()
        self.primary_beam.addItem("Select Section")
        form.addRow("Primary Beam *", self.primary_beam)

        self.secondary_beam = QComboBox()
        self.secondary_beam.addItem("Select Section")
        form.addRow("Secondary Beam *", self.secondary_beam)

        self.material = QComboBox()
        self.material.addItem("E 250 (Fe 410 W)A")
        form.addRow("Material *", self.material)

        conn_layout.addLayout(form)
        connection_box.setLayout(conn_layout)
        main_layout.addWidget(connection_box)

        # --- Section 2: Factored Loads ---
        load_box = QGroupBox("Factored Loads")
        load_box.setStyleSheet(connection_box.styleSheet())
        load_layout = QFormLayout()
        self.shear_force = QLineEdit()
        self.shear_force.setPlaceholderText("ex. 10 kN")
        load_layout.addRow("Shear Force (kN)", self.shear_force)

        self.axial_force = QLineEdit()
        self.axial_force.setPlaceholderText("ex. 10 kN")
        load_layout.addRow("Axial Force (kN)", self.axial_force)

        load_box.setLayout(load_layout)
        main_layout.addWidget(load_box)

        # --- Section 3: Bolt ---
        bolt_box = QGroupBox("Bolt")
        bolt_box.setStyleSheet(connection_box.styleSheet())
        bolt_form = QFormLayout()
        self.diameter = QComboBox()
        self.diameter.addItem("All")
        bolt_form.addRow("Diameter (mm) *", self.diameter)

        self.bolt_type = QComboBox()
        self.bolt_type.addItem("Bearing Bolt")
        bolt_form.addRow("Type *", self.bolt_type)

        self.property_class = QComboBox()
        self.property_class.addItem("All")
        bolt_form.addRow("Property Class (mm) *", self.property_class)

        bolt_box.setLayout(bolt_form)
        main_layout.addWidget(bolt_box)

        # --- Section 4: Plate ---
        plate_box = QGroupBox("Plate")
        plate_box.setStyleSheet(connection_box.styleSheet())
        plate_form = QFormLayout()
        self.thickness = QComboBox()
        self.thickness.addItem("All")
        plate_form.addRow("Thickness (mm) *", self.thickness)
        plate_box.setLayout(plate_form)
        main_layout.addWidget(plate_box)

        # --- Bottom Action ---
        self.design_btn = QPushButton("\u2692 Design \u00d7")  # wrench + Design + close
        self.design_btn.setStyleSheet("padding: 6px 12px;")
        main_layout.addWidget(self.design_btn, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)
        self.setFixedWidth(400)


def main():
    app = QApplication(sys.argv)
    widget = ConnectionDesignWidget()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
