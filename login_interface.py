# Kapatma butonu eklenebilir
# dekoratif butonlara işlevsiz butonlara basıldığında basılan buton da dahil diğer butonların renginin random olarak değişmesi
#       özelliği eklenebilir. (bence sol alta) # değişik olur
# qss dosyaların dışarı dan çekilmesi
# kullanıcı parola ve kullanıcı adı kontrolü eklenebilir vs.


import sources1_rc
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # penceresiz yapıldığı için buna gerek yok değil mi? Buna bir bak
        MainWindow.setObjectName("MainWindow")
        # sanki bu ismi versende vermesende default olarak bunu alıyor gibi
        MainWindow.resize(500, 450)

        MainWindow.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # penceresiz yapar
        MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 450))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        fontLineEdit = QFont("Consolas", 20, weight=75)
        fontLoginButton = QFont("Terminal", 30, 75)
        self.horizontalLayoutList = []
        
        def my_decorator(func):
            def wrapper(index):
                horLay= func()
                self.gridLayout.addLayout(horLay, index, 0, 1, 1) 
                self.horizontalLayoutList.append(horLay)
                
            return wrapper

        @my_decorator
        def satir():
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            # içerik
            self.generate_box(self.horizontalLayout, 8, "0,0,0")   
            
            return self.horizontalLayout   

        ####################### 0. SATIR ####################### es
        satir(0)
        ####################### 1. SATIR #######################
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()

        self.generate_box(self.horizontalLayout1, 1, "0,0,0")
        self.decoratifButton(
            Layout=self.horizontalLayout1,
            harf="L",
            fontFamily="Swis721 BlkOul BT",
            color="185, 0, 0"
        )
        self.decoratifButton(
            Layout=self.horizontalLayout1,
            harf="O",
            fontFamily="Swis721 BlkOul BT",
            color="85, 255, 255"
        )
        self.decoratifButton(
            Layout=self.horizontalLayout1,
            harf="G",
            fontFamily="Swis721 BlkOul BT",
            color="26, 26, 255"
        )
        self.generate_box(self.horizontalLayout1, 1, "0,0,0")
        self.decoratifButton(
            Layout=self.horizontalLayout1,
            harf="I",
            fontFamily="Swis721 BlkOul BT",
            color="255, 255, 0"
        )
        self.decoratifButton(
            Layout=self.horizontalLayout1,
            harf="N",
            fontFamily="Swis721 BlkOul BT",
            color="255, 85, 0"
        )

        self.generate_box(self.horizontalLayout1, 1, "0,0,0")
        self.gridLayout.addLayout(self.horizontalLayout1, 1, 0, 1, 1)
        self.horizontalLayoutList.append(self.horizontalLayout1)
        ####################### 2. SATIR #######################
        satir(2)
        ####################### 3. SATIR #######################
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()

        self.emailLE = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLE.setMinimumSize(QtCore.QSize(0, 60))
        self.emailLE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.emailLE.setFont(fontLineEdit)
        self.emailLE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.emailLE.setObjectName("emailLE")

        self.horizontalLayout3.addWidget(self.emailLE)
        
        self.gridLayout.addLayout(self.horizontalLayout3, 3, 0, 1, 1)
        self.horizontalLayoutList.append(self.horizontalLayout3)
        ####################### 4. SATIR #######################
        satir(4)
        ####################### 5. SATIR #######################
        self.horizontalLayout5 = QtWidgets.QHBoxLayout()

        self.passwordLE = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLE.setMinimumSize(QtCore.QSize(0, 60))
        self.passwordLE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.passwordLE.setFont(fontLineEdit)
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")

        self.horizontalLayout5.addWidget(self.passwordLE)
        self.gridLayout.addLayout(self.horizontalLayout5, 5, 0, 1, 1)
        self.horizontalLayoutList.append(self.horizontalLayout5)
        ####################### 6. SATIR #######################
        self.horizontalLayout6 = QtWidgets.QHBoxLayout()

        self.generate_box(self.horizontalLayout6, 5, "0,0,0")

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 60))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.loginButton.setFont(fontLoginButton)
        self.loginButton.setMouseTracking(True)
        self.loginButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.loginButton.setStyleSheet(open("loginButton.qss", "r").read())
        self.loginButton.setIconSize(QtCore.QSize(60, 60))
        self.loginButton.setAutoExclusive(False)
        self.loginButton.setObjectName("loginButton")

        self.horizontalLayout6.addWidget(self.loginButton)

        self.generate_box(self.horizontalLayout6, 1, "0,0,0")

        self.gridLayout.addLayout(self.horizontalLayout6, 6, 0, 1, 1)
        self.horizontalLayoutList.append(self.horizontalLayout6)
        ####################### 7. SATIR #######################
        satir(7)
        #######################   END    #######################


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loginButton.clicked.connect(self.prepareToAnimation)

    def generate_box(self, horLay, tane, color):
        for i in range(tane):
            self.widget_x = QtWidgets.QWidget(self.centralwidget)
            self.widget_x.setMinimumSize(QtCore.QSize(60, 60))
            self.widget_x.setMaximumSize(QtCore.QSize(60, 60))
            self.widget_x.setStyleSheet(
                "background-color: rgb({}, 50%);".format(color))

            horLay.addWidget(self.widget_x)
        self.index_c = 0

    def prepareToAnimation(self):
        for i in range(5, 7):
            self.horizontalLayout6.itemAt(i).widget().deleteLater()
            self.widget_y = QtWidgets.QWidget(self.centralwidget)
            self.widget_y.setMinimumSize(QtCore.QSize(60, 60))
            self.widget_y.setMaximumSize(QtCore.QSize(60, 60))
            self.widget_y.setStyleSheet(f"background-color: rgb(0,0,0);")
            self.horizontalLayout6.insertWidget(i, self.widget_y)

        # parola giriş kısmını sil ve 8 adet beyaz widget ekle
        self.horizontalLayout5.itemAt(0).widget().deleteLater()
        self.generate_box(self.horizontalLayout5, 8, "255,255,255")
        # email giriş kısmını sil ve 8 adet beyaz widget ekle
        self.horizontalLayout3.itemAt(0).widget().deleteLater()
        self.generate_box(self.horizontalLayout3, 8, "255,255,255")
        # butonları sil ve yerine kendi renlerinde widget ekle
        decoratif_buton_indexleri_ve_color = [[1, "185, 0, 0"],
                                              [2, "85, 255, 255"],
                                              [3, "26, 26, 255"],
                                              [4, "0,0,0"],
                                              [5, "255, 255, 0"],
                                              [6, "255, 85, 0"]]

        for index, color in decoratif_buton_indexleri_ve_color:
            self.widget_b = QtWidgets.QWidget(self.centralwidget)
            self.widget_b.setMinimumSize(QtCore.QSize(60, 60))
            self.widget_b.setMaximumSize(QtCore.QSize(60, 60))
            self.widget_b.setStyleSheet(
                f"background-color: rgb({color}, 50%);")
            self.horizontalLayout1.itemAt(index).widget().deleteLater()
            self.horizontalLayout1.insertWidget(
                index+len(decoratif_buton_indexleri_ve_color), self.widget_b)

        
        self.func_syc = 0
        self.intervals_ccow = [80, 40, 20, 20, 20, 15, 20]
        self.intervals_dw = [100 for i in range(7)]
        self.animateİnfo = {
            "ccow":
                {"plus" : +1,
                "carpan" : -1,
                "fonksiyon" : self.changeColorsOfWidgets,
                "itervals" : self.intervals_ccow},
            "dw" :
                {"plus" : -1,
                "carpan" : 1,
                "fonksiyon" : self.deleteWidgets,
                "itervals" : self.intervals_dw},}
        self.playWithWidgets(self.animateİnfo["ccow"]["fonksiyon"], count=8, interval=160, informations = self.animateİnfo["ccow"])


    def changeColorsOfWidgets(self, horlay): 
        horlay.itemAt(self.index_c).widget(
        ).setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c += 1
    def deleteWidgets(self, horLay):
        self.func_syc+=1
        for i in range(8):
            horLay.itemAt(i).widget().deleteLater()
        if self.func_syc == 9:
            print("bitti")
            sys.exit()

    def playWithWidgets(self, slot, count, interval, informations):
        inf = informations
        self.count = count  # 8
        counter = 0
        def handler(): 
            nonlocal counter
            counter += 1
            slot(self.horizontalLayoutList[(self.func_syc+inf["plus"])*inf["carpan"]])
            # ilk çalıştırmada count = 8, counter = 1 olduğundan if'e girmiyor.
            # ve giris(f) 8' kere çalışıp counter(syc) 9'a geldiğinde
            # bir sonraki giris1(f) fonksiyonuna girip timer'ı ona göre kurup tekrarlıyor
            if counter >= count:
                timer.stop()
                timer.deleteLater()
                self.index_c = 0
                try:
                    self.playWithWidgets(inf["fonksiyon"],
                             count=8,
                             interval=inf["itervals"][self.func_syc], informations=inf)
                except:  # burada da yine qtimer kullanılması gerekiyor.
                    self.func_syc = 0
                    self.playWithWidgets(self.animateİnfo["dw"]["fonksiyon"], 8,100,informations = self.animateİnfo["dw"])

                self.func_syc += 1
        timer = QtCore.QTimer()
        timer.timeout.connect(handler)
        timer.start(interval)




    def decoratifButton(self, Layout, harf, fontFamily, color):
        fontdecoratifButton = QFont(fontFamily, 50, weight=75)

        self.pushButton_x = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_x.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_x.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_x.setFont(fontdecoratifButton)
        self.pushButton_x.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_x.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_x.setAutoFillBackground(False)

        buttonStyle = open("decoratifButton.qss", "r").read()
        bS1 = buttonStyle[:buttonStyle.find("{")+1]
        bS2 = f"\nbackground-color: rgb({color}, 70%);"
        bS3 = buttonStyle[buttonStyle.find("{")+1:]
        finalButtonStyle = "".join((bS1, bS2, bS3))
        self.pushButton_x.setStyleSheet(finalButtonStyle)

        # self.pushButton_x.setStyleSheet(f"background-color: rgb({color}, 70%)")
        self.pushButton_x.setCheckable(False)
        self.pushButton_x.setAutoDefault(False)
        self.pushButton_x.setDefault(True)
        self.pushButton_x.setFlat(False)
        self.pushButton_x.setObjectName("pushButton_x")
        Layout.addWidget(self.pushButton_x)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_x.setText(_translate("MainWindow", harf))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.passwordLE.setPlaceholderText(_translate("MainWindow", "Parola"))
        self.emailLE.setPlaceholderText(
            _translate("MainWindow", "Email Adresi"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
