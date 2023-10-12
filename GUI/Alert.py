import sys
from PySide6 import QtWidgets as qtw

from Application.UI.ui_Alert import Ui_Alert

class Alert(qtw.QWidget, Ui_Alert):
    """
    This is a simple alert window.
    It requires the message to be passed or there is None.
    """    
    def __init__(self, Alert_Message=None):
        super().__init__()
        self.setupUi(self)
        self.label.setText(Alert_Message)
        self.pb_ok.clicked.connect(self.close)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Alert('apple')
    window.show()
    sys.exit(app.exec())
