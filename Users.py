import sqlite3

user = sqlite3.connect('Users.db')

cursor = user.cursor()

class User:
    def User():
        UserID = " "
        loggedIn = False


    #def User(databaseName, tableName):
        

        
    def login():
        UserID = input("UserID:")
        password = input("Password:")
        cursor.execute('SELECT Users.Password, Users.UserID FROM Users WHERE UserID=? AND Password=?', (UserID,password))
        row = cursor.fetchone()
        if row:
            print("Login Success")
            loggedIn =True
            return True
        else:
            print("Login Failed")
            loggedIn = False
            return False

    def creatAccount():
        




user = User()

user.login()