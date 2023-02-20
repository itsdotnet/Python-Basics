from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
with open('dictionary.txt') as dic:
    dic = dic.read().split('\n')
    
class ADD(QWidget):
    def __init__(self):
        super().__init__()

        self.hBtnEditLay = QHBoxLayout()
        self.vEditLay = QVBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engEdit = QLineEdit()
        self.engEdit.setPlaceholderText("Eng...")

        self.uzEdit = QLineEdit()
        self.uzEdit.setPlaceholderText("Uzb...")

        self.okBtn = QPushButton("OK")
        self.okBtn.clicked.connect(self.ok)

        self.natijaLbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.vEditLay.addWidget(self.engEdit)
        self.vEditLay.addWidget(self.uzEdit)

        self.hBtnEditLay.addLayout(self.vEditLay)
        self.hBtnEditLay.addWidget(self.okBtn)

        self.vMainLay.addLayout(self.hBtnEditLay)
        self.vMainLay.addWidget(self.natijaLbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def ok(self):

        
        
        if self.engEdit.text()=='' or self.uzEdit.text()=='':
            self.natijaLbl.setText('No\'to\'g\'ri malumot kiritdingiz !')
            self.natijaLbl.adjustSize()
        else:
            co = 0
            for i in dic:
                i = i.split()
                if self.engEdit.text()==i[0] or self.uzEdit.text()==i[1]:
                    self.natijaLbl.setText("Bu so'z allaqachon mavjud !")
                    self.natijaLbl.adjustSize()
                    co = 1
            if co==0:
                dic.append(f"{self.engEdit.text()}{' '*(20-len(self.engEdit.text()))}{self.uzEdit.text()}")
                self.natijaLbl.setText("So'z qo'shildi !")
                
                        # paused 
        self.engEdit.clear()
        self.uzEdit.clear()
                
    def menu(self):
        self.engEdit.clear()
        self.uzEdit.clear()
        self.natijaLbl.setText("")
        self.close()

class SEARCH(QWidget):
    def __init__(self):
        super().__init__()

        self.hRadioLay = QHBoxLayout()
        self.hEditBtnLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.EngRadio = QRadioButton("English")
        self.EngRadio.setChecked(True)
        self.UzRadio = QRadioButton('Uzbek')

        self.Edit = QLineEdit()

        self.searchBtn = QPushButton("search")
        self.searchBtn.clicked.connect(self.search)

        self.lbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.hRadioLay.addWidget(self.EngRadio)
        self.hRadioLay.addWidget(self.UzRadio)

        self.hEditBtnLay.addWidget(self.Edit)
        self.hEditBtnLay.addWidget(self.searchBtn)

        self.vMainLay.addLayout(self.hRadioLay)
        self.vMainLay.addLayout(self.hEditBtnLay)
        self.vMainLay.addWidget(self.lbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def search(self):
        global dic
        co = True
        if self.EngRadio.isChecked():
            for i in dic:
                i = i.split()
                if i[0]==self.Edit.text():
                    self.lbl.setText(i[1])
                    self.lbl.adjustSize()
                    co=False
        elif self.UzRadio.isChecked():
            for i in dic:
                i = i.split()
                if i[1]==self.Edit.text():
                    self.lbl.setText(i[0])
                    self.lbl.adjustSize()
                    co=False
        if co:
            self.lbl.setText("Bunday so'z topilmadi !")
            self.lbl.adjustSize()

    def menu(self):
        self.Edit.clear()
        self.lbl.clear()
        self.close()

class LIST(QWidget):
    def __init__(self):
        super().__init__()

        self.hLblLay = QHBoxLayout()
        self.hListWidgLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engLbl = QLabel("English")
        self.uzLbl = QLabel("Uzbek")

        self.engListWdg = QListWidget()
        self.uzListWdg = QListWidget()
        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)
        
        global dic
        
        pic = dic.copy()
        for i in range(len(pic)):
            pic[i]=pic[i].split()
            self.engListWdg.addItem(f"{i+1}-{pic[i][0]}")
            self.uzListWdg.addItem(f"{i+1}-{pic[i][1]}")

        self.hLblLay.addWidget(self.engLbl)
        self.hLblLay.addWidget(self.uzLbl)

        self.hListWidgLay.addWidget(self.engListWdg)
        self.hListWidgLay.addWidget(self.uzListWdg)

        self.vMainLay.addLayout(self.hLblLay)
        self.vMainLay.addLayout(self.hListWidgLay)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)
    
    def menu(self):
        self.engListWdg.clear()
        self.uzListWdg.clear()
        self.close()

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.addWindow = ADD()
        self.searchWindow = SEARCH()

        self.vBtnLay = QVBoxLayout()
        self.hMainLay = QHBoxLayout()

        self.addBtn = QPushButton("ADD")
        self.addBtn.clicked.connect(lambda: self.addWindow.show())

        self.searchBtn = QPushButton("SEARCH")
        self.searchBtn.clicked.connect(self.searchWindow.show)
        
        self.listBtn = QPushButton("LIST")
        self.listBtn.clicked.connect(self.show_list)

        self.exitBtn = QPushButton("EXIT")
        self.exitBtn.clicked.connect(self.exit)

        self.vBtnLay.addWidget(self.addBtn)
        self.vBtnLay.addWidget(self.searchBtn)
        self.vBtnLay.addWidget(self.listBtn)
        self.vBtnLay.addWidget(self.exitBtn)

        self.hMainLay.addStretch()
        self.hMainLay.addLayout(self.vBtnLay)
        self.hMainLay.addStretch()
        self.setLayout(self.hMainLay)

    def show_list(self):
        self. listWindow = LIST()
        self. listWindow.show()

    def exit(self):
            global dic
            
            with open("dictionary.txt","w") as fil:
                for i in range(len(dic)):
                    if i!=len(dic)-1:
                        fil.write(f"{dic[i]}\n")
                    else:
                        fil.write(f"{dic[i]}")
            self.close()

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()