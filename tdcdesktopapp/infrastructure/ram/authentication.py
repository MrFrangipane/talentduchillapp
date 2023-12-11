from PySide6.QtWidgets import QMessageBox

from tdcdesktopapp.components.authentication.abstract import AbstractSecurityLogin


class RamSecurityLogin(AbstractSecurityLogin):

    def exec(self):
        message = QMessageBox()
        message.setWindowTitle("Ram Security Login")
        message.setText("This is the Ram version of the application\nnothing is saved on quit.")
        message.setStandardButtons(QMessageBox.StandardButton.Ok)
        message.exec()

        return True
