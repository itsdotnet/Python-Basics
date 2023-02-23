from PyQt5.QtWidgets import *
from random import choice
from PyQt5 import QtCore

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # vertical main
        self.setFixedSize(300,350)
        self.vMainlay = QVBoxLayout()
        # grid for 2048 4x4
        self.grid = QGridLayout()
        # horizontail layout for up
        self.halyup = QHBoxLayout()
        # horizontial layout for new game and close
        self.hlay = QHBoxLayout()
        # horizontail for right down up
        self.hbtnlay = QHBoxLayout()
        # button for close and new game
        self.but_new = QPushButton("New Game")
        self.but_new.clicked.connect(self.reset)
        self.but_close = QPushButton("Close")
        self.but_close.clicked.connect(self.close)
        # KEY
        self.up = QPushButton('up')
        self.up.clicked.connect(self.up_move)
        self.left = QPushButton('left')
        self.left.clicked.connect(self.left_move)
        self.down = QPushButton('down')
        self.down.clicked.connect(self.down_move)
        self.right = QPushButton('right')
        self.right.clicked.connect(self.right_move)
        
        # label 
        self.lbl1 = QLabel()
        self.lbl2 = QLabel()
        self.lbl3 = QLabel()
        self.lbl4 = QLabel()
        self.lbl5 = QLabel()
        self.lbl6 = QLabel()
        self.lbl7 = QLabel()
        self.lbl8 = QLabel()
        self.lbl9 = QLabel()
        self.lbl10 = QLabel()
        self.lbl11 = QLabel()
        self.lbl12 = QLabel()
        self.lbl13 = QLabel()
        self.lbl14 = QLabel()
        self.lbl15 = QLabel()
        self.lbl16 = QLabel()
        self.lsl = [self.lbl1,self.lbl2,self.lbl3,self.lbl4,self.lbl5,self.lbl6,self.lbl7,self.lbl8,self.lbl9,self.lbl10,self.lbl11,self.lbl12,self.lbl13,self.lbl14,self.lbl15,self.lbl16]
        index = 0
        for i in range(4):
            for j in range(4):
                self.grid.addWidget(self.lsl[index],i,j)
                self.lsl[index].setStyleSheet('background-color:white;border-radius:5px;font-size:20px;')
                self.lsl[index].setAlignment(QtCore.Qt.AlignCenter)
                
                index+=1

        # add layout
        self.hlay.addWidget(self.but_new)
        self.hlay.addWidget(self.but_close)
        self.hbtnlay.addWidget(self.left)
        self.hbtnlay.addWidget(self.down)
        self.hbtnlay.addWidget(self.right)
        self.halyup.addWidget(self.up)
        self.vMainlay.addLayout(self.grid)
        self.vMainlay.addLayout(self.halyup)
        self.vMainlay.addLayout(self.hbtnlay)
        self.vMainlay.addLayout(self.hlay)
        
        self.setLayout(self.vMainlay)
    # method new game
    def reset(self):
        for i in self.lsl:
            i.clear()
        self.generate()
    
    def generate(self):
        co = True
        while co:
            self.catch = choice(self.lsl)
            if self.catch.text()=='':
                self.catch.setText('2')
                break
               
