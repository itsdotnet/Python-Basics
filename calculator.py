from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QLabel,QLineEdit
# global
start_bool = False
light_bool = True
# main
calc = QApplication([]) # app
window = QWidget() #window
window.setGeometry(200,100,350,500) #size
window.setStyleSheet('background-color:black;color:blue') #css
window.setWindowTitle('MyCalc')
line = QLabel(window)
line.setGeometry(25,40,300,70)
line.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px;padding-top:10px;') #css line
line.setAlignment(Qt.AlignRight)
# buttons

# clear 

label_clear = QPushButton(window)
label_clear.setText('C')
label_clear.setGeometry(25,130,60,60) #size
label_clear.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px;') #css line

# backspace

label_backspace = QPushButton(window)
label_backspace.setText('<-')
label_backspace.setGeometry(265,130,60,60) #size
label_backspace.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px') #css line

# +

label_plus = QPushButton(window)
label_plus.setText('+')
label_plus.setGeometry(265,200,60,60) #size
label_plus.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')


# -

label_minus = QPushButton(window)
label_minus.setText('-')
label_minus.setGeometry(265,270,60,60) #size
label_minus.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# *

label_k = QPushButton(window)
label_k.setText('*')
label_k.setGeometry(265,340,60,60) #size
label_k.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# /

label_b = QPushButton(window)
label_b.setText('/')
label_b.setGeometry(265,410,60,60) #size
label_b.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# =

label_result = QPushButton(window)
label_result.setText('=')
label_result.setGeometry(105,410,140,60) #size
label_result.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# (

label_oldi = QPushButton(window)
label_oldi.setText('(')
label_oldi.setGeometry(105,130,60,60) #qavs
label_oldi.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')
    
# )

label_orqa = QPushButton(window)
label_orqa.setText(')')
label_orqa.setGeometry(185,130,60,60) #qavs
label_orqa.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')


# raqmalar

# 1

label_bir = QPushButton(window)
label_bir.setText('1')
label_bir.setGeometry(25,200,60,60) #size
label_bir.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 2

label_ikki = QPushButton(window)
label_ikki.setText('2')
label_ikki.setGeometry(105,200,60,60) #size
label_ikki.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 3

label_uch = QPushButton(window)
label_uch.setText('3')
label_uch.setGeometry(185,200,60,60) #size
label_uch.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 4

label_tort = QPushButton(window)
label_tort.setText('4')
label_tort.setGeometry(25,270,60,60) #size
label_tort.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 5

label_besh = QPushButton(window)
label_besh.setText('5')
label_besh.setGeometry(105,270,60,60) #size
label_besh.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 6

label_olti = QPushButton(window)
label_olti.setText('6')
label_olti.setGeometry(185,270,60,60) #size
label_olti.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 7

label_yetti = QPushButton(window)
label_yetti.setText('7')
label_yetti.setGeometry(25,340,60,60) #size
label_yetti.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 8

label_sakkiz = QPushButton(window)
label_sakkiz.setText('8')
label_sakkiz.setGeometry(105,340,60,60) #size
label_sakkiz.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 9

label_toqqiz = QPushButton(window)
label_toqqiz.setText('9')
label_toqqiz.setGeometry(185,340,60,60) #size
label_toqqiz.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# 0

label_nol = QPushButton(window)
label_nol.setText('0')
label_nol.setGeometry(25,410,60,60) #size
label_nol.setStyleSheet('background-color:white;color:black;font-size:35px;border-radius:15px')

# methots

def yoz():
    line.setText('salom')
    ...
def uchir():
    line.setText('')
def back():
    line.setText(line.text()[:-1:])
def plus():
    line.setText(f"{line.text()}+")
def minus():
    line.setText(f"{line.text()}-")
def kop():
    line.setText(f"{line.text()}*")
def bol():
    line.setText(f"{line.text()}/")
def old():
    line.setText(f"{line.text()}(")
def orqa():
    line.setText(f"{line.text()})")
    
# raqam

def raqam_1():
    line.setText(f"{line.text()}1")
def raqam_2():
    line.setText(f"{line.text()}2")
def raqam_3():
    line.setText(f"{line.text()}3")
def raqam_4():
    line.setText(f"{line.text()}4")
def raqam_5():
    line.setText(f"{line.text()}5")
def raqam_6():
    line.setText(f"{line.text()}6")
def raqam_7():
    line.setText(f"{line.text()}7")
def raqam_8():
    line.setText(f"{line.text()}8")
def raqam_9():
    line.setText(f"{line.text()}9")
def raqam_0():
    line.setText(f"{line.text()}0")
# clear

label_clear.clicked.connect(uchir)

# backspace

label_backspace.clicked.connect(back)

# +

label_plus.clicked.connect(plus)

# -

label_minus.clicked.connect(minus)

# *

label_k.clicked.connect(kop)

# /

label_b.clicked.connect(bol)

# (

label_oldi.clicked.connect(old)

# )

label_orqa.clicked.connect(orqa)

# raqamlar
label_bir.clicked.connect(raqam_1)

label_ikki.clicked.connect(raqam_2)
label_uch.clicked.connect(raqam_3)
label_tort.clicked.connect(raqam_4)
label_besh.clicked.connect(raqam_5)
label_olti.clicked.connect(raqam_6)
label_yetti.clicked.connect(raqam_7)
label_sakkiz.clicked.connect(raqam_8)
label_toqqiz.clicked.connect(raqam_9)
label_nol.clicked.connect(raqam_0)


# equal
def eq():
    try:
        line.setText(str(eval(line.text())))
    except:
        line.setText('Error')
label_result.clicked.connect(eq)

window.show()
calc.exec_()
# not pause