from PyQt5.QtWidgets import QApplication,QLabel,QComboBox,QPushButton,QWidget,QVBoxLayout,QHBoxLayout,QRadioButton,QLineEdit,QMessageBox
ls_andijon = ["","Andijon tumani","Asaka tumani","Bo'ston tumani","Buloqboshi tumani","Chinobod tumani",'Izboskan tumani',"Jalaquduq tumani","Marhamat tumani","Oltinko'l tumani","Paxtaobod tumani","Shahrixon tumani","Ulug'nor tumani","Xoldevonbek tumani","Xo'jaobod tumani"]
ls_buxuro = ["","Buxoro tumani","G'ijduvon tumani","Jondor tumani","Kogon tumani","Olot tumani","Peshko tumani","Qorako'l tumani","Qorovulbozor tumani",'Romitan tumani','Shofirkon tumani','Vobkent tumani']
ls_fergana = ["","Bag'dod tumani","Beshariq tumani","Buvayda tumani","Dang'ara tumani","Farg'ona tumani","Furqat tumani","Oltiariq tumani","O'zbekiston tumani","Qo'shtepa tumani","Quva tumani","Rishton tumani","So'x tumani","Toshloq tumani","Uchko'prik tumani","Yozyovon tumani"]
ls_jizzax = ["","Arnasoy tumani","Baxmal tumani","Do'stlik tumani","Forish tumani","G'allaorol tumani","Mirzacho'l tumani","Paxtakor tumani","Sharof Rashidov tumani","Yangiobod tumani","Zafarobod tumani","Zarbdor tumani","Zomin tumani"]
ls_xorazm = ["","Bog'ot tumani","Gurlan tumani","Qo'shko'pir tumani","Shovot tumani","Urganch shahri","Urganch tumani","Xazorasp tumani","Xiva tumani","Xonqa tumani","Yangiariq tumani","Yangibozor tumani"]
ls_namangan = ["","Chortoq tumani","Chust tumani","Kosonsoy tumani","Mingbuloq tumani","Namangan tumani","Norin tumani (O'zbekiston)","Pop tumani","To'raqo'rg'on tumani","Uchqo'rg'on tumani","Uychi tumani","Yangiqo'rg'on tumani","Davlatobod tumani"]
ls_navoiy = ["","Konimex tumani","Navbahor tumani","Navoiy tumani","Nurota tumani","Qiziltepa tumani","Tomdi tumani","Uchquduq tumani","Xatirchi tumani"]
ls_qashqadaryo = ["","Chiroqchi tumani","Dehqonobod tumani","G'uzor tumani","Kasbi tumani","Kitob tumani","Koson tumani","Mirishkor tumani","Muborak tumani","Nishon tumani","Qamashi tumani","Qarshi shahri","Shahrisabz shahri","Qarshi tumani","Yakkabog' tumani"]
ls_samarqand = ["","Bulung'ur tumani","Ishtixon tumani","Jomboy tumani","Kattaqo'rg'on shahri","Kattaqo'rg'on tumani","Narpay tumani","Nurobod tumani","Oqdaryo tumani","Past darg'om tumani","Paxtachi tumani","Poyariq tumani","Qo'shrabot tumani","Samarqand shahri","Samarqand tumani","Toyloq tumani","Urgut tumani"]
ls_sirdaryo = ["","Sirdaryo tumani","Guliston tumani","Boyovut tumani","Sharof Rashidov tumani","Hovos tumani","Sayxunobod tumani","Sardoba tumani","Oqoltin tumani","Mexnatobod tumani","Mirzaobod tumani"]
ls_surxandaryo = ["Angor tumani","Bandixon tumani","Boysun tumani","Denov tumani","Jarqo'rg'on tumani","Muzrobot tumani","Oltinsoy tumani","Qiziriq tumani","Qumqo'rg'on tumani","Sariosiyo tumani","Sherobod tumani","Sho'rchi tumani","Termiz shahri","Termiz tumani","Uzun tumani"]
ls_toshkent = ["","Toshkent shahri","Bekobod tumani","Bo'stonliq tumani","Bo'ka tumani","Chinoz tumani","Qibray tumani","Ohangaron tumani","Oqqo'rg'on tumani","Parkent tumani","Piskent tumani","Quyi Chirchiq tumani","O'rta Chirchiq tumani","Yangiyo'l tumani","Yuqori Chirchiq tumani","Zangiota tumani"]
dct_viloyat = {'Andijon':ls_andijon,'Buxoro':ls_buxuro,'Farg\'ona':ls_fergana,'Jizzax':ls_jizzax,'Xorazm':ls_xorazm,'Namangan':ls_namangan,'Navoiy':ls_navoiy,'Qashqadaryo':ls_qashqadaryo,'Samarqand':ls_samarqand,'Sirdaryo':ls_sirdaryo,'Surxondaryo':ls_surxandaryo,'Toshkent':ls_toshkent}
# app
app = QApplication([])
window = QWidget()
ism = QLineEdit()
isml = QLabel("Ism:\t")
familiya = QLineEdit()
familiyal = QLabel("Familiya:  ")
hori = QHBoxLayout()
ver = QVBoxLayout()
ism_ = QHBoxLayout()
familiya_ = QHBoxLayout()
ism_.addWidget(isml)
ism_.addWidget(ism)
familiya_.addWidget(familiyal)
familiya_.addWidget(familiya)
ver.addLayout(ism_)
ver.addLayout(familiya_)
tuman = QComboBox()
viloyat = QComboBox()
viloyat.addItems(dct_viloyat.keys())
btn_ok = QPushButton('ok')
btn_print = QPushButton("print")
def ok():
    tuman.clear()
    tuman.addItems(dct_viloyat[viloyat.currentText()])
btn_ok.clicked.connect(ok)
def pr():
    msg = QMessageBox()
    msg.setWindowTitle('Info')
    try:
        if erkak.isChecked():
            msg.setText(f"""Ism: {ism.text()}
Familiya: {familiya.text()}
Viloyat: {viloyat.currentText()}
Tuman: {tuman.currentText()}
Jinsi: Erkak""")
        elif ayol.clicked():
            msg.setText(f"""Ism: {ism.text()}
Familiya: {familiya.text()}
Viloyat: {viloyat.currentText()}
Tuman: {tuman.currentText()}
Jinsi: Ayol""")
    except:
        msg.setText(f"""Ism: {ism.text()}
Familiya: {familiya.text()}
Viloyat: {viloyat.currentText()}
Tuman: {tuman.currentText()}
Jinsi: Nomalum""")
    msg.show()
    msg.exec_()
btn_print.clicked.connect(pr)

lbl = QLabel("")
hori.addWidget(viloyat)
hori.addWidget(btn_ok)
horiz = QHBoxLayout()
ayol = QRadioButton("Ayol")
erkak = QRadioButton("Erkak")
horiz.addWidget(erkak)
horiz.addWidget(ayol)
ver.addWidget(lbl)
ver.addLayout(hori)
ver.addWidget(tuman)
ver.addLayout(horiz)
ver.addWidget(btn_print)
window.setLayout(ver)
window.setWindowTitle('Ma\'lumot')
window.show()
app.exec_()