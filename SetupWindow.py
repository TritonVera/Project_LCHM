from PyQt5.QtWidgets import QSizePolicy, QWidget, QGroupBox, QRadioButton, \
                            QVBoxLayout, QLabel, QHBoxLayout, QPushButton, \
                            QDoubleSpinBox
from PyQt5.QtCore import Qt


class SetupWindow(QGroupBox):
    def __init__(self, parent = None):
        QGroupBox.__init__(self, parent)
        print(parent)
        self.setDisabled(1)