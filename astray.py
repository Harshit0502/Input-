import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGroupBox,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox,
    QLineEdit,
    QSpinBox,
    QFrame,
    QLabel,
)


class MainWindow(QMainWindow):
    """Main application window with sidebar and central form."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Structural Connection Designer")
        self._build_ui()

    # ------------------------------------------------------------------
    # UI Construction
    # ------------------------------------------------------------------
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = self._create_sidebar()
        root_layout.addWidget(self.sidebar)

        self.content_area = QWidget()
        content_layout = QVBoxLayout(self.content_area)
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(10)

        content_layout.addWidget(self._create_connection_section())
        content_layout.addWidget(self._create_bolt_section())
        content_layout.addWidget(self._create_plate_section())
        content_layout.addWidget(self._create_loads_section())
        content_layout.addStretch()

        root_layout.addWidget(self.content_area)

        self._apply_styles()

    # ------------------------------------------------------------------
    # Sidebar
    # ------------------------------------------------------------------
    def _create_sidebar(self) -> QWidget:
        bar = QFrame()
        bar.setObjectName("sidebar")
        layout = QVBoxLayout(bar)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        top_row = QHBoxLayout()
        self.input_dock_btn = QPushButton("Input Dock")
        self.input_dock_btn.setObjectName("inputDockBtn")
        self.additional_btn = QPushButton("Additional Inputs ▼")
        self.additional_btn.setObjectName("additionalBtn")
        top_row.addWidget(self.input_dock_btn)
        top_row.addWidget(self.additional_btn)
        layout.addLayout(top_row)

        self.assumptions_btn = QPushButton("Assumptions")
        self.assumptions_btn.setObjectName("assumptionsBtn")
        self.preferences_btn = QPushButton("Preferences")
        self.preferences_btn.setObjectName("preferencesBtn")
        layout.addWidget(self.assumptions_btn)
        layout.addWidget(self.preferences_btn)
        layout.addStretch()

        bar.setFixedWidth(170)
        return bar

    # ------------------------------------------------------------------
    # Sections
    # ------------------------------------------------------------------
    def _create_connection_section(self) -> QGroupBox:
        group = QGroupBox("Connection")
        form = QFormLayout(group)
        form.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        self.connection_type = QComboBox()
        self.connection_type.addItems(["Bolted", "Welded"])
        form.addRow("Connection Type", self.connection_type)

        self.end_condition = QComboBox()
        self.end_condition.addItems(["Fixed", "Hinged"])
        form.addRow("End Condition", self.end_condition)

        orientation_widget = QWidget()
        h = QHBoxLayout(orientation_widget)
        h.setContentsMargins(0, 0, 0, 0)
        self.orientation = QComboBox()
        self.orientation.addItems(["Horizontal", "Vertical"])
        self.mirror_btn = QPushButton("Mirror")
        self.mirror_btn.setCheckable(True)
        h.addWidget(self.orientation)
        h.addWidget(self.mirror_btn)
        form.addRow("Member Orientation", orientation_widget)

        return group

    def _create_bolt_section(self) -> QGroupBox:
        group = QGroupBox("Bolt Details")
        form = QFormLayout(group)
        form.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        self.bolt_dia = QLineEdit()
        self.bolt_dia.setPlaceholderText("ex. 20 mm")
        form.addRow("Bolt Diameter", self.bolt_dia)

        self.bolt_type = QComboBox()
        self.bolt_type.addItems(["Friction", "Bearing"])
        form.addRow("Bolt Type", self.bolt_type)

        self.num_bolts = QSpinBox()
        self.num_bolts.setRange(1, 100)
        form.addRow("Number of Bolts", self.num_bolts)

        return group

    def _create_plate_section(self) -> QGroupBox:
        group = QGroupBox("Plate Dimensions")
        form = QFormLayout(group)
        form.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        self.plate_thk = QLineEdit()
        form.addRow("Plate Thickness", self.plate_thk)

        self.plate_w = QLineEdit()
        form.addRow("Plate Width", self.plate_w)

        self.plate_h = QLineEdit()
        form.addRow("Plate Height", self.plate_h)

        return group

    def _create_loads_section(self) -> QGroupBox:
        group = QGroupBox("Factored Loads")
        form = QFormLayout(group)
        form.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        self.axial_force = QLineEdit()
        self.axial_force.setPlaceholderText("ex. 10 kN")
        form.addRow("Axial Force (kN)", self.axial_force)

        self.shear_force = QLineEdit()
        self.shear_force.setPlaceholderText("ex. 15 kN")
        form.addRow("Shear Force (kN)", self.shear_force)

        return group

    # ------------------------------------------------------------------
    # Styling helper
    # ------------------------------------------------------------------
    def _apply_styles(self):
        self.setStyleSheet(
            """
            QFrame#sidebar {
                background: #f0f8f0;
            }
            QPushButton#inputDockBtn {
                background-color: #2d6a2d;
                color: white;
                padding: 4px 8px;
                border-radius: 4px;
            }
            QPushButton#additionalBtn {
                background-color: #a8d5a8;
                padding: 4px 6px;
                border-radius: 4px;
            }
            QPushButton#assumptionsBtn,
            QPushButton#preferencesBtn {
                background-color: #c9e5c9;
                padding: 4px 6px;
                border-radius: 4px;
            }
            QGroupBox {
                border: 1px solid #7fbf7f;
                border-radius: 6px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
                background: transparent;
            }
            QLineEdit {
                background: white;
                padding: 2px 4px;
            }
            QPushButton:checked {
                background-color: #688f68;
                color: white;
            }
            """
        )


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
