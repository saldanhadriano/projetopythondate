# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 438)
        MainWindow.setMaximumSize(QSize(450, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0.485401, y1:0.289, x2:0.52, y2:1, stop:0.0511364 rgba(147, 0, 0, 255), stop:1 rgba(109, 0, 55, 255))\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 40px;\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-size: 20px;\n"
"	color: black;\n"
"	min-height: 40px;\n"
"	border-radius: 20px;\n"
"	background-color: white;\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 431, 101))
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(30, 160, 171, 101))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_yes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_yes = QPushButton(self.frame_yes)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout.addWidget(self.button_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(250, 160, 171, 101))
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_no)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout_2.addWidget(self.button_no)

        self.coracao = QLabel(self.centralwidget)
        self.coracao.setObjectName(u"coracao")
        self.coracao.setGeometry(QRect(90, 90, 281, 251))
        self.coracao.setStyleSheet(u"")
        self.coracao.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao.setScaledContents(True)
        self.coracao_2 = QLabel(self.centralwidget)
        self.coracao_2.setObjectName(u"coracao_2")
        self.coracao_2.setGeometry(QRect(360, 340, 91, 91))
        self.coracao_2.setStyleSheet(u"")
        self.coracao_2.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_2.setScaledContents(True)
        self.coracao_3 = QLabel(self.centralwidget)
        self.coracao_3.setObjectName(u"coracao_3")
        self.coracao_3.setGeometry(QRect(40, 300, 91, 91))
        self.coracao_3.setStyleSheet(u"")
        self.coracao_3.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_3.setScaledContents(True)
        self.coracao_4 = QLabel(self.centralwidget)
        self.coracao_4.setObjectName(u"coracao_4")
        self.coracao_4.setGeometry(QRect(0, 90, 91, 91))
        self.coracao_4.setStyleSheet(u"")
        self.coracao_4.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_4.setScaledContents(True)
        self.coracao_5 = QLabel(self.centralwidget)
        self.coracao_5.setObjectName(u"coracao_5")
        self.coracao_5.setGeometry(QRect(360, 80, 91, 91))
        self.coracao_5.setStyleSheet(u"")
        self.coracao_5.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_5.setScaledContents(True)
        self.coracao_6 = QLabel(self.centralwidget)
        self.coracao_6.setObjectName(u"coracao_6")
        self.coracao_6.setGeometry(QRect(320, 120, 51, 51))
        self.coracao_6.setStyleSheet(u"")
        self.coracao_6.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_6.setScaledContents(True)
        self.coracao_7 = QLabel(self.centralwidget)
        self.coracao_7.setObjectName(u"coracao_7")
        self.coracao_7.setGeometry(QRect(120, 360, 51, 51))
        self.coracao_7.setStyleSheet(u"")
        self.coracao_7.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_7.setScaledContents(True)
        self.coracao_8 = QLabel(self.centralwidget)
        self.coracao_8.setObjectName(u"coracao_8")
        self.coracao_8.setGeometry(QRect(270, 320, 61, 61))
        self.coracao_8.setStyleSheet(u"")
        self.coracao_8.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_8.setScaledContents(True)
        self.coracao_9 = QLabel(self.centralwidget)
        self.coracao_9.setObjectName(u"coracao_9")
        self.coracao_9.setGeometry(QRect(-10, 300, 61, 61))
        self.coracao_9.setStyleSheet(u"")
        self.coracao_9.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_9.setScaledContents(True)
        self.coracao_10 = QLabel(self.centralwidget)
        self.coracao_10.setObjectName(u"coracao_10")
        self.coracao_10.setGeometry(QRect(60, 160, 61, 61))
        self.coracao_10.setStyleSheet(u"")
        self.coracao_10.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_10.setScaledContents(True)
        self.coracao_11 = QLabel(self.centralwidget)
        self.coracao_11.setObjectName(u"coracao_11")
        self.coracao_11.setGeometry(QRect(360, 260, 51, 51))
        self.coracao_11.setStyleSheet(u"")
        self.coracao_11.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_11.setScaledContents(True)
        self.coracao_12 = QLabel(self.centralwidget)
        self.coracao_12.setObjectName(u"coracao_12")
        self.coracao_12.setGeometry(QRect(230, 380, 41, 41))
        self.coracao_12.setStyleSheet(u"")
        self.coracao_12.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_12.setScaledContents(True)
        self.coracao_13 = QLabel(self.centralwidget)
        self.coracao_13.setObjectName(u"coracao_13")
        self.coracao_13.setGeometry(QRect(310, 280, 81, 81))
        self.coracao_13.setStyleSheet(u"")
        self.coracao_13.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_13.setScaledContents(True)
        self.coracao_14 = QLabel(self.centralwidget)
        self.coracao_14.setObjectName(u"coracao_14")
        self.coracao_14.setGeometry(QRect(160, 320, 81, 81))
        self.coracao_14.setStyleSheet(u"")
        self.coracao_14.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_14.setScaledContents(True)
        self.coracao_15 = QLabel(self.centralwidget)
        self.coracao_15.setObjectName(u"coracao_15")
        self.coracao_15.setGeometry(QRect(80, 260, 81, 81))
        self.coracao_15.setStyleSheet(u"")
        self.coracao_15.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_15.setScaledContents(True)
        self.coracao_16 = QLabel(self.centralwidget)
        self.coracao_16.setObjectName(u"coracao_16")
        self.coracao_16.setGeometry(QRect(110, 90, 81, 81))
        self.coracao_16.setStyleSheet(u"")
        self.coracao_16.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_16.setScaledContents(True)
        self.coracao_18 = QLabel(self.centralwidget)
        self.coracao_18.setObjectName(u"coracao_18")
        self.coracao_18.setGeometry(QRect(40, 380, 110, 83))
        self.coracao_18.setStyleSheet(u"")
        self.coracao_18.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_18.setScaledContents(True)
        self.coracao_19 = QLabel(self.centralwidget)
        self.coracao_19.setObjectName(u"coracao_19")
        self.coracao_19.setGeometry(QRect(280, 380, 101, 91))
        self.coracao_19.setStyleSheet(u"")
        self.coracao_19.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_19.setScaledContents(True)
        self.coracao_17 = QLabel(self.centralwidget)
        self.coracao_17.setObjectName(u"coracao_17")
        self.coracao_17.setGeometry(QRect(10, 200, 81, 81))
        self.coracao_17.setStyleSheet(u"")
        self.coracao_17.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_17.setScaledContents(True)
        self.coracao_20 = QLabel(self.centralwidget)
        self.coracao_20.setObjectName(u"coracao_20")
        self.coracao_20.setGeometry(QRect(390, 150, 81, 81))
        self.coracao_20.setStyleSheet(u"")
        self.coracao_20.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_20.setScaledContents(True)
        self.coracao_21 = QLabel(self.centralwidget)
        self.coracao_21.setObjectName(u"coracao_21")
        self.coracao_21.setGeometry(QRect(380, 230, 81, 81))
        self.coracao_21.setStyleSheet(u"")
        self.coracao_21.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_21.setScaledContents(True)
        self.coracao_22 = QLabel(self.centralwidget)
        self.coracao_22.setObjectName(u"coracao_22")
        self.coracao_22.setGeometry(QRect(260, 90, 41, 41))
        self.coracao_22.setStyleSheet(u"")
        self.coracao_22.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_22.setScaledContents(True)
        self.coracao_23 = QLabel(self.centralwidget)
        self.coracao_23.setObjectName(u"coracao_23")
        self.coracao_23.setGeometry(QRect(170, 30, 41, 41))
        self.coracao_23.setStyleSheet(u"")
        self.coracao_23.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_23.setScaledContents(True)
        self.coracao_24 = QLabel(self.centralwidget)
        self.coracao_24.setObjectName(u"coracao_24")
        self.coracao_24.setGeometry(QRect(280, 10, 91, 91))
        self.coracao_24.setStyleSheet(u"")
        self.coracao_24.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_24.setScaledContents(True)
        self.coracao_25 = QLabel(self.centralwidget)
        self.coracao_25.setObjectName(u"coracao_25")
        self.coracao_25.setGeometry(QRect(60, 10, 91, 91))
        self.coracao_25.setStyleSheet(u"")
        self.coracao_25.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao_25.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.coracao_25.raise_()
        self.coracao_24.raise_()
        self.coracao_23.raise_()
        self.coracao_22.raise_()
        self.coracao_15.raise_()
        self.coracao_14.raise_()
        self.coracao_6.raise_()
        self.coracao_10.raise_()
        self.coracao_16.raise_()
        self.label.raise_()
        self.frame_yes.raise_()
        self.frame_no.raise_()
        self.coracao.raise_()
        self.coracao_2.raise_()
        self.coracao_3.raise_()
        self.coracao_4.raise_()
        self.coracao_5.raise_()
        self.coracao_7.raise_()
        self.coracao_8.raise_()
        self.coracao_9.raise_()
        self.coracao_11.raise_()
        self.coracao_12.raise_()
        self.coracao_13.raise_()
        self.coracao_18.raise_()
        self.coracao_19.raise_()
        self.coracao_17.raise_()
        self.coracao_20.raise_()
        self.coracao_21.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Namora comigo?", None))
        self.button_yes.setText(QCoreApplication.translate("MainWindow", u"Sim :)", None))
        self.button_no.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.coracao.setText("")
        self.coracao_2.setText("")
        self.coracao_3.setText("")
        self.coracao_4.setText("")
        self.coracao_5.setText("")
        self.coracao_6.setText("")
        self.coracao_7.setText("")
        self.coracao_8.setText("")
        self.coracao_9.setText("")
        self.coracao_10.setText("")
        self.coracao_11.setText("")
        self.coracao_12.setText("")
        self.coracao_13.setText("")
        self.coracao_14.setText("")
        self.coracao_15.setText("")
        self.coracao_16.setText("")
        self.coracao_18.setText("")
        self.coracao_19.setText("")
        self.coracao_17.setText("")
        self.coracao_20.setText("")
        self.coracao_21.setText("")
        self.coracao_22.setText("")
        self.coracao_23.setText("")
        self.coracao_24.setText("")
        self.coracao_25.setText("")
    # retranslateUi
