'''
用 PyQt 实现GUI
'''
import os 
import sys 
from PyQt5.QtWidgets import (QMainWindow,QApplication, QWidget,QPushButton,QToolTip,
QDesktopWidget,QHBoxLayout,QVBoxLayout,QPlainTextEdit,QButtonGroup,QTextEdit,QLabel,QTextBrowser,QLineEdit)
from PyQt5.QtGui import QIcon,QFont,QPalette,QBrush,QPixmap
from controler import Dictator

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #初始化整个界面
    def initUI(self):
        self.setGeometry(300,300,600,220)           #设置大小
        self.setWindowTitle(" Keygen Framework ")
        self.center()               #居中显示
        self.IObox = QVBoxLayout()
        self.setLayout(self.IObox)
        
        #self.IObox.SetFixedSize(280,300)
        self.drawInputBox()     #创建输入窗口
        self.drawOutBox()       #创建输出窗口
        self.drawButton()       #创建按钮
        self.show()             #显示窗口


    #窗口居中显示
    def center(self):
        fg = self.frameGeometry()   #主窗口大小
        cp = QDesktopWidget().availableGeometry().center()  #获取屏幕分辨率，计算中间点位置
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    #绘制输入框
    def drawInputBox(self):
        self.InputBox = QTextEdit()
        self.InputBox.setFixedSize(280,130)
        self.IObox.addStretch(10)
        self.IObox.addWidget(self.InputBox)

    #获取输入的数据源
    def getData(self):
        return self.InputBox.toPlainText()

    #绘制输出窗口
    def drawOutBox(self):
        self.OutBox = QPlainTextEdit()
        self.OutBox.setFixedSize(280,130)
        self.IObox.addStretch(10)
        self.IObox.addWidget(self.OutBox)
    
    #显示数据到输出窗口
    def outputData(self,text):
        self.OutBox.setPlainText(text)

    #初始化按钮
    def drawButton(self):
        self.btnBox = QHBoxLayout()
        self.IObox.addLayout(self.btnBox)
        self.btnGo = QPushButton()
        self.btnGo.clicked.connect(lambda :self.btnGoHandler())
        self.btnGo.setText("Go")
        self.btnBox.addWidget(self.btnGo)
        self.IObox.addWidget(self.btnGo)
    
    #按钮回调函数
    def btnGoHandler(self):
        #创建控制器，处理数据
        #self.outputData(self.getData())
        self.controler=Dictator(self.getData())         #数据传递给控制器，让它去解析
        self.outputData(self.controler.feedbackData())  #把控制器解析的数据拿来显示
        
