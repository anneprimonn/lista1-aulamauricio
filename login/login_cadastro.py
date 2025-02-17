from PySide6.QtWidgets import QMainWindow
from cadastro import Ui_MainWindow

class CadastroWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Cadastro") 
        
    def save_data(self):
        pass