"""Module containing the main function to run sequence delivery tool.
"""
import os
import sys

from PySide2 import QtWidgets

# Set `src` directory to  `PYTHONPATH` on runtime
_core_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(_core_path)

from _tool import model, view, controller


def main():
    """Main function to run MVC together.
    """
    app = QtWidgets.QApplication(sys.argv)
    sd_model = model.SequenceDeliveryModel()
    sd_controller = controller.SequenceDeliveryController(sd_model)
    sd_view = view.SequenceDeliveryView(sd_controller)
    sd_view.show()
    sys.exit(app.exec_())

main()
