from PyQt5 import QtWidgets


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        self.credentials = {}
        if(self.textName.text() is not '' and self.textPass.text() is not ''):
            self.credentials['username'] = self.textName.text()
            self.credentials['password'] = self.textPass.text()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

    def getCredentials(self):
        return self.credentials


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    sys.exit(login.exec_())