# ===================================================================================================================  
    def left_move(self):
        if self.lbl4.text()!='' and self.lbl4.text()==self.lbl3.text():
            try:
                self.lbl3.setText(str(f"{int(self.lbl4.text())+int(self.lbl3.text())}"))
                self.lbl4.clear()
                
            except:
                ...
        elif self.lbl2.text()!='' and self.lbl2.text()==self.lbl1.text():
            try:
                self.lbl1.setText(str(f"{int(self.lbl2.text())+int(self.lbl1.text())}"))
                self.lbl2.clear()
                
            except:
                ...
            
        elif self.lbl3.text()!='' and self.lbl3.text()==self.lbl2.text():
            try:
                self.lbl2.setText(str(f"{int(self.lbl3.text())+int(self.lbl2.text())}"))
                self.lbl3.clear()
                
            except:
                ...
        elif self.lbl4.text()==self.lbl2.text() and self.lbl3.text()=='':
            try:
                self.lbl2.setText(str(f"{int(self.lbl4.text())+int(self.lbl2.text())}"))
                self.lbl4.clear()
                
            except:
                ...
        elif self.lbl3.text()==self.lbl1.text() and self.lbl2.text()=='':
            try:
                self.lbl1.setText(str(f"{int(self.lbl3.text())+int(self.lbl1.text())}"))
                self.lbl3.clear()
                
            except:
                ...
        elif self.lbl4.text()==self.lbl1.text() and self.lbl2.text()=='' and self.lbl3.text()=='':
            try:
                self.lbl1.setText(str(f"{int(self.lbl4.text())+int(self.lbl1.text())}"))
                self.lbl4.clear()
                
            except:
                ...
        if self.lbl1.text()=='':
            self.lbl1.setText(self.lbl2.text())
            self.lbl2.setText(self.lbl3.text())
            self.lbl3.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl2.text()=='':
            self.lbl2.setText(self.lbl3.text())
            self.lbl3.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl1.text()=='':
            self.lbl1.setText(self.lbl2.text())
            self.lbl2.setText(self.lbl3.text())
            self.lbl3.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl3.text()=='':
            self.lbl3.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl2.text()=='':
            self.lbl2.setText(self.lbl3.text())
            self.lbl3.setText(self.lbl4.text())
            self.lbl4.clear()
        # qator 2 =================================================================================================
        
        if self.lbl8.text()!='' and self.lbl8.text()==self.lbl7.text():
            try:
                self.lbl7.setText(str(f"{int(self.lbl8.text())+int(self.lbl7.text())}"))
                self.lbl8.clear()
            
            except:
                ...
        elif self.lbl6.text()!='' and self.lbl6.text()==self.lbl5.text():
            try:
                self.lbl5.setText(str(f"{int(self.lbl6.text())+int(self.lbl5.text())}"))
                self.lbl6.clear()
            
            except:
                ...
            
        elif self.lbl7.text()!='' and self.lbl7.text()==self.lbl6.text():
            try:
                self.lbl6.setText(str(f"{int(self.lbl7.text())+int(self.lbl6.text())}"))
                self.lbl7.clear()
            
            except:
                ...
        elif self.lbl8.text()==self.lbl6.text() and self.lbl7.text()=='' and self.lbl8.text()!='':
            try:
                self.lbl6.setText(str(f"{int(self.lbl8.text())+int(self.lbl6.text())}"))
                self.lbl8.clear()
            
            except:
                ...
        elif self.lbl7.text()==self.lbl5.text() and self.lbl6.text()=='' and self.lbl7.text()!="":
            try:
                self.lbl5.setText(str(f"{int(self.lbl7.text())+int(self.lbl5.text())}"))
                self.lbl7.clear()
            
            except:
                ...
        elif self.lbl8.text()==self.lbl5.text() and self.lbl6.text()=='' and self.lbl7.text()=='':
            try:
                self.lbl5.setText(str(f"{int(self.lbl8.text())+int(self.lbl5.text())}"))
                self.lbl8.clear()
            
            except:
                ...
        if self.lbl5.text()=='':
            self.lbl5.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl8.text())
            self.lbl8.clear()
        if self.lbl6.text()=='':
            self.lbl6.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl8.text())
            self.lbl8.clear()
        if self.lbl5.text()=='':
            self.lbl5.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl8.text())
            self.lbl8.clear()
        if self.lbl7.text()=='':
            self.lbl7.setText(self.lbl8.text())
            self.lbl8.clear()
        if self.lbl6.text()=='':
            self.lbl6.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl8.text())
            self.lbl8.clear()
        # qator 3 ===============================================================================================
        if self.lbl12.text()!='' and self.lbl12.text()==self.lbl11.text():
            try:
                self.lbl11.setText(str(f"{int(self.lbl12.text())+int(self.lbl11.text())}"))
                self.lbl12.clear()
            
            except:
                ...
        elif self.lbl10.text()!='' and self.lbl10.text()==self.lbl9.text():
            try:
                self.lbl9.setText(str(f"{int(self.lbl10.text())+int(self.lbl9.text())}"))
                self.lbl10.clear()
            
            except:
                ...
            
        elif self.lbl11.text()!='' and self.lbl11.text()==self.lbl10.text():
            try:
                self.lbl10.setText(str(f"{int(self.lbl11.text())+int(self.lbl10.text())}"))
                self.lbl11.clear()
            
            except:
                ...
        elif self.lbl12.text()==self.lbl10.text() and self.lbl11.text()=='':
            try:
                self.lbl10.setText(str(f"{int(self.lbl12.text())+int(self.lbl10.text())}"))
                self.lbl12.clear()
            
            except:
                ...
        elif self.lbl11.text()==self.lbl9.text() and self.lbl10.text()=='':
            try:
                self.lbl9.setText(str(f"{int(self.lbl11.text())+int(self.lbl9.text())}"))
                self.lbl11.clear()
            
            except:
                ...
        elif self.lbl12.text()==self.lbl9.text() and self.lbl10.text()=='' and self.lbl11.text()=='':
            try:
                self.lbl9.setText(str(f"{int(self.lbl12.text())+int(self.lbl9.text())}"))
                self.lbl12.clear()
            
            except:
                ...
        if self.lbl9.text()=='':
            self.lbl9.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl12.text())
            self.lbl12.clear()
        
        if self.lbl10.text()=='':
            self.lbl10.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl12.text())
            self.lbl12.clear()
        if self.lbl9.text()=='':
            self.lbl9.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl12.text())
            self.lbl12.clear()
        if self.lbl10.text()=='':
            self.lbl10.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl12.text())
            self.lbl12.clear()
        if self.lbl11.text()=='':
            self.lbl11.setText(self.lbl12.text())
            self.lbl12.clear()
        # qator 4 ================================================================================================
        if self.lbl16.text()!='' and self.lbl16.text()==self.lbl15.text():
            try:
                self.lbl15.setText(str(f"{int(self.lbl16.text())+int(self.lbl15.text())}"))
                self.lbl16.clear()
            
            except:
                ...
        elif self.lbl14.text()!='' and self.lbl14.text()==self.lbl13.text():
            try:
                self.lbl13.setText(str(f"{int(self.lbl14.text())+int(self.lbl13.text())}"))
                self.lbl14.clear()
            
            except:
                ...
            
        elif self.lbl15.text()!='' and self.lbl15.text()==self.lbl14.text():
            try:
                self.lbl14.setText(str(f"{int(self.lbl15.text())+int(self.lbl14.text())}"))
                self.lbl15.clear()
            
            except:
                ...
        elif self.lbl16.text()==self.lbl14.text() and self.lbl15.text()=='':
            try:
                self.lbl14.setText(str(f"{int(self.lbl16.text())+int(self.lbl14.text())}"))
                self.lbl16.clear()
            
            except:
                ...
        elif self.lbl15.text()==self.lbl13.text() and self.lbl14.text()=='':
            try:
                self.lbl13.setText(str(f"{int(self.lbl15.text())+int(self.lbl13.text())}"))
                self.lbl15.clear()
            
            except:
                ...
        elif self.lbl16.text()==self.lbl13.text() and self.lbl14.text()=='' and self.lbl15.text()=='':
            try:
                self.lbl13.setText(str(f"{int(self.lbl16.text())+int(self.lbl13.text())}"))
                self.lbl16.clear()
            except:
                ...
        if self.lbl13.text()=='':
            self.lbl13.setText(self.lbl14.text())
            self.lbl14.setText(self.lbl15.text())
            self.lbl15.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl14.text()=='':
            self.lbl14.setText(self.lbl15.text())
            self.lbl15.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl13.text()=='':
            self.lbl13.setText(self.lbl14.text())
            self.lbl14.setText(self.lbl15.text())
            self.lbl15.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl14.text()=='':
            self.lbl14.setText(self.lbl15.text())
            self.lbl15.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl15.text()=='':
            self.lbl15.setText(self.lbl16.text())
            self.lbl16.clear()
        self.over()
        self.generate()
