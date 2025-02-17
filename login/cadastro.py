# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Tela_Cadastro(object):
    def setupUi(self, Tela_Cadastro):
        if not Tela_Cadastro.objectName():
            Tela_Cadastro.setObjectName(u"Tela_Cadastro")
        Tela_Cadastro.resize(800, 600)
        self.centralwidget = QWidget(Tela_Cadastro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 231, 219);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.txt_estadocivil = QLabel(self.frame_5)
        self.txt_estadocivil.setObjectName(u"txt_estadocivil")
        font = QFont()
        font.setPointSize(12)
        self.txt_estadocivil.setFont(font)

        self.verticalLayout_5.addWidget(self.txt_estadocivil)

        self.button_viuvo = QRadioButton(self.frame_5)
        self.button_viuvo.setObjectName(u"button_viuvo")
        self.button_viuvo.setFont(font)

        self.verticalLayout_5.addWidget(self.button_viuvo)

        self.button_solteiro = QRadioButton(self.frame_5)
        self.button_solteiro.setObjectName(u"button_solteiro")
        self.button_solteiro.setFont(font)

        self.verticalLayout_5.addWidget(self.button_solteiro)

        self.button_casado = QRadioButton(self.frame_5)
        self.button_casado.setObjectName(u"button_casado")
        self.button_casado.setFont(font)

        self.verticalLayout_5.addWidget(self.button_casado)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 231, 219);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.txt_endereco = QLabel(self.frame_6)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setFont(font)

        self.verticalLayout_6.addWidget(self.txt_endereco)

        self.input_endereco = QLineEdit(self.frame_6)
        self.input_endereco.setObjectName(u"input_endereco")

        self.verticalLayout_6.addWidget(self.input_endereco)


        self.gridLayout.addWidget(self.frame_6, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 231, 219);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_usuario = QLabel(self.frame_2)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setFont(font)

        self.verticalLayout_2.addWidget(self.txt_usuario)

        self.input_usuario = QLineEdit(self.frame_2)
        self.input_usuario.setObjectName(u"input_usuario")

        self.verticalLayout_2.addWidget(self.input_usuario)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 231, 219);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tx_nome = QLabel(self.frame)
        self.tx_nome.setObjectName(u"tx_nome")
        self.tx_nome.setFont(font)

        self.verticalLayout.addWidget(self.tx_nome)

        self.input_nome = QLineEdit(self.frame)
        self.input_nome.setObjectName(u"input_nome")

        self.verticalLayout.addWidget(self.input_nome)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 231, 219);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_senha = QLabel(self.frame_3)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setFont(font)

        self.verticalLayout_3.addWidget(self.txt_senha)

        self.input_senha = QLineEdit(self.frame_3)
        self.input_senha.setObjectName(u"input_senha")

        self.verticalLayout_3.addWidget(self.input_senha)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 231, 219);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_datanasc = QLabel(self.frame_4)
        self.txt_datanasc.setObjectName(u"txt_datanasc")
        self.txt_datanasc.setFont(font)

        self.verticalLayout_4.addWidget(self.txt_datanasc)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_4.addWidget(self.dateEdit)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        Tela_Cadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_Cadastro)

        QMetaObject.connectSlotsByName(Tela_Cadastro)
    # setupUi

    def retranslateUi(self, Tela_Cadastro):
        Tela_Cadastro.setWindowTitle(QCoreApplication.translate("Tela_Cadastro", u"MainWindow", None))
        self.txt_estadocivil.setText(QCoreApplication.translate("Tela_Cadastro", u"Estado civil:", None))
        self.button_viuvo.setText(QCoreApplication.translate("Tela_Cadastro", u"Vi\u00favo", None))
        self.button_solteiro.setText(QCoreApplication.translate("Tela_Cadastro", u"Solteiro", None))
        self.button_casado.setText(QCoreApplication.translate("Tela_Cadastro", u"Casado", None))
        self.pushButton.setText(QCoreApplication.translate("Tela_Cadastro", u"Proximo", None))
        self.txt_endereco.setText(QCoreApplication.translate("Tela_Cadastro", u"Endere\u00e7o:", None))
        self.txt_usuario.setText(QCoreApplication.translate("Tela_Cadastro", u"Novo usu\u00e1rio:", None))
        self.tx_nome.setText(QCoreApplication.translate("Tela_Cadastro", u"Nome completo:", None))
        self.txt_senha.setText(QCoreApplication.translate("Tela_Cadastro", u"Nova senha:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Tela_Cadastro", u"Voltar", None))
        self.txt_datanasc.setText(QCoreApplication.translate("Tela_Cadastro", u"Data Nascimento:", None))
    # retranslateUi

