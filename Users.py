import sqlite3


class User:
    def _init_(self, databaseName, tableName):
        self.loggedIn = False
        self.userID = " "
        self.database = databaseName
        self.tableName = tableName


        
    def login(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()

        self.userID = input("UserID:")
        password = input("Password:")
        cursor.execute('SELECT Users.Password, Users.UserID FROM ? WHERE UserID=? AND Password=?', (self.tableName,self.userID,password))
        row = cursor.fetchone()
        if row:
            print("Login Success")
            self.loggedIn =True
            return True
        else:
            print("Login Failed")
            self.loggedIn = False
            return False

    def logout(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()
        
        self.userID = " "
        self.loggedIn = False
        return False

    def viewAccountInformation(self):
        print()



def main():
    user1 =User('Users.db', 'Users')

    user1.login()