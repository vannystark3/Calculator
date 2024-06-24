from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CALCULATOR")
        self.setGeometry(200,200,400,220)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(5,5,390,60)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid gray;"
                                 "background : white"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial',15))
        push1 = QPushButton("1",self)
        push2 = QPushButton("2",self)
        push3 = QPushButton("3",self)
        push4 = QPushButton("4",self)
        push5 = QPushButton("5",self)
        push6 = QPushButton("6",self)
        push7 = QPushButton("7",self)
        push8 = QPushButton("8",self)
        push9 = QPushButton("9",self)
        push0 = QPushButton("0",self)
        pushplus = QPushButton("+",self)
        pushminus = QPushButton("-",self)
        pushmul = QPushButton("*",self)
        pushdiv = QPushButton("/",self)
        pushequal = QPushButton("=",self)
        pushdot = QPushButton(".",self)
        pushcl = QPushButton("clear",self)
        pushdel = QPushButton("del",self)
        push1.move(0,100)
        push2.move(100,100)
        push3.move(200,100)
        push4.move(0,130)
        push5.move(100,130)
        push6.move(200,130)
        push7.move(0,160)
        push8.move(100,160)
        push9.move(200,160)
        push0.move(100,190)
        pushequal.move(200,190)
        pushdot.move(0,190)
        pushplus.move(300,100)
        pushminus.move(300,130)
        pushmul.move(300,160)
        pushdiv.move(300,190)
        pushcl.setGeometry(0,70,200,30)
        pushdel.setGeometry(200,70,200,30)

        c = QGraphicsColorizeEffect()
        c.setColor(Qt.red)
        pushequal.setGraphicsEffect(c)

        d = QGraphicsColorizeEffect()
        e = QGraphicsColorizeEffect()
        f = QGraphicsColorizeEffect()
        g = QGraphicsColorizeEffect()
        d.setColor(Qt.blue)
        e.setColor(Qt.blue)
        f.setColor(Qt.blue)
        g.setColor(Qt.blue)

        x = QGraphicsColorizeEffect()
        x.setColor(Qt.magenta)
        pushdot.setGraphicsEffect(x)
        pushplus.setGraphicsEffect(d)
        pushminus.setGraphicsEffect(e)
        pushmul.setGraphicsEffect(f)
        pushdiv.setGraphicsEffect(g)

        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push0.clicked.connect(self.action0)
        pushequal.clicked.connect(self.action_equal)
        pushdot.clicked.connect(self.action_dot)
        pushplus.clicked.connect(self.action_plus)
        pushminus.clicked.connect(self.action_minus)
        pushmul.clicked.connect(self.action_mul)
        pushdiv.clicked.connect(self.action_div)
        pushcl.clicked.connect(self.action_clear)
        pushdel.clicked.connect(self.action_del)

    def action_equal(self):
        equation = self.label.text()
        try:
            ans = eval(equation)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong input")
    def action_dot(self):
        text = self.label.text()
        self.label.setText(text + ".")
    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + "+")
    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + "-")
    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + "*")
    def action_div(self):
        text = self.label.text()
        slef.label.setText(text + "/")
    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")
    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")
    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")
    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")
    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")
    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")
    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")
    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")
    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")
    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")
    def action_clear(self):
        self.label.setText("")
    def action_del(self):
        text = self.label.text()
        a = len(text)
        b = text[:a-1]
        self.label.setText(b)
        
app = QApplication(sys.argv)
app.setStyle('Fusion')
qp = QPalette()
qp.setColor(QPalette.ButtonText,Qt.black)
qp.setColor(QPalette.Button,Qt.gray)
qp.setColor(QPalette.Window,Qt.black)
app.setPalette(qp)
window = Window()
sys.exit(app.exec())
