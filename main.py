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
        
        self.button_no.clicked.connect(self.moveButton)
        self.button_yes.clicked.connect(self.melhorOpcao)
        
        self.frame_no.installEventFilter(self)
        self.frame_yes.installEventFilter(self)
        
    def moveButton(self):
          self.frame_no.move(random.randint(0,300), random.randint(0,300))
          
          
    def melhorOpcao(self):
        self.label.setText("Escolheu a melhor opção!!!")
        self.label.setStyleSheet("QLabel{\n"
"	font-size: 30px;\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"}\n")
        self.button_yes.setVisible(False)
        self.button_no.setVisible(False)
        self.coracao.setVisible(True)
        self.coracao_2.setVisible(True)
        self.coracao_3.setVisible(True)
        self.coracao_4.setVisible(True)
        self.coracao_5.setVisible(True)
        self.coracao_6.setVisible(True)
        self.coracao_7.setVisible(True)
        self.coracao_8.setVisible(True)
        self.coracao_9.setVisible(True)
        self.coracao_10.setVisible(True)
        self.coracao_11.setVisible(True)
        self.coracao_12.setVisible(True)
        self.coracao_13.setVisible(True)
        self.coracao_14.setVisible(True)
        self.coracao_15.setVisible(True)
        self.coracao_16.setVisible(True)
        self.coracao_17.setVisible(True)
        self.coracao_18.setVisible(True)
        self.coracao_19.setVisible(True)
        self.coracao_20.setVisible(True)
        self.coracao_21.setVisible(True)
        self.coracao_22.setVisible(True)
        self.coracao_23.setVisible(True)
        self.coracao_24.setVisible(True)
        self.coracao_25.setVisible(True)

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
