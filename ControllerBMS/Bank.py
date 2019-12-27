# created by buzun at 2019-12-03 18:25.
# email : batuuzun08@gmail.com
# edited by beyza at 2019-12-05 20:07.

from ModelBMS.database import Database


class Bank:
    def __init__(self, bankInformations):
        self.__ID = bankInformations[0]
        self.__bankName = bankInformations[1]
        self.__phoneNumber = bankInformations[2]
        self.db = Database
        #self.onlineUser = User

    #getter and setter function
    def  setID(self, newID):
        self.__ID = newID

    def setbankName(self, newbankName):
        self.__bankName = newbankName

    def setphoneNumber(self, newphoneNumber):
        self.__phoneNumber = newphoneNumber
    
    def  getID(self):
        return self.__ID     

    def getbankName(self):
        return self.__bankName   

    def getphoneNumber(self):
        return self.__phoneNumber 

    # read database 
    # account activities
    # user info 
    def viewAllDetails(self):
        pass


    @classmethod
    def setBanks(cls, userID):
        query = "SELECT ID, Name, Phone FROM bank WHERE EXISTS (SELECT DISTINCT account.BankId FROM account INNER JOIN customer ON customerID = customer.ID WHERE customerID = %s)"
        banks = Database.Query(Database, query, userID)
        clsBanks : Bank = []
        for bank in banks:
            clsBanks.append(cls(bank))
        
        return clsBanks




    def createUsersBanks(self, userID):
        query = "SELECT DISTINCT bank.ID, bank.Name, bank.Phone FROM bank INNER JOIN account ON account.BankId = bank.ID WHERE account.customerID = %s"
        banks = self.db.Query(Database, query, userID)
        for bankInformation in banks:
            self.onlineUser.banks.append(Bank(bankInformation))


    #def getUsersBank(self):
    #    return self.onlineUser.banks
    