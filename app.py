import sys
import os
from PyQt5 import Qt
from settingsController import SettingsController
from gitController import GitController
from projectController import ProjectController


def main(argv):
    settingsController = SettingsController()
    prefs = settingsController.loadPrefs()
    prefs['credentials']['password'] = settingsController.decrypt(
        prefs['credentials']['password'])
    if len(argv) > 1 and argv[1] is not None:
        gitController = GitController()
        gitController.create_repo(prefs, argv[1])


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    if(len(sys.argv) < 2):
        projectController = ProjectController()
        projectController.exec_()
        sys.argv.append(projectController.getProjectName())
    main(sys.argv)
