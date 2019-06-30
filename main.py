import sys
import os
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit,  QVBoxLayout , QDialog , QToolButton, QLineEdit,QProgressBar, QSlider
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic
from PyQt5 import QtCore
import serial #Serial imported for Serial communication
from PyQt5.QtCore import  pyqtSignal, QThread




Form = uic.loadUiType(os.path.join(os.getcwd(), 'gui.ui'))[0]
Form1 = uic.loadUiType(os.path.join(os.getcwd(), '2.ui'))[0]


        
class Mainclass(Form, QMainWindow):  # gui and main thread
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.openButton.clicked.connect(self.openbutton)
        self.closeButton.clicked.connect(self.closebutton)
        self.stopButton.clicked.connect(self.stopbutton)
        self.startButton.clicked.connect(self.startbutton)
        self.settingButton.clicked.connect(self.settingbutton)
        self.dialog1=secendclass()
        
        self.sl.valueChanged.connect(self.valuechange)
        self.Bar.setMaximum(100)
        self.Bar.setMinimum(0)
        self.sl.setMaximum(100)
        self.sl.setMinimum(0)
        
        self.SerialUpdate=serialupdate()
        self.SerialUpdate.update_trigger.connect(self.TestBoxUpdate)
        self.SerialUpdate.start()
      

    def TestBoxUpdate(self,cc):
        self.text.setText(cc)
        
    def stopbutton(self):
        self.SerialUpdate.stop()
        
        
    def startbutton(self):
        self.SerialUpdate.start()
        
    def openbutton(self , value):
        value=1
        self.Bar.setValue(value)
        self.sl.setValue(value)
        self.clockwise()
        
        
    def closebutton(self , value):
        value=100
        self.Bar.setValue(value)
        self.sl.setValue(value)
        self.padclock()
   
    def settingbutton(self):
        self.dialog1.show()
        self.dialog1=secondclass()
        self.dialog1.show()


    def valuechange(self , value):
        self.Bar.setValue(value)
        
        
#==============================
class secendclass(Form1, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
#===============================
# MULTI-THREADING

class serialupdate(QThread):
    update_trigger=QtCore.pyqtSignal(str)
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.ser=serial.Serial()
        self.ser.port="COM3"
        self.ser.baudrate= 9600



    def run(self):
        self.ser.open()
        while 1:
            self.cc=str(self.ser.readline())
            self.cc=self.cc[2:][:-5]
            self.update_trigger.emit(self.cc)
            
            
        
    def stop(self):
        self.ser.close()

        
    def __del__(self):
        self.ser.close()
    
    
#=================================

def mainrun():
   
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    w = Mainclass()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
        mainrun()
