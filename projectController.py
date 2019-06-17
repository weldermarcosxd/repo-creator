from PyQt5 import QtWidgets


class ProjectController(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ProjectController, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.buttonOk = QtWidgets.QPushButton('Ok', self)
        self.buttonOk.clicked.connect(self.handleProject)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.buttonOk)

    def handleProject(self):
        self.project_name = ""
        if(self.textName.text() is not ''):
            self.project_name = self.textName.text()
            self.project_name = self.project_name.split(" ")[0].lower()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Invalid project name')

    def getProjectName(self):
        return self.project_name


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projectController = ProjectController()
    sys.exit(projectController.exec_())
