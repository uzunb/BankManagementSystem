# created by beyza at 2019-11-27 15:49.
# email : beyzakarali4743@gmail.com

from PyQt5 import QtCore, QtGui, QtWidgets
from ViewBMS.ParaTransferi import Ui_MoneyTransfer
from ViewBMS.Odemeler import Ui_Payments
from ViewBMS.Bagis import Ui_Donation
from ViewBMS.Fatura import Ui_Bill
from ViewBMS.Ayarlar import Ui_Settings
from ViewBMS.Krediler import Ui_Credit

#incele ne işi var
from ModelBMS.database import Database as db
from ControllerBMS.UserCls import User as usr
from ControllerBMS.Bank import Bank 
from ControllerBMS.Account import Account


class Ui_BMS(object):

    def __init__(self, User : usr):
        self.onlineUser = User
        self.bk = Bank
        self.winBMS = QtWidgets.QMainWindow()
        self.setupUi(self.winBMS)
        self.winBMS.show()

    #Güvenli çıkış.
    def ShutDown(self):
        self.winBMS.close()

    #Para Transferleri ekranına geçiş.
    def MoneyTransferPage(self):
        self.winBMS.hide()
        self.win = Ui_MoneyTransfer(self.winBMS)

    #Ödemeler sayfasına geçiş.
    def PaymentsPage(self):
        self.winBMS.hide()
        self.win = Ui_Payments(self.winBMS)

    #Ayarlar sayfasına geçiş.
    def SettingPage(self):
        self.winBMS.hide()
        self.win = Ui_Settings(self.winBMS)

    #Krediler sayfasına geçiş.
    def CreditPage(self):
       self.winBMS.hide()
       self.win = Ui_Credit(self.winBMS)



    #BMS ekranında seçilen bankanın ID'sini döndürür.
    def returnSelectedBank(self):
        return self.comboBox.currentText()

    #User'ın ID sini geri döndürür.
    def returnOnlineUserID(self):
        return str(self.onlineUser.getID())


    def viewBalance(self):
        self.comboBox_2.curr




    #User'a ait bankaları döndürür. 
    def getUsersBank(self):
        clsBank = self.onlineUser.getBanks()
        self.viewBanks(clsBank)

    #User'a ait bankaları BMS ekranında listeler.
    def viewBanks(self, banks : Bank):
        for bank in banks:
            bankName = bank.getbankName()
            self.comboBox.addItem(bankName)
        print("Bankalar getirildi.")

    
    #BMS ekranına User'ın hesaplarını döndürür.
    def getUsersAccounts(self):
        clsAccounts = self.onlineUser.getAccounts()
        self.viewAccounts(clsAccounts)

    def viewAccounts(self, accounts : Account):
        for account in accounts:
            accountName = account.getAccountNo()
            self.comboBox_2.addItem(accountName)
        print("Hesaplar getirildi.")





######################### SAYFA DÜZENİ ###########################
#Pyuic5 generator ile otomatik oluşturulmuştur.


    def setupUi(self, BMS):
        BMS.setObjectName("BMS")
        BMS.resize(500, 400)
        BMS.setMinimumSize(QtCore.QSize(500, 400))
        BMS.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(BMS)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 0, 141, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.getUsersBank()
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 180, 31, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../FOTO/DOLAR.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 180, 31, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../FOTO/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 180, 31, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../FOTO/altın.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 60, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(41, 84))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 280, 171, 41))
        self.pushButton_6.clicked.connect(self.CreditPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 340, 171, 41))
        self.pushButton_7.clicked.connect(self.SettingPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 220, 171, 41))
        #lambda : isimsiz fonksiyon üretmeyi sağlar.
        self.pushButton_5.clicked.connect(self.MoneyTransferPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 220, 171, 41))
        self.pushButton_8.clicked.connect(self.PaymentsPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 280, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 340, 171, 41))
        self.pushButton_10.clicked.connect(self.ShutDown)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(180, 180, 31, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_11.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../FOTO/tl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(52, 29))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.label_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_5.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../BmsLogo.png"))
        self.label_5.setObjectName("label_5")

        #Hesaplar
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 30, 141, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.getUsersAccounts()
     

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 100, 151, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 140, 151, 31))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.comboBox.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_11.raise_()
        self.label_5.raise_()
        self.pushButton_7.raise_()
        self.pushButton_10.raise_()
        self.pushButton_6.raise_()
        self.comboBox_2.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        BMS.setCentralWidget(self.centralwidget)

        self.retranslateUi(BMS)
        QtCore.QMetaObject.connectSlotsByName(BMS)
        BMS.setTabOrder(self.comboBox, self.comboBox_2)
        BMS.setTabOrder(self.comboBox_2, self.pushButton_4)
        BMS.setTabOrder(self.pushButton_4, self.pushButton_11)
        BMS.setTabOrder(self.pushButton_11, self.pushButton_3)
        BMS.setTabOrder(self.pushButton_3, self.pushButton_2)
        BMS.setTabOrder(self.pushButton_2, self.pushButton)
        BMS.setTabOrder(self.pushButton, self.pushButton_5)
        BMS.setTabOrder(self.pushButton_5, self.pushButton_6)
        BMS.setTabOrder(self.pushButton_6, self.pushButton_7)
        BMS.setTabOrder(self.pushButton_7, self.pushButton_8)
        BMS.setTabOrder(self.pushButton_8, self.pushButton_9)
        BMS.setTabOrder(self.pushButton_9, self.pushButton_10)

    def retranslateUi(self, BMS):
        _translate = QtCore.QCoreApplication.translate
        BMS.setWindowTitle(_translate("BMS", "BMS"))
        self.pushButton_6.setText(_translate("BMS", "KREDİ İŞLEMLERİ"))
        self.pushButton_7.setText(_translate("BMS", "AYARLAR"))
        self.pushButton_5.setText(_translate("BMS", "PARA TRANSFERLERİ"))
        self.pushButton_8.setText(_translate("BMS", "ÖDEMELER"))
        self.pushButton_9.setText(_translate("BMS", "HESAP HAREKETLERİ"))
        self.pushButton_10.setText(_translate("BMS", "GÜVENLİ ÇIKIŞ"))
        self.label_7.setText(_translate("BMS", "<html><head/><body><p><span style=\" font-weight:600;\">Bakiye</span></p></body></html>"))
        self.label_2.setText(_translate("BMS", "<html><head/><body><p><span style=\" font-weight:600;\">Borçlar</span></p></body></html>"))


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    BMS = Ui_BMS(usr)
    sys.exit(app.exec_()) 