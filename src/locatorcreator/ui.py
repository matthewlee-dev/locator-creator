"""locatorcreator UI."""

from maya import OpenMayaUI as omui
from Qt import QtCompat, QtWidgets

from locatorcreator.example import create_locator


def maya_main_window():
    """Return Maya's main window as a QWidget.

    Returns:
        QtWidgets.QWidget: Maya's main window.
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return QtCompat.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class LocatorCreatorWindow(QtWidgets.QDialog):
    """A single-button window that creates a locator on click."""

    def __init__(self, parent=None):
        super().__init__(parent or maya_main_window())
        self.setWindowTitle("Locator Creator")

        create_button = QtWidgets.QPushButton("Create Locator")
        create_button.clicked.connect(lambda: create_locator())

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(create_button)


def show():
    """Create and show the Locator Creator window.

    Returns:
        LocatorCreatorWindow: The window that was shown.
    """
    window = LocatorCreatorWindow()
    window.show()
    return window
