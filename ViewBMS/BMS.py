
# created by beyza at 2019-11-27 15:49.
# email : beyzakarali4743@gmail.com

from PyQt5 import QtCore, QtGui, QtWidgets
from ViewBMS.ParaTransferi import Ui_MoneyTransfer
from ViewBMS.Odemeler import Ui_Payments
from ViewBMS.Bagis import Ui_Donation
from ViewBMS.Fatura import Ui_Bill
from ViewBMS.Ayarlar import Ui_Settings 
from ViewBMS.Krediler import Ui_Credit
from ModelBMS.database import Database as db
from ControllerBMS.UserCls import User as usr


#Ana menü sayfası
class Ui_BMS(object):
    def __init__(self, User : usr):
        self.onlineUser = User
        self.winBMS = QtWidgets.QMainWindow()
        self.setupUi(self.winBMS)
        self.winBMS.show()

    #Güvenli çıkış.
    def ShutDown(self):
        self.winBMS.close()
    
    def MoneyTransferPage(self):
        self.winBMS.hide()
        self.win = Ui_MoneyTransfer(self.winBMS)

    def PaymentsPage(self):
        self.winBMS.hide()
        self.win = Ui_Payments(self.winBMS)

    def SettingPage(self):
        self.winBMS.hide()
        self.win = Ui_Settings(self.winBMS)
          
    def CreditPage(self):
       self.winBMS.hide()
       self.win = Ui_Credit(self.winBMS)
 

    def getUsersBank(self):
        userID = str(self.onlineUser.getID())
        banks = db.Query(db, "SELECT DISTINCT bank.Name FROM bank INNER JOIN account ON account.BankId = bank.ID WHERE account.customerID = %s"
                 , userID)
        self.viewBanks(banks)
    
    def viewBanks(self, banks):
        for bank in banks:
            self.comboBox.addItem(bank[0])

    
    def setupUi(self, BMS):
        BMS.setObjectName("BMS")
        BMS.resize(500, 400)
        BMS.setMinimumSize(QtCore.QSize(500, 400))
        BMS.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(BMS)
        self.centralwidget.setObjectName("centralwidget")


        #------------------------------
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 10, 181, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.getUsersBank()
        #------------------------------

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 100, 31, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        iconPath = "C:/Users/batu_/source/repos/BankManagementSystem/BankManagementSystem/icons/dolar.svg"
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 140, 31, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../FOTO/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 50, 31, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../FOTO/altın.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 61, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../FOTO/images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(95, 84))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 270, 171, 41))
        self.pushButton_6.clicked.connect(self.CreditPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 330, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.SettingPage)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(116, 100, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 100, 81, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")

        #lambda : isimsiz fonksiyon üretmeyi sağlar.
        self.pushButton_5.clicked.connect(self.MoneyTransferPage)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.PaymentsPage)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 270, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 330, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.ShutDown)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 110, 31, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_11.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../FOTO/tl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(52, 29))
        self.pushButton_11.setObjectName("pushButton_11")
        BMS.setCentralWidget(self.centralwidget)

        self.retranslateUi(BMS)
        QtCore.QMetaObject.connectSlotsByName(BMS)
        return BMS


    def retranslateUi(self, BMS):
        _translate = QtCore.QCoreApplication.translate
        BMS.setWindowTitle(_translate("BMS", "BMS"))
        self.comboBox.setItemText(0, _translate("BMS", "BANKA SEÇİNİZ"))

        self.label.setText(_translate("BMS", "BAKİYE"))
        self.label_2.setText(_translate("BMS", " BORÇLAR"))
        self.pushButton_5.setText(_translate("BMS", "PARA TRANSFERLERİ"))
        self.pushButton_6.setText(_translate("BMS", "KREDİ İŞLEMLERİ"))
        self.pushButton_7.setText(_translate("BMS", "AYARLAR"))
        self.pushButton_8.setText(_translate("BMS", "ÖDEMELER"))
        self.pushButton_9.setText(_translate("BMS", "HESAP HAREKETLERİ"))
        self.pushButton_10.setText(_translate("BMS", "GÜVENLİ ÇIKIŞ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BMS = Ui_BMS()
    sys.exit(app.exec_())
