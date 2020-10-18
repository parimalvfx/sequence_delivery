"""This module contains the view class for sequence delivery.
"""
from PySide2 import QtCore, QtWidgets


class SequenceDeliveryView(QtWidgets.QWidget):
    """This view class provides the presentation logic to sequence delivery.

    :param controller: Controller class to drive the backend operations.
    :type controller: :class:`_tool.controller.SequenceDeliveryController`
    :param parent: Parent widget.
    :type parent: :class:`PySide2.QtWidgets.QWidget`, optional
    """
    def __init__(self, controller, parent=None) -> None:
        super().__init__(parent=parent)
        self._controller = controller
        self._build_ui()
        self._connect_signals()

    def _build_ui(self):
        """Method to build all child widgets and layouts.
        """
        # Source widgets and layout
        source_label = QtWidgets.QLabel("Source directory")
        self.source_line_edit = QtWidgets.QLineEdit()
        self.source_button = QtWidgets.QPushButton("...")
        self.source_button.setMaximumWidth(50)
        source_layout = QtWidgets.QHBoxLayout()
        for widget in (source_label, self.source_line_edit, self.source_button):
            source_layout.addWidget(widget)

        # Destination widgets and layout
        destination_label = QtWidgets.QLabel("Destination directory")
        self.destination_line_edit = QtWidgets.QLineEdit()
        self.destination_button = QtWidgets.QPushButton("...")
        self.destination_button.setMaximumWidth(50)
        destination_layout = QtWidgets.QHBoxLayout()
        for widget in (destination_label, self.destination_line_edit,
        self.destination_button):
            destination_layout.addWidget(widget)

        # Button widgets and layout
        self.execute_button = QtWidgets.QPushButton("Execute")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.execute_button)
        button_layout.addWidget(self.cancel_button)

        # Master layout
        master_layout = QtWidgets.QVBoxLayout()
        for layout in (source_layout, destination_layout, button_layout):
            master_layout.addLayout(layout)
        self.setLayout(master_layout)
        self.setWindowTitle("Sequence Delivery Tool")
        self.setMinimumWidth(700)
        self.setFixedHeight(140)

    def _connect_signals(self):
        """Method to connect widget signals.
        """
        self.source_button.clicked.connect(self._get_source_directory)
        self.destination_button.clicked.connect(self._get_destination_directory)
        self.cancel_button.clicked.connect(self.close)
        self.execute_button.clicked.connect(self._execute)

    def _create_file_dialog(self):
        """Helper method to create `QtWidgets.QFileDialog`.
        """
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        file_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)

        return file_dialog

    def _get_source_directory(self):
        """File dialog to get source directory from user.
        """
        file_dialog = self._create_file_dialog()

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self._controller._model.source_directories = selected_files
            self.source_line_edit.setText(selected_files[0])

    def _get_destination_directory(self):
        """File dialog to get destination directory from user.
        """
        file_dialog = self._create_file_dialog()

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()[0]
            self._controller._model.destinaion_directory = selected_files
            self.destination_line_edit.setText(selected_files)

    def _execute(self):
        """Execute moving of image sequences.
        """
        self.setCursor(QtCore.Qt.WaitCursor)
        self.cancel_button.setDisabled(True)
        self._controller.move_sequences()
        self.cancel_button.setEnabled(True)
        self.unsetCursor()