# ===================================================================================================================  
    def down_move(self):
        # qator 1 =====================================================================================================
        
        if self.lbl1.text()!='' and self.lbl1.text()==self.lbl5.text():
            try:
                self.lbl5.setText(str(f"{int(self.lbl1.text())+int(self.lbl5.text())}"))
                self.lbl1.clear()
                
            except:
                ...
        elif self.lbl9.text()!='' and self.lbl9.text()==self.lbl13.text():
            try:
                self.lbl13.setText(str(f"{int(self.lbl9.text())+int(self.lbl13.text())}"))
                self.lbl9.clear()
                
            except:
                ...
            
        elif self.lbl5.text()!='' and self.lbl5.text()==self.lbl9.text():
            try:
                self.lbl9.setText(str(f"{int(self.lbl5.text())+int(self.lbl9.text())}"))
                self.lbl5.clear()
                
            except:
                ...
        elif self.lbl1.text()==self.lbl9.text() and self.lbl5.text()=='':
            try:
                self.lbl9.setText(str(f"{int(self.lbl1.text())+int(self.lbl9.text())}"))
                self.lbl1.clear()
                
            except:
                ...
        elif self.lbl5.text()==self.lbl13.text() and self.lbl9.text()=='':
            try:
                self.lbl13.setText(str(f"{int(self.lbl5.text())+int(self.lbl13.text())}"))
                self.lbl5.clear()
                
            except:
                ...
        elif self.lbl1.text()==self.lbl13.text() and self.lbl9.text()=='' and self.lbl5.text()=='':
            try:
                self.lbl13.setText(str(f"{int(self.lbl1.text())+int(self.lbl13.text())}"))
                self.lbl1.clear()
                
            except:
                ...
        if self.lbl13.text()=='':
            self.lbl13.setText(self.lbl9.text())
            self.lbl9.setText(self.lbl5.text())
            self.lbl5.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl9.text()=='':
            self.lbl9.setText(self.lbl5.text())
            self.lbl5.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl13.text()=='':
            self.lbl13.setText(self.lbl9.text())
            self.lbl9.setText(self.lbl5.text())
            self.lbl5.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl5.text()=='':
            self.lbl5.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl9.text()=='':
            self.lbl9.setText(self.lbl5.text())
            self.lbl5.setText(self.lbl1.text())
            self.lbl1.clear()
        # qator 2 =================================================================================================
        if self.lbl2.text()!='' and self.lbl2.text()==self.lbl6.text():
            try:
                self.lbl6.setText(str(f"{int(self.lbl2.text())+int(self.lbl6.text())}"))
                self.lbl2.clear()
            
            except:
                ...
        elif self.lbl10.text()!='' and self.lbl10.text()==self.lbl14.text():
            try:
                self.lbl14.setText(str(f"{int(self.lbl10.text())+int(self.lbl14.text())}"))
                self.lbl10.clear()
            
            except:
                ...
            
        elif self.lbl6.text()!='' and self.lbl6.text()==self.lbl10.text():
            try:
                self.lbl10.setText(str(f"{int(self.lbl6.text())+int(self.lbl10.text())}"))
                self.lbl6.clear()
            
            except:
                ...
        elif self.lbl2.text()==self.lbl10.text() and self.lbl6.text()=='' and self.lbl2.text()!='':
            try:
                self.lbl10.setText(str(f"{int(self.lbl2.text())+int(self.lbl10.text())}"))
                self.lbl2.clear()
            
            except:
                ...
        elif self.lbl6.text()==self.lbl14.text() and self.lbl10.text()=='' and self.lbl6.text()!="":
            try:
                self.lbl14.setText(str(f"{int(self.lbl6.text())+int(self.lbl14.text())}"))
                self.lbl6.clear()
            
            except:
                ...
        elif self.lbl2.text()==self.lbl14.text() and self.lbl10.text()=='' and self.lbl6.text()=='':
            try:
                self.lbl14.setText(str(f"{int(self.lbl2.text())+int(self.lbl14.text())}"))
                self.lbl2.clear()
            
            except:
                ...
        if self.lbl14.text()=='':
            self.lbl14.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl2.text())
            self.lbl2.clear()
        if self.lbl10.text()=='':
            self.lbl10.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl2.text())
            self.lbl2.clear()
        if self.lbl14.text()=='':
            self.lbl14.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl2.text())
            self.lbl2.clear()
        if self.lbl6.text()=='':
            self.lbl6.setText(self.lbl2.text())
            self.lbl2.clear()
        if self.lbl10.text()=='':
            self.lbl10.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl2.text())
            self.lbl2.clear()
        # qator 3 ===============================================================================================
        if self.lbl3.text()!='' and self.lbl3.text()==self.lbl7.text():
            try:
                self.lbl7.setText(str(f"{int(self.lbl3.text())+int(self.lbl7.text())}"))
                self.lbl3.clear()
            
            except:
                ...
        elif self.lbl11.text()!='' and self.lbl11.text()==self.lbl15.text():
            try:
                self.lbl15.setText(str(f"{int(self.lbl11.text())+int(self.lbl15.text())}"))
                self.lbl11.clear()
            
            except:
                ...
            
        elif self.lbl7.text()!='' and self.lbl7.text()==self.lbl11.text():
            try:
                self.lbl11.setText(str(f"{int(self.lbl7.text())+int(self.lbl11.text())}"))
                self.lbl7.clear()
            
            except:
                ...
        elif self.lbl3.text()==self.lbl11.text() and self.lbl7.text()=='':
            try:
                self.lbl11.setText(str(f"{int(self.lbl3.text())+int(self.lbl11.text())}"))
                self.lbl3.clear()
            
            except:
                ...
        elif self.lbl7.text()==self.lbl15.text() and self.lbl11.text()=='':
            try:
                self.lbl15.setText(str(f"{int(self.lbl7.text())+int(self.lbl15.text())}"))
                self.lbl7.clear()
            
            except:
                ...
        elif self.lbl3.text()==self.lbl15.text() and self.lbl11.text()=='' and self.lbl7.text()=='':
            try:
                self.lbl15.setText(str(f"{int(self.lbl3.text())+int(self.lbl15.text())}"))
                self.lbl3.clear()
            
            except:
                ...
        if self.lbl15.text()=='':
            self.lbl15.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl3.text())
            self.lbl3.clear()
        
        if self.lbl11.text()=='':
            self.lbl11.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl3.text())
            self.lbl3.clear()
        if self.lbl15.text()=='':
            self.lbl15.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl3.text())
            self.lbl3.clear()
        if self.lbl11.text()=='':
            self.lbl11.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl3.text())
            self.lbl3.clear()
        if self.lbl7.text()=='':
            self.lbl7.setText(self.lbl3.text())
            self.lbl3.clear()
        # qator 4 ================================================================================================
        if self.lbl4.text()!='' and self.lbl4.text()==self.lbl8.text():
            try:
                self.lbl8.setText(str(f"{int(self.lbl4.text())+int(self.lbl8.text())}"))
                self.lbl4.clear()
            
            except:
                ...
        elif self.lbl12.text()!='' and self.lbl12.text()==self.lbl16.text():
            try:
                self.lbl16.setText(str(f"{int(self.lbl12.text())+int(self.lbl16.text())}"))
                self.lbl12.clear()
            
            except:
                ...
            
        elif self.lbl8.text()!='' and self.lbl8.text()==self.lbl12.text():
            try:
                self.lbl12.setText(str(f"{int(self.lbl8.text())+int(self.lbl12.text())}"))
                self.lbl8.clear()
            
            except:
                ...
        elif self.lbl4.text()==self.lbl12.text() and self.lbl8.text()=='':
            try:
                self.lbl12.setText(str(f"{int(self.lbl4.text())+int(self.lbl12.text())}"))
                self.lbl4.clear()
            
            except:
                ...
        elif self.lbl8.text()==self.lbl16.text() and self.lbl12.text()=='':
            try:
                self.lbl16.setText(str(f"{int(self.lbl8.text())+int(self.lbl16.text())}"))
                self.lbl8.clear()
            
            except:
                ...
        elif self.lbl4.text()==self.lbl16.text() and self.lbl12.text()=='' and self.lbl8.text()=='':
            try:
                self.lbl16.setText(str(f"{int(self.lbl4.text())+int(self.lbl16.text())}"))
                self.lbl4.clear()
            except:
                ...
        if self.lbl16.text()=='':
            self.lbl16.setText(self.lbl12.text())
            self.lbl12.setText(self.lbl8.text())
            self.lbl8.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl12.text()=='':
            self.lbl12.setText(self.lbl8.text())
            self.lbl8.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl16.text()=='':
            self.lbl16.setText(self.lbl12.text())
            self.lbl12.setText(self.lbl8.text())
            self.lbl8.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl12.text()=='':
            self.lbl12.setText(self.lbl8.text())
            self.lbl8.setText(self.lbl4.text())
            self.lbl4.clear()
        if self.lbl8.text()=='':
            self.lbl8.setText(self.lbl4.text())
            self.lbl4.clear()
        self.over()
        self.generate()
    
    def right_move(self):
        # qator 1 =====================================================================================================
        
        if self.lbl1.text()!='' and self.lbl1.text()==self.lbl2.text():
            try:
                self.lbl2.setText(str(f"{int(self.lbl1.text())+int(self.lbl2.text())}"))
                self.lbl1.clear()
                
            except:
                ...
        elif self.lbl3.text()!='' and self.lbl3.text()==self.lbl4.text():
            try:
                self.lbl4.setText(str(f"{int(self.lbl3.text())+int(self.lbl4.text())}"))
                self.lbl3.clear()
                
            except:
                ...
            
        elif self.lbl2.text()!='' and self.lbl2.text()==self.lbl3.text():
            try:
                self.lbl3.setText(str(f"{int(self.lbl2.text())+int(self.lbl3.text())}"))
                self.lbl2.clear()
                
            except:
                ...
        elif self.lbl1.text()==self.lbl3.text() and self.lbl2.text()=='':
            try:
                self.lbl3.setText(str(f"{int(self.lbl1.text())+int(self.lbl3.text())}"))
                self.lbl1.clear()
                
            except:
                ...
        elif self.lbl2.text()==self.lbl4.text() and self.lbl3.text()=='':
            try:
                self.lbl4.setText(str(f"{int(self.lbl2.text())+int(self.lbl4.text())}"))
                self.lbl2.clear()
                
            except:
                ...
        elif self.lbl1.text()==self.lbl4.text() and self.lbl3.text()=='' and self.lbl2.text()=='':
            try:
                self.lbl4.setText(str(f"{int(self.lbl1.text())+int(self.lbl4.text())}"))
                self.lbl1.clear()
                
            except:
                ...
        if self.lbl4.text()=='':
            self.lbl4.setText(self.lbl3.text())
            self.lbl3.setText(self.lbl2.text())
            self.lbl2.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl3.text()=='':
            self.lbl3.setText(self.lbl2.text())
            self.lbl2.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl4.text()=='':
            self.lbl4.setText(self.lbl3.text())
            self.lbl3.setText(self.lbl2.text())
            self.lbl2.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl2.text()=='':
            self.lbl2.setText(self.lbl1.text())
            self.lbl1.clear()
        if self.lbl3.text()=='':
            self.lbl3.setText(self.lbl2.text())
            self.lbl2.setText(self.lbl1.text())
            self.lbl1.clear()
        # qator 2 =================================================================================================
        if self.lbl5.text()!='' and self.lbl5.text()==self.lbl6.text():
            try:
                self.lbl6.setText(str(f"{int(self.lbl5.text())+int(self.lbl6.text())}"))
                self.lbl5.clear()
            
            except:
                ...
        elif self.lbl7.text()!='' and self.lbl7.text()==self.lbl8.text():
            try:
                self.lbl8.setText(str(f"{int(self.lbl7.text())+int(self.lbl8.text())}"))
                self.lbl7.clear()
            
            except:
                ...
            
        elif self.lbl6.text()!='' and self.lbl6.text()==self.lbl7.text():
            try:
                self.lbl7.setText(str(f"{int(self.lbl6.text())+int(self.lbl7.text())}"))
                self.lbl6.clear()
            
            except:
                ...
        elif self.lbl5.text()==self.lbl7.text() and self.lbl6.text()=='' and self.lbl5.text()!='':
            try:
                self.lbl7.setText(str(f"{int(self.lbl5.text())+int(self.lbl7.text())}"))
                self.lbl5.clear()
            
            except:
                ...
        elif self.lbl6.text()==self.lbl8.text() and self.lbl7.text()=='' and self.lbl6.text()!="":
            try:
                self.lbl8.setText(str(f"{int(self.lbl6.text())+int(self.lbl8.text())}"))
                self.lbl6.clear()
            
            except:
                ...
        elif self.lbl5.text()==self.lbl8.text() and self.lbl7.text()=='' and self.lbl6.text()=='':
            try:
                self.lbl8.setText(str(f"{int(self.lbl5.text())+int(self.lbl8.text())}"))
                self.lbl5.clear()
            
            except:
                ...
        if self.lbl8.text()=='':
            self.lbl8.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl5.text())
            self.lbl5.clear()
        if self.lbl7.text()=='':
            self.lbl7.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl5.text())
            self.lbl5.clear()
        if self.lbl8.text()=='':
            self.lbl8.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl5.text())
            self.lbl5.clear()
        if self.lbl6.text()=='':
            self.lbl6.setText(self.lbl5.text())
            self.lbl5.clear()
        if self.lbl7.text()=='':
            self.lbl7.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl5.text())
            self.lbl5.clear()
        # qator 3 ===============================================================================================
        if self.lbl9.text()!='' and self.lbl9.text()==self.lbl10.text():
            try:
                self.lbl10.setText(str(f"{int(self.lbl9.text())+int(self.lbl10.text())}"))
                self.lbl9.clear()
            
            except:
                ...
        elif self.lbl11.text()!='' and self.lbl11.text()==self.lbl12.text():
            try:
                self.lbl12.setText(str(f"{int(self.lbl11.text())+int(self.lbl12.text())}"))
                self.lbl11.clear()
            
            except:
                ...
            
        elif self.lbl10.text()!='' and self.lbl10.text()==self.lbl11.text():
            try:
                self.lbl11.setText(str(f"{int(self.lbl10.text())+int(self.lbl11.text())}"))
                self.lbl10.clear()
            
            except:
                ...
        elif self.lbl9.text()==self.lbl11.text() and self.lbl10.text()=='':
            try:
                self.lbl11.setText(str(f"{int(self.lbl9.text())+int(self.lbl11.text())}"))
                self.lbl9.clear()
            
            except:
                ...
        elif self.lbl10.text()==self.lbl12.text() and self.lbl11.text()=='':
            try:
                self.lbl12.setText(str(f"{int(self.lbl10.text())+int(self.lbl12.text())}"))
                self.lbl10.clear()
            
            except:
                ...
        elif self.lbl9.text()==self.lbl12.text() and self.lbl11.text()=='' and self.lbl10.text()=='':
            try:
                self.lbl12.setText(str(f"{int(self.lbl9.text())+int(self.lbl12.text())}"))
                self.lbl9.clear()
            
            except:
                ...
        if self.lbl12.text()=='':
            self.lbl12.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl9.text())
            self.lbl9.clear()
        
        if self.lbl11.text()=='':
            self.lbl11.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl9.text())
            self.lbl9.clear()
        if self.lbl12.text()=='':
            self.lbl12.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl9.text())
            self.lbl9.clear()
        if self.lbl11.text()=='':
            self.lbl11.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl9.text())
            self.lbl9.clear()
        if self.lbl10.text()=='':
            self.lbl10.setText(self.lbl9.text())
            self.lbl9.clear()
        # qator 4 ================================================================================================
        if self.lbl13.text()!='' and self.lbl13.text()==self.lbl14.text():
            try:
                self.lbl14.setText(str(f"{int(self.lbl13.text())+int(self.lbl14.text())}"))
                self.lbl13.clear()
            
            except:
                ...
        elif self.lbl15.text()!='' and self.lbl15.text()==self.lbl16.text():
            try:
                self.lbl16.setText(str(f"{int(self.lbl15.text())+int(self.lbl16.text())}"))
                self.lbl15.clear()
            
            except:
                ...
            
        elif self.lbl14.text()!='' and self.lbl14.text()==self.lbl15.text():
            try:
                self.lbl15.setText(str(f"{int(self.lbl14.text())+int(self.lbl15.text())}"))
                self.lbl14.clear()
            
            except:
                ...
        elif self.lbl13.text()==self.lbl15.text() and self.lbl14.text()=='':
            try:
                self.lbl15.setText(str(f"{int(self.lbl13.text())+int(self.lbl15.text())}"))
                self.lbl13.clear()
            
            except:
                ...
        elif self.lbl14.text()==self.lbl16.text() and self.lbl15.text()=='':
            try:
                self.lbl16.setText(str(f"{int(self.lbl14.text())+int(self.lbl16.text())}"))
                self.lbl14.clear()
            
            except:
                ...
        elif self.lbl13.text()==self.lbl16.text() and self.lbl15.text()=='' and self.lbl14.text()=='':
            try:
                self.lbl16.setText(str(f"{int(self.lbl13.text())+int(self.lbl16.text())}"))
                self.lbl13.clear()
            except:
                ...
        if self.lbl16.text()=='':
            self.lbl16.setText(self.lbl15.text())
            self.lbl15.setText(self.lbl14.text())
            self.lbl14.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl15.text()=='':
            self.lbl15.setText(self.lbl14.text())
            self.lbl14.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl16.text()=='':
            self.lbl16.setText(self.lbl15.text())
            self.lbl15.setText(self.lbl14.text())
            self.lbl14.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl15.text()=='':
            self.lbl15.setText(self.lbl14.text())
            self.lbl14.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl14.text()=='':
            self.lbl14.setText(self.lbl13.text())
            self.lbl13.clear()
        self.over()
        self.generate()
    
    def up_move(self):
        # qator 1 =====================================================================================================
        
        if self.lbl13.text()!='' and self.lbl13.text()==self.lbl9.text():
            try:
                self.lbl9.setText(str(f"{int(self.lbl13.text())+int(self.lbl9.text())}"))
                self.lbl13.clear()
                
            except:
                ...
        elif self.lbl5.text()!='' and self.lbl5.text()==self.lbl1.text():
            try:
                self.lbl1.setText(str(f"{int(self.lbl5.text())+int(self.lbl1.text())}"))
                self.lbl5.clear()
                
            except:
                ...
            
        elif self.lbl9.text()!='' and self.lbl9.text()==self.lbl5.text():
            try:
                self.lbl5.setText(str(f"{int(self.lbl9.text())+int(self.lbl5.text())}"))
                self.lbl9.clear()
                
            except:
                ...
        elif self.lbl13.text()==self.lbl5.text() and self.lbl9.text()=='':
            try:
                self.lbl5.setText(str(f"{int(self.lbl13.text())+int(self.lbl5.text())}"))
                self.lbl13.clear()
                
            except:
                ...
        elif self.lbl9.text()==self.lbl1.text() and self.lbl5.text()=='':
            try:
                self.lbl1.setText(str(f"{int(self.lbl9.text())+int(self.lbl1.text())}"))
                self.lbl9.clear()
                
            except:
                ...
        elif self.lbl13.text()==self.lbl1.text() and self.lbl5.text()=='' and self.lbl9.text()=='':
            try:
                self.lbl1.setText(str(f"{int(self.lbl13.text())+int(self.lbl1.text())}"))
                self.lbl13.clear()
                
            except:
                ...
        if self.lbl1.text()=='':
            self.lbl1.setText(self.lbl5.text())
            self.lbl5.setText(self.lbl9.text())
            self.lbl9.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl5.text()=='':
            self.lbl5.setText(self.lbl9.text())
            self.lbl9.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl1.text()=='':
            self.lbl1.setText(self.lbl5.text())
            self.lbl5.setText(self.lbl9.text())
            self.lbl9.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl9.text()=='':
            self.lbl9.setText(self.lbl13.text())
            self.lbl13.clear()
        if self.lbl5.text()=='':
            self.lbl5.setText(self.lbl9.text())
            self.lbl9.setText(self.lbl13.text())
            self.lbl13.clear()
        # qator 2 =================================================================================================
        if self.lbl14.text()!='' and self.lbl14.text()==self.lbl10.text():
            try:
                self.lbl10.setText(str(f"{int(self.lbl14.text())+int(self.lbl10.text())}"))
                self.lbl14.clear()
            
            except:
                ...
        elif self.lbl6.text()!='' and self.lbl6.text()==self.lbl2.text():
            try:
                self.lbl2.setText(str(f"{int(self.lbl6.text())+int(self.lbl2.text())}"))
                self.lbl6.clear()
            
            except:
                ...
            
        elif self.lbl10.text()!='' and self.lbl10.text()==self.lbl6.text():
            try:
                self.lbl6.setText(str(f"{int(self.lbl10.text())+int(self.lbl6.text())}"))
                self.lbl10.clear()
            
            except:
                ...
        elif self.lbl14.text()==self.lbl6.text() and self.lbl10.text()=='' and self.lbl14.text()!='':
            try:
                self.lbl6.setText(str(f"{int(self.lbl14.text())+int(self.lbl6.text())}"))
                self.lbl14.clear()
            
            except:
                ...
        elif self.lbl10.text()==self.lbl2.text() and self.lbl6.text()=='' and self.lbl10.text()!="":
            try:
                self.lbl2.setText(str(f"{int(self.lbl10.text())+int(self.lbl2.text())}"))
                self.lbl10.clear()
            
            except:
                ...
        elif self.lbl14.text()==self.lbl2.text() and self.lbl6.text()=='' and self.lbl10.text()=='':
            try:
                self.lbl2.setText(str(f"{int(self.lbl14.text())+int(self.lbl2.text())}"))
                self.lbl14.clear()
            
            except:
                ...
        if self.lbl2.text()=='':
            self.lbl2.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl14.text())
            self.lbl14.clear()
        if self.lbl6.text()=='':
            self.lbl6.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl14.text())
            self.lbl14.clear()
        if self.lbl2.text()=='':
            self.lbl2.setText(self.lbl6.text())
            self.lbl6.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl14.text())
            self.lbl14.clear()
        if self.lbl10.text()=='':
            self.lbl10.setText(self.lbl14.text())
            self.lbl14.clear()
        if self.lbl6.text()=='':
            self.lbl6.setText(self.lbl10.text())
            self.lbl10.setText(self.lbl14.text())
            self.lbl14.clear()
         # qator 3 ===============================================================================================
        if self.lbl15.text()!='' and self.lbl15.text()==self.lbl11.text():
            try:
                self.lbl11.setText(str(f"{int(self.lbl15.text())+int(self.lbl11.text())}"))
                self.lbl15.clear()
            
            except:
                ...
        elif self.lbl7.text()!='' and self.lbl7.text()==self.lbl3.text():
            try:
                self.lbl3.setText(str(f"{int(self.lbl7.text())+int(self.lbl3.text())}"))
                self.lbl7.clear()
            
            except:
                ...
            
        elif self.lbl11.text()!='' and self.lbl11.text()==self.lbl7.text():
            try:
                self.lbl7.setText(str(f"{int(self.lbl11.text())+int(self.lbl7.text())}"))
                self.lbl11.clear()
            
            except:
                ...
        elif self.lbl15.text()==self.lbl7.text() and self.lbl11.text()=='':
            try:
                self.lbl7.setText(str(f"{int(self.lbl15.text())+int(self.lbl7.text())}"))
                self.lbl15.clear()
            
            except:
                ...
        elif self.lbl11.text()==self.lbl3.text() and self.lbl7.text()=='':
            try:
                self.lbl3.setText(str(f"{int(self.lbl11.text())+int(self.lbl3.text())}"))
                self.lbl11.clear()
            
            except:
                ...
        elif self.lbl15.text()==self.lbl3.text() and self.lbl7.text()=='' and self.lbl11.text()=='':
            try:
                self.lbl3.setText(str(f"{int(self.lbl15.text())+int(self.lbl3.text())}"))
                self.lbl15.clear()
            
            except:
                ...
        if self.lbl3.text()=='':
            self.lbl3.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl15.text())
            self.lbl15.clear()
        
        if self.lbl7.text()=='':
            self.lbl7.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl15.text())
            self.lbl15.clear()
        if self.lbl3.text()=='':
            self.lbl3.setText(self.lbl7.text())
            self.lbl7.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl15.text())
            self.lbl15.clear()
        if self.lbl7.text()=='':
            self.lbl7.setText(self.lbl11.text())
            self.lbl11.setText(self.lbl15.text())
            self.lbl15.clear()
        if self.lbl11.text()=='':
            self.lbl11.setText(self.lbl15.text())
            self.lbl15.clear()
        # qator 4 ================================================================================================
        if self.lbl16.text()!='' and self.lbl16.text()==self.lbl12.text():
            try:
                self.lbl12.setText(str(f"{int(self.lbl16.text())+int(self.lbl12.text())}"))
                self.lbl16.clear()
            
            except:
                ...
        elif self.lbl8.text()!='' and self.lbl8.text()==self.lbl4.text():
            try:
                self.lbl4.setText(str(f"{int(self.lbl8.text())+int(self.lbl4.text())}"))
                self.lbl8.clear()
            
            except:
                ...
            
        elif self.lbl12.text()!='' and self.lbl12.text()==self.lbl8.text():
            try:
                self.lbl8.setText(str(f"{int(self.lbl12.text())+int(self.lbl8.text())}"))
                self.lbl12.clear()
            
            except:
                ...
        elif self.lbl16.text()==self.lbl8.text() and self.lbl12.text()=='':
            try:
                self.lbl8.setText(str(f"{int(self.lbl16.text())+int(self.lbl8.text())}"))
                self.lbl16.clear()
            
            except:
                ...
        elif self.lbl12.text()==self.lbl4.text() and self.lbl8.text()=='':
            try:
                self.lbl4.setText(str(f"{int(self.lbl12.text())+int(self.lbl4.text())}"))
                self.lbl12.clear()
            
            except:
                ...
        elif self.lbl16.text()==self.lbl4.text() and self.lbl8.text()=='' and self.lbl12.text()=='':
            try:
                self.lbl4.setText(str(f"{int(self.lbl16.text())+int(self.lbl4.text())}"))
                self.lbl16.clear()
            except:
                ...
        if self.lbl4.text()=='':
            self.lbl4.setText(self.lbl8.text())
            self.lbl8.setText(self.lbl12.text())
            self.lbl12.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl8.text()=='':
            self.lbl8.setText(self.lbl12.text())
            self.lbl12.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl4.text()=='':
            self.lbl4.setText(self.lbl8.text())
            self.lbl8.setText(self.lbl12.text())
            self.lbl12.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl8.text()=='':
            self.lbl8.setText(self.lbl12.text())
            self.lbl12.setText(self.lbl16.text())
            self.lbl16.clear()
        if self.lbl12.text()=='':
            self.lbl12.setText(self.lbl16.text())
            self.lbl16.clear()
        self.over()
        self.generate()
        
    def over(self):
        sana = 0
        max = 2
        for i in self.lsl:
            if i.text()!='':
                sana+=1
                if max<int(i.text()):
                    max = int(i.text())
        if sana==16:
            sana = 0
            self.msg = QMessageBox()
            self.msg.setIcon(self.msg.Information)
            self.msg.setText(f'Game over!\nYour score {max}')
            self.msg.buttonClicked.connect(self.reset)
            self.msg.exec_()
        
app = QApplication([])
window = Window()
window.generate()
window.show()
app.exec_()