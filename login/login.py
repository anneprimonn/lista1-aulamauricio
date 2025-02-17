from PySide6.QtWidgets import QMainWindow, QMessageBox
from login_designer import Ui_MainWindow  


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tela de Login")  
        self.ui.botao_entrar.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.ui.input_usuario.text()
        senha = self.ui.input_senha.text()

        if usuario == "adm" and senha == "123":
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.close()

        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")