# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QLineEdit,
    QPushButton
)


class FinalWin(QWidget):
    def __init__(self, age, P1, P2, P3):
        super().__init__()
        self.age = int(age)
        self.P1 = int(P1)
        self.P2 = int(P2)
        self.P3 = int(P3)
        self.set_appear()
        self.initUI()
        #self.connects()
        self.show()
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI (self):
        self.result1 = QLabel(self.rufie (self.age, self.P1, self.P2, self.P3))
        self.index = QLabel(str(self.result))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.result1, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def rufie (self, age, P1, P2, P3):
        self.result = (4 * (P1 + P2 + P3) - 200) / 10
        result = self.result
        if age == 7 or age == 8:
            if result >= 21:
                #низкий
                return txt_res1
            elif result >= 17 and result <= 20.9:
                #удовлетворительный
                return txt_res2
            elif result >= 12 and result <= 16.9:
                #средний
                return txt_res3
            elif result >= 6.5 and result <= 11.9:
                #выше среднего
                return txt_res4
            else:
                #высокий
                return txt_res5
        

        elif age == 9 or age == 10:
            if result >= 19.5:
                #низкий
                return txt_res1
            elif result >= 15.5 and result <= 19.4:
                #удовлетворительный
                return txt_res2
            elif result >= 10.5 and result <= 15.4:
                #средний
                return txt_res3
            elif result >= 5 and result <= 10.4:
                #выше среднего
                return txt_res4
            else:
                #высокий
                return txt_res5


        elif age == 11 or age == 12:
            if result >= 18:
                #низкий
                return txt_res1
            elif result >= 14 and result <= 17.9:
                #удовлетворительный
                return txt_res2
            elif result >= 9 and result <= 13.9:
                #средний
                return txt_res3
            elif result >= 3.5 and result <= 8.9:
                #выше среднего
                return txt_res4
            else:
                #высокий
                return txt_res5


        elif age == 13 or age == 14:
            if result >= 16.5:
                #низкий
                return txt_res1
            elif result >= 12.5 and result <= 16.4:
                #удовлетворительный
                return txt_res2
            elif result >= 7.5 and result <= 12.4:
                #средний
                return txt_res3
            elif result >= 2 and result <= 7.4:
                #выше среднего
                return txt_res4
            else:
                #высокий
                return txt_res5

        elif age >= 15:
            if result >= 15:
                #низкий
                return txt_res1
            elif result >= 11 and result <= 14.9:
                #удовлетворительный
                return txt_res2
            elif result >= 6 and result <= 10.9:
                #средний
                return txt_res3
            elif result >= 0.5 and result <= 5.9:
                #выше среднего
                return txt_res4
            else:
                #высокий
                return txt_res5

