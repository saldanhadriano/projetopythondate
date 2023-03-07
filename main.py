import sys
from threading import Event
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import QObject, QEvent, QPropertyAnimation, QEasingCurve, QPoint, QTimer

import random

from ui_main_ui_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.coracao.setVisible(False)
        self.coracao_2.setVisible(False)
        self.coracao_3.setVisible(False)
        self.coracao_4.setVisible(False)
        self.coracao_5.setVisible(False)
        self.coracao_6.setVisible(False)
        self.coracao_7.setVisible(False)
        self.coracao_8.setVisible(False)
        self.coracao_9.setVisible(False)
        self.coracao_10.setVisible(False)
        self.coracao_11.setVisible(False)
        self.coracao_12.setVisible(False)
        self.coracao_13.setVisible(False)
        self.coracao_14.setVisible(False)
        self.coracao_15.setVisible(False)
        self.coracao_16.setVisible(False)
        self.coracao_17.setVisible(False)
        self.coracao_18.setVisible(False)
        self.coracao_19.setVisible(False)
        self.coracao_20.setVisible(False)
        self.coracao_21.setVisible(False)
        self.coracao_22.setVisible(False)
        self.coracao_23.setVisible(False)
        self.coracao_24.setVisible(False)
        self.coracao_25.setVisible(False)
        self.coracao_26.setVisible(False)
        
        self.button_no.clicked.connect(self.moveButton)
        self.button_yes.clicked.connect(self.melhorOpcao)
        
        self.frame_no.installEventFilter(self)
        self.frame_yes.installEventFilter(self)
        
    def moveButton(self):
          self.frame_no.move(random.randint(0,300), random.randint(0,300))
          #self.button_no.setStyleSheet("QPushButton#button_no{\n"
          #                              "	min-width: 70px;\n"
          #                              "   max-width: 70px;\n"
          #                              "	border: 1px solid;\n"
          #                              "	border-color: purple;\n"
          #                              "	font-size: 10px;\n"
          #                              "	color: black;\n"
          #                              "	min-height: 20px;\n"
          #                              "   max-height: 20px;\n"
          #                              "	border-radius: 10px;\n"
          #                              "	font-size: 10px;\n"
          #                              "	background-color: white;\n"
          #                              "}\n")
          
    def melhorOpcao(self):
        self.label.setText("Obrigado por escolher\n a melhor opção!\n*-*")
        self.label.setStyleSheet("QLabel{\n"
                                 "	font-size: 17px;\n"
                                 "	font-weight: bold;\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "  qproperty-alignment: AlignCenter;\n"
                                 "}\n")
        self.button_yes.setVisible(False)
        self.button_no.setVisible(False)

        QtCore.QTimer.singleShot(random.randint(9000,10000), lambda: self.coracao.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_2.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_3.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_4.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_5.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_6.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_7.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_8.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_9.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_10.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_11.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_12.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_13.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_14.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_15.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_16.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_17.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_18.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_19.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_20.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_21.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_22.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_23.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_24.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(1000,10000), lambda: self.coracao_25.setVisible(True))
        QtCore.QTimer.singleShot(random.randint(9500,10000), lambda: self.coracao_26.setVisible(True))
        

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frame_no:
                self.moveButton()
                return True
        else:
            return False


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
