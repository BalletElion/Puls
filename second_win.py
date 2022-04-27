from final_win import*
from instr import*
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel, #текст
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QLineEdit,#ввод
    QPushButton #кнопка
)
from PyQt5.QtCore import Qt, QTimer, QTime
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.begin = QLabel(txt_name)
        self.enter = QLineEdit()
        self.age = QLabel(txt_age)
        self.tx = QLabel(txt_test1)
        self.result_1 = QLineEdit()
        self.tx2 = QLabel(txt_test2)
        self.enter2 = QLineEdit()
        self.btn2 = QPushButton(txt_starttest2)
        self.tx3 = QLineEdit()
        self.fin = QLabel(txt_test3)
        self.finbtn = QPushButton(txt_starttest3)
        self.aaa = QLineEdit()
        self.text_timer = QLabel('00:00:00')
        self.btn_test1 = QPushButton(txt_starttest1)
        self.finfin = QPushButton(txt_sendresults)

        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.begin)
        self.layout.addWidget(self.enter, alignment = Qt.AlignLeft)#СДЕЛАЙ ВЫР.
        self.layout.addWidget(self.age)
        self.layout.addWidget(self.enter2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.tx)
        self.layout.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        self.layout.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.result_1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.tx2)
        self.layout.addWidget(self.btn2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.fin)
        self.layout.addWidget(self.finbtn, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.tx3, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.aaa, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.finfin, alignment = Qt.AlignCenter)
        self.setStyleSheet('background: #ff99cc;')

        
        
        
        
        
        self.setLayout(self.layout)
        

    def connects(self):
       self.btn_test1.clicked.connect(self.start_timer1)
       self.finfin.clicked.connect(self.next_click)
       self.btn2.clicked.connect(self.start_timer2)
    def start_timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
            
    def timer1Event(self):
        global time
        time = time.addSecs(-1) 
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def next_click(self):
        self.hide()
        self.aaa1 = FinalWin(self.enter2.text(), self.result_1.text(), self.tx3.text(), self.aaa.text())

    def start_timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
            
    def timer2Event(self):
        global time
        time = time.addSecs(-1) 
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0); ")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()












