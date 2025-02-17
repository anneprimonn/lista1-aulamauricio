import sys
from PySide6.QtWidgets import QApplication,QMessageBox, QMainWindow
from login_designer import Ui_MainWindow
from cadastro import Ui_Tela_Cadastro

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.login = Ui_MainWindow()
        self.login.setupUi(self)
        self.login.botao_entrar.clicked.connect(self.checker)

    def checker(self):
        if self.login.input_usuario.text() == "adm":
            self.login_cadastro = Ui_Tela_Cadastro()
            self.login_cadastro.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())


