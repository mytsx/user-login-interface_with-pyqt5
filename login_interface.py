# Kapatma butonu eklenebilir
# dekoratif butonlara işlevsiz butonlara basıldığında basılan buton da dahil diğer butonların renginin random olarak değişmesi
#       özelliği eklenebilir. (bence sol alta) # değişik olur
# qss dosyaların dışarı dan çekilmesi
# kullanıcı parola ve kullanıcı adı kontrolü eklenebilir vs.


from PyQt5 import QtCore, QtGui, QtWidgets

import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 450))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_8.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)


        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.generate_box(self.horizontalLayout_10, 5, "0,0,0") # # # # #
        # self.decoratifButton(
        #     Layout = self.horizontalLayout_10,
        #     harf="LOGIN",
        #     fontFamily = "Terminal",
        #     fontSize=40,
        #     color= "0, 0, 0"
        # )


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 185, 89);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(0, 185, 89);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)

        self.generate_box(self.horizontalLayout_10, 1, "0,0,0") # 

        self.gridLayout.addLayout(self.horizontalLayout_10, 6, 0, 1, 1)


        # en alt
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.generate_box(self.horizontalLayout_14, 8, "0,0,0") # # # # # # # #
        self.gridLayout.addLayout(self.horizontalLayout_14, 7, 0, 1, 1)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.generate_box(self.horizontalLayout_12, 8, "0,0,0") # # # # # # # #
        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)
        
        # login ile email arasında
        # self.horizontalLayout_12.itemAt(0).widget().setStyleSheet(
        #     "background-color: rgb(0, 255,0);"
        # )

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.generate_box(self.horizontalLayout_13, 8, "0,0,0") # # # # # # # #
        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        # en üst
        # self.horizontalLayout_13.itemAt(0).widget().setStyleSheet(
        #     "background-color: rgb(0, 255,0);"
        # )

        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.generate_box(self.horizontalLayout_16, 8, "0,0,0") # # # # # # # #
        self.gridLayout.addLayout(self.horizontalLayout_16, 4, 0, 1, 1)

        # login butonun satırında
        # self.horizontalLayout_10.itemAt(0).widget().setStyleSheet(
        #     "background-color: rgb(0, 255,0);"
        # )


        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.generate_box(self.horizontalLayout_11, 1, "0,0,0") #
        self.decoratifButton(
            Layout = self.horizontalLayout_11, 
            harf="L",
            fontFamily="Swis721 BlkOul BT",
            color= "185, 0, 0"
            )
        self.decoratifButton(
            Layout = self.horizontalLayout_11, 
            harf="O",
            fontFamily="Rockwell",
            color= "85, 255, 255"
            )
        self.decoratifButton(
            Layout = self.horizontalLayout_11, 
            harf="G",
            fontFamily="Swis721 BlkOul BT",
            color= "26, 26, 255"
            )
        self.generate_box(self.horizontalLayout_11, 1, "0,0,0") #
        self.decoratifButton(
            Layout = self.horizontalLayout_11, 
            harf="I",
            fontFamily="Rockwell",
            color= "255, 255, 0"
            )
        self.decoratifButton(
            Layout = self.horizontalLayout_11, 
            harf="N",
            fontFamily="Swis721 BlkOul BT",
            color= "255, 85, 0"
            )
        
        self.generate_box(self.horizontalLayout_11, 1, "0,0,0") #
        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{║\n"
"font-family: System;\n"
"font-size: 45px;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.giris1)
    def generate_box(self, horLay, tane, color):
        for i in range(tane):
            self.widget_x = QtWidgets.QWidget(self.centralwidget)
            self.widget_x = QtWidgets.QWidget(self.centralwidget)
            self.widget_x.setMinimumSize(QtCore.QSize(60, 60))
            self.widget_x.setMaximumSize(QtCore.QSize(60, 60))
            self.widget_x.setStyleSheet("background-color: rgb({}, 50%);".format(color))
            # self.widget_x.setObjectName("widget_8")
            horLay.addWidget(self.widget_x)
        self.index_c = 0
    def giris1(self):
        self.uyu(self.giris, count = 8, interval=160)
        self.widget_y = QtWidgets.QWidget(self.centralwidget)
        self.widget_y = QtWidgets.QWidget(self.centralwidget)
        self.widget_y.setMinimumSize(QtCore.QSize(60, 60))
        self.widget_y.setMaximumSize(QtCore.QSize(60, 60))
        self.widget_y.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalLayout_10.itemAt(5).widget().deleteLater()
        # self.horizontalLayout_10.removeWidget(self.horizontalLayout_10.itemAt(6).widget())
        self.horizontalLayout_10.insertWidget(6,self.widget_y)
        self.widget_a = QtWidgets.QWidget(self.centralwidget)
        self.widget_a = QtWidgets.QWidget(self.centralwidget)
        self.widget_a.setMinimumSize(QtCore.QSize(60, 60))
        self.widget_a.setMaximumSize(QtCore.QSize(60, 60))
        self.widget_a.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalLayout_10.itemAt(5).widget().deleteLater()
        self.horizontalLayout_10.insertWidget(5, self.widget_a)
        # parola giriş kısmını sil ve 8 adet beyaz widget ekle
        self.horizontalLayout_8.itemAt(0).widget().deleteLater()
        self.generate_box(self.horizontalLayout_8, 8, "255,255,255")
        self.horizontalLayout_7.itemAt(0).widget().deleteLater()
        self.generate_box(self.horizontalLayout_7, 8, "255,255,255")
        # butonları sil ve yerine kendi renlerinde widget ekle
        decoratif_buton_indexleri_ve_color = [[1, "185, 0, 0"],
                                              [2, "85, 255, 255"],
                                              [3, "26, 26, 255"],
                                              [4, "0,0,0"],
                                              [5, "255, 255, 0"],
                                              [6, "255, 85, 0"]]
        for index, color in decoratif_buton_indexleri_ve_color:
            if index!= 4:
                self.horizontalLayout_11.itemAt(index).widget().deleteLater()
        self.horizontalLayout_11.itemAt(7).widget().deleteLater()
        for index, color in decoratif_buton_indexleri_ve_color:
            self.widget_b = QtWidgets.QWidget(self.centralwidget)
            self.widget_b = QtWidgets.QWidget(self.centralwidget)
            self.widget_b.setMinimumSize(QtCore.QSize(60, 60))
            self.widget_b.setMaximumSize(QtCore.QSize(60, 60))
            self.widget_b.setStyleSheet("background-color: rgb({}, 50%);".format(color))
            self.horizontalLayout_11.insertWidget(index, self.widget_b)
        self.func_list = [self.giris_1, self.giris_2, self.giris_3, self.giris_4, self.giris_5, self.giris_6, self.giris_7]
        self.intervals_1 = [80,40,20,20,20,15,20]
        self.func_syc = 0
    
            

    def giris(self, counter):
        self.horizontalLayout_14.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_1(self, counter):
        # if self.index_c == 0:
        #     self.gridLayout.removeItem(self.horizontalLayout_14)
            # print(self.gridLayout.countk())
        self.horizontalLayout_10.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_2(self, counter):
        # if self.index_c == 0:
        #     self.gridLayout.removeItem(self.horizontalLayout_10)
            # print(self.gridLayout.count())
        self.horizontalLayout_8.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_3(self, counter):
        # if self.index_c == 0:
            # self.gridLayout.removeItem(self.horizontalLayout_8)
            # print(self.gridLayout.count())
        self.horizontalLayout_16.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_4(self, counter):
        # if self.index_c == 0:
            # self.gridLayout.removeItem(self.horizontalLayout_16)
            # print(self.gridLayout.count())
        self.horizontalLayout_7.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_5(self, counter):
        # if self.index_c == 0:
            # self.gridLayout.removeItem(self.horizontalLayout_7)
            # print(self.gridLayout.count())
        self.horizontalLayout_12.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_6(self, counter):
        # if self.index_c == 0:
            # self.gridLayout.removeItem(self.horizontalLayout_12)
            # print(self.gridLayout.count())
        self.horizontalLayout_11.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
    def giris_7(self, counter):
        # if self.index_c == 0:
            # self.gridLayout.removeItem(self.horizontalLayout_11)
            # print(self.gridLayout.count())
        self.horizontalLayout_13.itemAt(self.index_c).widget().setStyleSheet("background-color: rgb(0, 255,0);")
        self.index_c +=1
        if self.index_c == 7:
            self.horizontalLayout_13.itemAt(7).widget().setStyleSheet("background-color: rgb(0, 255,0);")

    def uyu(self, slot, count=1, interval=15):
        self.count = count
        counter = 0
        def handler():
            nonlocal counter
            counter += 1
            slot(counter) #giris
            if counter >= count:
                timer.stop()
                timer.deleteLater()
                self.index_c = 0
                try:
                    self.uyu(self.func_list[self.func_syc],
                                            count=8,
                                            interval=self.intervals_1[self.func_syc] )
                except : # burada da yine qtimer kullanılması gerekiyor.
                    self.uyu_2(self.sil_lg, 1)
                    self.func_list_lay = [
                        self.sil_lg,
                        self.sil_lg1,
                        self.sil_lg2,
                        self.sil_lg3,
                        self.sil_lg4,
                        self.sil_lg5,
                        self.sil_lg6,
                        self.sil_lg7,

                    ]
                    self.func_lay_syc = 0


                self.func_syc += 1
        timer = QtCore.QTimer()
        timer.timeout.connect(handler)
        timer.start(interval)
    def sil_lg(self, counter):
        pass
        # for i in range(8):
        #     self.horizontalLayout_13.itemAt(i).widget().deleteLater()
    def sil_lg1(self, counter):
        print("sil_lg1")
        for i in range(8):
            self.horizontalLayout_11.itemAt(i).widget().deleteLater()
    def sil_lg2(self, counter):
        for i in range(8):
            self.horizontalLayout_12.itemAt(i).widget().deleteLater()
    def sil_lg3(self, counter):
        for i in range(8):
            self.horizontalLayout_7.itemAt(i).widget().deleteLater()
    def sil_lg4(self, counter):
        for i in range(8):
            self.horizontalLayout_16.itemAt(i).widget().deleteLater()
    def sil_lg5(self, counter):
        for i in range(8):
            self.horizontalLayout_8.itemAt(i).widget().deleteLater()
    def sil_lg6(self, counter):
        for i in range(8):
            self.horizontalLayout_10.itemAt(i).widget().deleteLater()
    def sil_lg7(self, counter):
        for i in range(8):
            self.horizontalLayout_14.itemAt(i).widget().deleteLater()

    def uyu_2(self, slot, count=1, interval=100):
        self.count = count
        counter = 0
        def handler():
            nonlocal counter
            counter += 1
            slot(counter) #giris
            if counter >= count:
                timer.stop()
                timer.deleteLater()
                try:
                    self.uyu_2(self.func_list_lay[self.func_lay_syc], count=1)
                    self.func_lay_syc += 1
                except:
                    
                    for i in range(8):
                         self.horizontalLayout_13.itemAt(i).widget().deleteLater()
   
                    print("bitti")
                    sys.exit()
                    pass
        timer = QtCore.QTimer()
        timer.timeout.connect(handler)
        timer.start(interval)
        


    def decoratifButton(self, Layout ,harf, fontFamily, color, fontSize=50):
        self.pushButton_x = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_x.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_x.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily(fontFamily)
        font.setPointSize(fontSize)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_x.setFont(font)
        self.pushButton_x.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_x.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_x.setAutoFillBackground(False)
        self.pushButton_x.setStyleSheet("\n"
"\n"
"QPushButton {\n"
f"    background-color: rgb({color}, 70%);\n"
"    color: rgb(0, 185, 89);\n"
"    border: 0px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(0, 185, 89);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: inset;\n"
"}")
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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Parola"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Email Adresi"))
import sources1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
