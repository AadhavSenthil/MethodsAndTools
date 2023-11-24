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
        cursor.execute(f'SELECT Users.Password, Users.UserID FROM {self.tableName} WHERE UserID=? AND Password=?', (self.userID,password))
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
        
        if self.loggedIn == True:
            cursor.execute(f"UPDATE {self.tableName} SET UserID = ? WHERE UserID = {self.userID} ")
            self.userID = " "
            self.loggedIn = False

        return False

    def viewAccountInformation(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()
        if self.loggedIn == True:
            cursor.execute(f'SELECT * FROM {self.tableName} WHERE UserID=?', (self.userID))
            row = cursor.fetchone()
            print("Account Info:")
            if not row:
                print("No matching User.")
            else:
                print(row)

        else:
            print("Please Login to see Account Information.")


    def createAccount(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()
        self.userID = input("UserID: ")
        email = input("Email: ")
        password = input("Password: ")
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip = ("Zip: ")
        payment = ("Payment: ")

        cursor.execute(f"INSERT INTO {self.tableName} (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.userID, email, password, firstName, lastName, address, city, state, zip, payment))
        user.commit()

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID







def main():
    user1 =User('Users.db', 'Users')
    
    user1.createAccount()

    user1.login()