import sys
import base64
import json
from pprint import pprint
from PyQt5 import Qt
from loginController import Login


class SettingsController(object):

    def getFolder(self):
        return Qt.QFileDialog.getExistingDirectory(None, "Selecione a raiz do repositório no seu sistema", "../")

    def getCredentials(self):
        login = Login()
        login.exec_()
        credentials = login.getCredentials()
        credentials['password'] = self.encrypt(
            credentials['password'].encode('utf-8'))
        return credentials

    def encrypt(self, source):
        return base64.b64encode(source).decode("utf-8")

    def decrypt(self, source):
        return base64.b64decode(source).decode("utf-8")

    def fillRepoFolder(self, prefs):
        if not "localRepo" in prefs:
            prefs["localRepo"] = None
        while(prefs["localRepo"] is None or prefs["localRepo"] is ""):
            prefs["localRepo"] = self.getFolder()
        with open('settings.json', 'w') as outfile:
            json.dump(prefs, outfile)
            return prefs

    def fillUserCredentials(self, prefs):
        if not "credentials" in prefs:
            prefs["credentials"] = {}
        while(prefs["credentials"] is None or not bool(prefs["credentials"])):
            prefs["credentials"] = self.getCredentials()
        with open('settings.json', 'w') as outfile:
            json.dump(prefs, outfile)
            return prefs

    def loadPrefs(self):
        try:
            with open('settings.json') as json_file:
                prefs = json.load(json_file)
                prefs = self.fillRepoFolder(prefs)
                prefs = self.fillUserCredentials(prefs)
        except Exception:
            if not 'prefs' in locals():
                prefs = {}
            prefs = self.fillRepoFolder(prefs)
            prefs = self.fillUserCredentials(prefs)
        finally:
            return prefs


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    settingsController = SettingsController()
    print(settingsController.loadPrefs())
