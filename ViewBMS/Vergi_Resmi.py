


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaxOfficial(object):
    def __init__(self):
        self.winTaxOfficial = QtWidgets.QMainWindow()
        self.setupUi(self.winTaxOfficial)
        self.winTaxOfficial.show()

    def setupUi(self, TaxOfficial):
        TaxOfficial.setObjectName("TaxOfficial")
        TaxOfficial.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(TaxOfficial)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 500, 380))
        self.toolBox.setMinimumSize(QtCore.QSize(1, 2))
        self.toolBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.toolBox.setSizeIncrement(QtCore.QSize(2, 0))
        self.toolBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 500, 326))
        self.page.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(220, 10, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(260, 120, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 270, 71, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(240, 190, 111, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(220, 71, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.page)
        self.commandLinkButton.setGeometry(QtCore.QRect(410, 290, 81, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 500, 326))
        self.page_2.setObjectName("page_2")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 10, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(70, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 80, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 140, 71, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(240, 200, 111, 61))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 280, 71, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.page_2)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(410, 290, 81, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.toolBox.addItem(self.page_2, "")
        TaxOfficial.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TaxOfficial)
        self.statusbar.setObjectName("statusbar")
        TaxOfficial.setStatusBar(self.statusbar)

        self.retranslateUi(TaxOfficial)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(TaxOfficial)

    def retranslateUi(self, TaxOfficial):
        _translate = QtCore.QCoreApplication.translate
        TaxOfficial.setWindowTitle(_translate("TaxOfficial", "Vergi Ve Resmi Kurum"))
        self.label.setText(_translate("TaxOfficial", "Plaka No"))
        self.pushButton.setText(_translate("TaxOfficial", "Sorgula"))
        self.label_2.setText(_translate("TaxOfficial", "Ödenecek Tutar"))
        self.pushButton_2.setText(_translate("TaxOfficial", "ÖDE"))
        self.label_3.setText(_translate("TaxOfficial", "Vergi Dönemi"))
        self.comboBox.setItemText(0, _translate("TaxOfficial", "Seçiniz"))
        self.comboBox.setItemText(1, _translate("TaxOfficial", "2019"))
        self.comboBox.setItemText(2, _translate("TaxOfficial", "2018"))
        self.comboBox.setItemText(3, _translate("TaxOfficial", "2017"))
        self.comboBox.setItemText(4, _translate("TaxOfficial", "2016"))
        self.comboBox.setItemText(5, _translate("TaxOfficial", "2015"))
        self.commandLinkButton.setText(_translate("TaxOfficial", "GERİ"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("TaxOfficial", "Motorlu Taşıtlar Vergisi"))
        self.label_5.setText(_translate("TaxOfficial", "Plaka No"))
        self.label_6.setText(_translate("TaxOfficial", "Tel no"))
        self.pushButton_3.setText(_translate("TaxOfficial", "Sorgula"))
        self.label_7.setText(_translate("TaxOfficial", "Ödenecek Tutar"))
        self.pushButton_4.setText(_translate("TaxOfficial", "ÖDE"))
        self.commandLinkButton_2.setText(_translate("TaxOfficial", "GERİ"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("TaxOfficial", "Trafik Cezası"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TAX_OFFİCİAL = Ui_TaxOfficial()
    sys.exit(app.exec_())