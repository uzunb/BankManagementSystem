import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox
import numpy as np

class Database:
    def __init__(self):
        self.connection : mysql.connector


    #Veritabanına bağlanma.
    def connectDatabase(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                database = "bmsdb",
                user = "root",
                password = ""
                )

        except mysql.connector.Error as error:
            print("Database.py BAĞLANMA HATASI")
            print("Failed to connect to database {} ".format(error))
            self.showErrorDialog("VERİTABANI BAĞLANTI HATASI", "Veritabanı bağlantısını etkinleştiriniz.")
            exit(code=-1)
        
        print("Database connected...")

        return self.connection



    
    #Veritabanı bağlantısını kesme.
    def disconnectDatabase(self):
        try:
            self.connection.close()
        except mysql.connector.Error as error:
            print("Database.py BAĞLANTI KESME HATASI")
            print("Failed to close database connection {}".format((error)))

        print("Database disconnected...")




  
    #Kimlik doğrulama
    def getUserInformations(self, username, password):
        query = "SELECT * FROM customer WHERE Username = %s AND password = %s"
        try:
            informationsOfUser = self.Query(query, username, password)
            
            print(informationsOfUser)
        except Error as msgError:
            print(msgError)
        
        if(informationsOfUser == []):
            return False
        else:
            return informationsOfUser

    
    def isNestedArray(self, info):
        if(np.size(info[0]) > 1 ):
            info = info[0]
        return info

    
    
    #Veritabanı sorgusu yapma.
    def Query(self, query : str, *info):
        info = self.isNestedArray(self, info)

        try:
            self.connection = self.connectDatabase(self)
            
            cursor = self.connection.cursor()
            cursor.execute(query, info)
        except Error as er:
            print("QUERY FUNCTION HATA")
            print(er)
        try:
            result = cursor.fetchall()
        except Error as er:
            result = self.connection.commit()

        self.disconnectDatabase(self)
        print(result)
        return result

    #random Customer ekleme
    def randCustomer(self):
        try:
            connection = self.getDbConnection()
            cursor = connection.cursor()
            with open("customer.txt", "r") as dosya:
                for query in dosya:
                    result = cursor.execute(query)
                    connection.commit()

        except mysql.connector.Error as error:
            print("Failed to insert Customer table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Mysql connection is closed")

        

    def convertToBinaryData(self, filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData




    def writeImg(self, data, filename):
        with open(filename,'wb') as file:
            file.write(data)




    #Cursor oluşturma
    def createCursor(self):
        cursor = connection.cursor()
        return cursor



    @staticmethod
    def showErrorDialog(title, text, informativeText = ""):
            msg = QMessageBox()
            msg.setWindowTitle(title)
            msg.setText(text)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText(informativeText)
            x = msg.exec_()