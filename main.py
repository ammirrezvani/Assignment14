from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from math import *
from functools import partial

class calculator(QMainWindow):
    def __init__(self):
        super().__init__() 

        loader = QUiLoader()
        self.ui = loader.load("designer.ui")
        self.ui.show()

        

        
        self.ui.pushac.clicked.connect(self.ac)
        self.ui.pushdot.clicked.connect(self.dot)
        self.ui.pushsum.clicked.connect(self.sum)
        self.ui.pushsub.clicked.connect(self.sub)
        self.ui.pushmul.clicked.connect(self.mul)
        self.ui.pushdiv.clicked.connect(self.div)
        self.ui.pushsin.clicked.connect(self.sin)
        self.ui.pushcos.clicked.connect(self.cos)
        self.ui.pushtan.clicked.connect(self.tan)
        self.ui.pushsqrt.clicked.connect(self.sqrt)
       ## self.ui.pusglog.clicked.connect(self.log)
        self.ui.pushcot.clicked.connect(self.cot)
       ## self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.pushpercent.clicked.connect(self.percent)
        self.ui.pushequal.clicked.connect(self.eq)       


        self.ui.push0.clicked.connect(partial(self.number,"0"))
        self.ui.push1.clicked.connect(partial(self.number,"1"))
        self.ui.push2.clicked.connect(partial(self.number,"2"))
        self.ui.push3.clicked.connect(partial(self.number,"3"))
        self.ui.push4.clicked.connect(partial(self.number,"4"))
        self.ui.push5.clicked.connect(partial(self.number,"5"))
        self.ui.push6.clicked.connect(partial(self.number,"6"))
        self.ui.push7.clicked.connect(partial(self.number,"7"))
        self.ui.push8.clicked.connect(partial(self.number,"8"))
        self.ui.push9.clicked.connect(partial(self.number,"9"))        


    def number(self,N):
        self.ui.textbox.setText(self.ui.textbox.text()+ N)

    def percent(self):
        self.opp = "%"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")       
        self.ui.textbox.setText(str(self.num1/100))

    def sign(self):
        self.opp = "+/-"
        self.num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(-1 * self.num))

    def sum(self):
        self.opp = "+"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def sub(self):
        self.opp = "-"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def mul(self):
        self.opp = "*"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def div(self):
        self.opp = "/"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def sin(self):
        self.opp = "sin"
        self.ui.textbox.setText("Sin ")

    def cos(self):
        self.opp = "cos"
        self.ui.textbox.setText("Cos ")

    def tan(self):
        self.opp = "tan"
        self.ui.textbox.setText("Tan ")

    def sqrt(self):
        self.opp = "sqrt"
        self.ui.textbox.setText("√ ")

    def log(self):
        self.opp = "log"
        self.ui.textbox.setText("log ")

    def cot(self):
        self.opp = "cot"
        self.ui.textbox.setText("Cot ")

    def ac(self):
        self.ui.textbox.setText("")   

    def dot(self):
        for i in self.ui.textbox.text():
            if "." in self.ui.textbox.text():
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text()+".")

    def eq(self):
        if self.opp =="+":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1+self.num2))

        if self.opp =="-":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 - self.num2))

        if self.opp =="*":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 * self.num2))

        if self.opp =="/":
            self.num2 = float(self.ui.textbox.text())
            if self.num2 !=0:
                self.ui.textbox.setText(str(self.num1/self.num2))
            else:
                self.ui.textbox.setText("Can't divide by zero")
        
        if self.opp =="sin":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(sin(radians((self.num1)))))

        if self.opp =="cos":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(cos(radians(self.num1))))

        if self.opp =="tan":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(tan(radians(self.num1))))

        if self.opp =="sqrt":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(sqrt(self.num1)))

        if self.opp =="log":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(log(self.num1)))

        if self.opp =="cot":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            if self.num1 != 0:
                cal_sin = sin(radians(self.num1))
                cal_cos = cos(radians(self.num1))
                self.ui.textbox.setText(str(cal_cos/cal_sin))
            else:
                self.ui.textbox.setText("Can't divide by zero")

app = QApplication()
calculator_main_window = calculator()
app.exec()