# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_designer.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
#import img_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 582)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 500))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 500))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(255, 231, 219);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        font = QFont()
        font.setPointSize(12)
        self.txt_senha.setFont(font)

        self.gridLayout_2.addWidget(self.txt_senha, 3, 0, 1, 1)

        self.botao_entrar = QPushButton(self.frame)
        self.botao_entrar.setObjectName(u"botao_entrar")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setWeight(QFont.Medium)
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.botao_entrar.setCheckable(False)
        self.botao_entrar.setAutoRepeat(False)
        self.botao_entrar.setAutoRepeatDelay(500)
        self.botao_entrar.setAutoRepeatInterval(500)

        self.gridLayout_2.addWidget(self.botao_entrar, 5, 0, 1, 1)

        self.input_senha = QLineEdit(self.frame)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setMouseTracking(False)
        self.input_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.input_senha.setInputMask(u"")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha.setCursorPosition(0)
        self.input_senha.setDragEnabled(False)
        self.input_senha.setReadOnly(False)
        self.input_senha.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.input_senha.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input_senha, 4, 0, 1, 1)

        self.input_usuario = QLineEdit(self.frame)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.input_usuario, 2, 0, 1, 1)

        self.txt_usuario = QLabel(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setFont(font)

        self.gridLayout_2.addWidget(self.txt_usuario, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/icon_login/imglogin.jpg"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.frame)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"entrar", None))
        self.input_senha.setPlaceholderText("")
        self.txt_usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label.setText("")
    # retranslateUi

